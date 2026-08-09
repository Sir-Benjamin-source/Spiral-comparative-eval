"""Standard scikit-learn estimators only. No Spiral imports."""
from __future__ import annotations
from typing import Any, Dict
from sklearn.ensemble import HistGradientBoostingClassifier, HistGradientBoostingRegressor, RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def get_classification_models(random_state: int = 42) -> Dict[str, Any]:
    return {
        "logreg": Pipeline([("scaler", StandardScaler()), ("clf", LogisticRegression(max_iter=1000, random_state=random_state))]),
        "rf": RandomForestClassifier(n_estimators=100, max_depth=8, random_state=random_state, n_jobs=-1),
        "hgb": HistGradientBoostingClassifier(max_depth=6, random_state=random_state),
    }

def get_regression_models(random_state: int = 42) -> Dict[str, Any]:
    return {
        "ridge": Pipeline([("scaler", StandardScaler()), ("reg", Ridge(random_state=random_state))]),
        "rf": RandomForestRegressor(n_estimators=100, max_depth=8, random_state=random_state, n_jobs=-1),
        "hgb": HistGradientBoostingRegressor(max_depth=6, random_state=random_state),
    }

def get_models(task: str, random_state: int = 42) -> Dict[str, Any]:
    if task == "classification":
        return get_classification_models(random_state)
    if task == "regression":
        return get_regression_models(random_state)
    raise ValueError(f"Unknown task: {task}")
