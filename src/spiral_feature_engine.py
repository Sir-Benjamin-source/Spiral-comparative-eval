"""
Spiral Feature Hypothesis Engine

Translates the Spiral Path process into concrete feature selection /
hypothesis generation for tabular data.

Public stages:
  Candidate  → notice potentially useful features / interactions
  Under-test → score and refine them against held-out performance
  Verified   → only features that survive the loop are kept

This is deliberately simple and fully auditable for the first public campaign.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from typing import List, Dict, Any, Tuple
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import cross_val_score
import json
from datetime import datetime


class SpiralFeatureEngine:
    def __init__(self, task: str = "classification", random_state: int = 42, max_features: int = 20):
        self.task = task
        self.random_state = random_state
        self.max_features = max_features
        self.log: List[Dict[str, Any]] = []
        self.selected_features_: List[str] = []
        self.feature_scores_: Dict[str, float] = {}

    def _base_model(self):
        if self.task == "classification":
            return RandomForestClassifier(
                n_estimators=50, max_depth=6, random_state=self.random_state, n_jobs=-1
            )
        else:
            return RandomForestRegressor(
                n_estimators=50, max_depth=6, random_state=self.random_state, n_jobs=-1
            )

    def _score_features(self, X: pd.DataFrame, y: np.ndarray, feature_list: List[str]) -> Dict[str, float]:
        if len(feature_list) == 0:
            return {}
        model = self._base_model()
        model.fit(X[feature_list], y)
        importances = model.feature_importances_
        return {f: float(imp) for f, imp in zip(feature_list, importances)}

    def generate_candidates(self, X: pd.DataFrame, y: np.ndarray) -> List[str]:
        scores = self._score_features(X, y, list(X.columns))
        ranked = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
        candidates = [f for f, _ in ranked[: self.max_features]]
        self._log_event("candidate_generation", {
            "n_candidates": len(candidates),
            "top_5": candidates[:5],
            "scores": {k: scores[k] for k in candidates[:10]}
        })
        return candidates

    def refine(self, X: pd.DataFrame, y: np.ndarray, candidates: List[str],
               n_cycles: int = 3, cv: int = 3) -> List[str]:
        current = candidates[:]
        best_score = -np.inf
        best_set = current[:]

        for cycle in range(1, n_cycles + 1):
            if len(current) < 2:
                break

            model = self._base_model()
            scoring = "roc_auc" if self.task == "classification" and len(np.unique(y)) == 2 else "accuracy" if self.task == "classification" else "neg_mean_squared_error"
            try:
                scores = cross_val_score(model, X[current], y, cv=cv, scoring=scoring, n_jobs=-1)
                mean_score = float(np.mean(scores))
            except Exception:
                mean_score = -np.inf

            self._log_event("refinement_cycle", {
                "cycle": cycle,
                "n_features": len(current),
                "mean_cv_score": mean_score,
                "features": current[:]
            })

            if mean_score > best_score:
                best_score = mean_score
                best_set = current[:]

            if len(current) > 3:
                imp = self._score_features(X, y, current)
                lowest = min(imp, key=imp.get)
                current = [f for f in current if f != lowest]
                self._log_event("prune", {"removed": lowest, "remaining": len(current)})

        self.selected_features_ = best_set
        self.feature_scores_ = self._score_features(X, y, best_set)
        return best_set

    def fit_transform(self, X: pd.DataFrame, y: np.ndarray, n_cycles: int = 3) -> pd.DataFrame:
        candidates = self.generate_candidates(X, y)
        verified = self.refine(X, y, candidates, n_cycles=n_cycles)
        self._log_event("verified_set", {
            "n_features": len(verified),
            "features": verified,
            "scores": self.feature_scores_
        })
        return X[verified]

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        if not self.selected_features_:
            raise RuntimeError("Must call fit_transform first")
        return X[self.selected_features_]

    def _log_event(self, event_type: str, payload: Dict[str, Any]):
        entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "event": event_type,
            "payload": payload
        }
        self.log.append(entry)

    def get_provenance(self) -> List[Dict[str, Any]]:
        return self.log

    def save_log(self, path: str):
        with open(path, "w") as f:
            json.dump(self.log, f, indent=2)
