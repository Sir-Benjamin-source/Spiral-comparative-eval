"""
Data loading utilities for the Spiral head-to-head campaign.
All datasets are fetched from OpenML for exact public reproducibility.
"""

from __future__ import annotations

import openml
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from typing import Dict, Tuple, Any


# Fixed dataset registry for the campaign
DATASET_REGISTRY = {
    "adult": {
        "openml_id": 1590,
        "task": "classification",
        "target": "class",
        "sensitive": ["sex"],
        "description": "Adult income prediction (fairness benchmark)"
    },
    "breast_cancer": {
        "openml_id": 15,
        "task": "classification",
        "target": "Class",
        "sensitive": None,
        "description": "Breast Cancer Wisconsin (Diagnostic)"
    },
    "wine_quality": {
        "openml_id": 287,
        "task": "classification",
        "target": "quality",
        "sensitive": None,
        "description": "Wine Quality (red+white combined variant)"
    },
    "heart": {
        "openml_id": 53,
        "task": "classification",
        "target": "class",
        "sensitive": None,
        "description": "Heart Disease (Statlog)"
    },
    "credit": {
        "openml_id": 29,
        "task": "classification",
        "target": "class",
        "sensitive": None,
        "description": "Credit Approval"
    },
    "abalone": {
        "openml_id": 183,
        "task": "regression",
        "target": "Class_number_of_rings",
        "sensitive": None,
        "description": "Abalone age prediction"
    },
}


def load_openml_dataset(name: str, test_size: float = 0.2, random_state: int = 42) -> Dict[str, Any]:
    if name not in DATASET_REGISTRY:
        raise ValueError(f"Unknown dataset '{name}'. Choose from {list(DATASET_REGISTRY.keys())}")

    cfg = DATASET_REGISTRY[name]
    print(f"Loading {name} (OpenML {cfg['openml_id']}) ...")

    dataset = openml.datasets.get_dataset(cfg["openml_id"])
    X, y, categorical_indicator, attribute_names = dataset.get_data(
        target=dataset.default_target_attribute, dataset_format="dataframe"
    )

    X = X.copy()
    y = y.copy()

    mask = ~X.isnull().any(axis=1)
    if hasattr(y, "isnull"):
        mask = mask & ~y.isnull()
    X = X.loc[mask].reset_index(drop=True)
    y = y.loc[mask].reset_index(drop=True) if hasattr(y, "loc") else y[mask]

    cat_cols = [col for col, is_cat in zip(X.columns, categorical_indicator) if is_cat]
    for col in cat_cols:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))

    if cfg["task"] == "classification":
        if y.dtype == object or str(y.dtype).startswith("category"):
            le_y = LabelEncoder()
            y = le_y.fit_transform(y.astype(str))
        else:
            y = y.astype(int).values if hasattr(y, "values") else np.asarray(y, dtype=int)
    else:
        y = y.astype(float).values if hasattr(y, "values") else np.asarray(y, dtype=float)

    stratify = y if cfg["task"] == "classification" and len(np.unique(y)) > 1 else None
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=stratify
    )

    sensitive = cfg.get("sensitive")

    return {
        "name": name,
        "X_train": X_train.reset_index(drop=True),
        "X_test": X_test.reset_index(drop=True),
        "y_train": np.asarray(y_train),
        "y_test": np.asarray(y_test),
        "feature_names": list(X.columns),
        "task": cfg["task"],
        "sensitive_cols": sensitive,
        "meta": {
            "openml_id": cfg["openml_id"],
            "description": cfg["description"],
            "n_samples": len(X),
            "n_features": X.shape[1],
            "n_train": len(X_train),
            "n_test": len(X_test),
        }
    }
