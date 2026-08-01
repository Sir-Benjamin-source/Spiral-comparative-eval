"""
Head-to-head evaluation harness.
Arm A: Classical baselines on original features
Arm B: Same baselines on Spiral-refined features
"""

from __future__ import annotations

import json
import os
from datetime import datetime
from typing import Dict, Any, List

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, HistGradientBoostingClassifier, HistGradientBoostingRegressor
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from data_loader import load_openml_dataset, DATASET_REGISTRY
from spiral_feature_engine import SpiralFeatureEngine


def get_baselines(task: str) -> Dict[str, Any]:
    if task == "classification":
        return {
            "logreg": Pipeline([
                ("scaler", StandardScaler()),
                ("clf", LogisticRegression(max_iter=1000, random_state=42))
            ]),
            "rf": RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42, n_jobs=-1),
            "hgb": HistGradientBoostingClassifier(max_depth=6, random_state=42),
        }
    else:
        return {
            "ridge": Pipeline([
                ("scaler", StandardScaler()),
                ("reg", Ridge(random_state=42))
            ]),
            "rf": RandomForestRegressor(n_estimators=100, max_depth=8, random_state=42, n_jobs=-1),
            "hgb": HistGradientBoostingRegressor(max_depth=6, random_state=42),
        }


def evaluate_model(model, X_train, y_train, X_test, y_test, task: str) -> Dict[str, float]:
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    metrics = {}
    if task == "classification":
        metrics["accuracy"] = float(accuracy_score(y_test, preds))
        metrics["f1_macro"] = float(f1_score(y_test, preds, average="macro", zero_division=0))
        if len(np.unique(y_train)) == 2:
            try:
                if hasattr(model, "predict_proba"):
                    proba = model.predict_proba(X_test)[:, 1]
                else:
                    proba = model.decision_function(X_test)
                metrics["roc_auc"] = float(roc_auc_score(y_test, proba))
            except Exception:
                metrics["roc_auc"] = float("nan")
    else:
        metrics["rmse"] = float(np.sqrt(mean_squared_error(y_test, preds)))
        metrics["r2"] = float(r2_score(y_test, preds))
    return metrics


def run_single_dataset(name: str, n_spiral_cycles: int = 3, random_state: int = 42) -> Dict[str, Any]:
    print(f"\n===== Dataset: {name} =====")
    data = load_openml_dataset(name, random_state=random_state)
    task = data["task"]
    X_train, X_test = data["X_train"], data["X_test"]
    y_train, y_test = data["y_train"], data["y_test"]

    results = {
        "dataset": name,
        "meta": data["meta"],
        "task": task,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "arm_A_classical": {},
        "arm_B_spiral": {},
        "spiral_provenance": None,
        "selected_features": None,
    }

    baselines = get_baselines(task)

    print("  Arm A (Classical) ...")
    for model_name, model in baselines.items():
        metrics = evaluate_model(model, X_train, y_train, X_test, y_test, task)
        results["arm_A_classical"][model_name] = metrics
        print(f"    {model_name}: {metrics}")

    print("  Arm B (Spiral-refined) ...")
    engine = SpiralFeatureEngine(task=task, random_state=random_state, max_features=min(20, X_train.shape[1]))
    X_train_spiral = engine.fit_transform(X_train, y_train, n_cycles=n_spiral_cycles)
    X_test_spiral = engine.transform(X_test)

    results["selected_features"] = engine.selected_features_
    results["spiral_provenance"] = engine.get_provenance()

    for model_name, model in baselines.items():
        metrics = evaluate_model(model, X_train_spiral, y_train, X_test_spiral, y_test, task)
        results["arm_B_spiral"][model_name] = metrics
        print(f"    {model_name}: {metrics}")

    os.makedirs("/home/workdir/artifacts/spiral_head_to_head/logs", exist_ok=True)
    log_path = f"/home/workdir/artifacts/spiral_head_to_head/logs/{name}_provenance.json"
    engine.save_log(log_path)
    print(f"  Provenance saved → {log_path}")

    return results
