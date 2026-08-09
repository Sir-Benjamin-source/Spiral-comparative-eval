"""Standard sklearn metrics only."""
from __future__ import annotations
from typing import Any, Dict
import numpy as np
from sklearn.metrics import accuracy_score, f1_score, mean_squared_error, r2_score, roc_auc_score

def classification_metrics(y_true, y_pred, y_score=None) -> Dict[str, float]:
    out = {"accuracy": float(accuracy_score(y_true, y_pred)), "f1_macro": float(f1_score(y_true, y_pred, average="macro", zero_division=0))}
    if y_score is not None and len(np.unique(y_true)) == 2:
        try:
            out["roc_auc"] = float(roc_auc_score(y_true, y_score))
        except Exception:
            out["roc_auc"] = float("nan")
    return out

def regression_metrics(y_true, y_pred) -> Dict[str, float]:
    return {"rmse": float(np.sqrt(mean_squared_error(y_true, y_pred))), "r2": float(r2_score(y_true, y_pred))}

def score_model(model: Any, X_test, y_test, task: str) -> Dict[str, float]:
    preds = model.predict(X_test)
    if task == "classification":
        y_score = None
        if len(np.unique(y_test)) == 2:
            try:
                if hasattr(model, "predict_proba"):
                    y_score = model.predict_proba(X_test)[:, 1]
                elif hasattr(model, "decision_function"):
                    y_score = model.decision_function(X_test)
            except Exception:
                y_score = None
        return classification_metrics(y_test, preds, y_score)
    return regression_metrics(y_test, preds)
