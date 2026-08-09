"""OpenML dataset loading — standard open-source practice. No Spiral metadata."""
from __future__ import annotations
from typing import Any, Dict
import numpy as np
import openml
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

DATASET_REGISTRY: Dict[str, Dict[str, Any]] = {
    "adult": {"openml_id": 1590, "task": "classification"},
    "breast_cancer": {"openml_id": 15, "task": "classification"},
    "wine_quality": {"openml_id": 287, "task": "classification"},
    "heart": {"openml_id": 53, "task": "classification"},
    "credit": {"openml_id": 29, "task": "classification"},
    "abalone": {"openml_id": 183, "task": "regression"},
}

def load_dataset(name: str, test_size: float = 0.2, random_state: int = 42) -> Dict[str, Any]:
    if name not in DATASET_REGISTRY:
        raise ValueError(f"Unknown dataset {name}")
    cfg = DATASET_REGISTRY[name]
    dataset = openml.datasets.get_dataset(cfg["openml_id"])
    X, y, categorical_indicator, attribute_names = dataset.get_data(
        target=dataset.default_target_attribute, dataset_format="dataframe"
    )
    X, y = X.copy(), y.copy()
    mask = ~X.isnull().any(axis=1)
    if hasattr(y, "isnull"):
        mask = mask & ~y.isnull()
    X, y = X.loc[mask].reset_index(drop=True), y.loc[mask].reset_index(drop=True)
    for col in X.columns:
        if X[col].dtype == object or str(X[col].dtype).startswith("category"):
            X[col] = LabelEncoder().fit_transform(X[col].astype(str))
        else:
            X[col] = pd.to_numeric(X[col], errors="coerce")
    X = X.fillna(X.median(numeric_only=True))
    if y.dtype == object or str(y.dtype).startswith("category"):
        y = LabelEncoder().fit_transform(y.astype(str))
    else:
        y = np.asarray(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return {"name": name, "task": cfg["task"], "openml_id": cfg["openml_id"], "X_train": X_train, "X_test": X_test,
            "y_train": y_train, "y_test": y_test, "n_features": X_train.shape[1], "n_train": len(X_train), "n_test": len(X_test)}
