"""Honest comparative harness v2 — Arm A pure classical; Arm B SpiralMethod residual-owned."""
from __future__ import annotations
import json, os
from datetime import datetime, timezone
from typing import Any, Dict
import numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier, HistGradientBoostingRegressor, RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.metrics import accuracy_score, f1_score, mean_squared_error, r2_score, roc_auc_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from data_loader import DATASET_REGISTRY, load_openml_dataset
from spiral_method import SpiralMethod

def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def get_baselines(task: str):
    if task == "classification":
        return {
            "logreg": Pipeline([("scaler", StandardScaler()), ("clf", LogisticRegression(max_iter=1000, random_state=42))]),
            "rf": RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42, n_jobs=-1),
            "hgb": HistGradientBoostingClassifier(max_depth=6, random_state=42),
        }
    return {
        "ridge": Pipeline([("scaler", StandardScaler()), ("reg", Ridge(random_state=42))]),
        "rf": RandomForestRegressor(n_estimators=100, max_depth=8, random_state=42, n_jobs=-1),
        "hgb": HistGradientBoostingRegressor(max_depth=6, random_state=42),
    }

def evaluate_model(model, X_train, y_train, X_test, y_test, task: str):
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    metrics = {}
    if task == "classification":
        metrics["accuracy"] = float(accuracy_score(y_test, preds))
        metrics["f1_macro"] = float(f1_score(y_test, preds, average="macro", zero_division=0))
        if len(np.unique(y_train)) == 2:
            try:
                proba = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else model.decision_function(X_test)
                metrics["roc_auc"] = float(roc_auc_score(y_test, proba))
            except Exception:
                metrics["roc_auc"] = float("nan")
    else:
        metrics["rmse"] = float(np.sqrt(mean_squared_error(y_test, preds)))
        metrics["r2"] = float(r2_score(y_test, preds))
    return metrics

def run_single_dataset(name: str, random_state: int = 42):
    print(f"\n===== v2 Dataset: {name} =====")
    data = load_openml_dataset(name, random_state=random_state)
    task = data["task"]
    X_train, X_test = data["X_train"], data["X_test"]
    y_train, y_test = data["y_train"], data["y_test"]
    y_train_np = np.asarray(y_train)
    results = {"dataset": name, "protocol": "v2_honest_comparative", "task": task, "timestamp": _now(),
               "arm_A_classical_pure": {}, "arm_B_spiral_method": {}, "spiral_process": {}}
    baselines = get_baselines(task)
    print("  Arm A (pure classical) ...")
    for model_name, model in baselines.items():
        metrics = evaluate_model(model, X_train, y_train, X_test, y_test, task)
        results["arm_A_classical_pure"][model_name] = metrics
        print(f"    {model_name}: {metrics}")
    print("  Arm B (SpiralMethod residual-owned) ...")
    spiral = SpiralMethod(task=task, random_state=random_state, n_cycles=5)
    spiral_result = spiral.fit(X_train, y_train_np)
    X_tr_s, X_te_s = spiral.transform(X_train), spiral.transform(X_test)
    results["spiral_process"] = {
        "final_residual": spiral_result.final_residual, "final_band": spiral_result.final_band,
        "handshake_continuous": spiral_result.handshake_continuous,
        "n_verified_features": len(spiral_result.verified_features),
        "n_cycles": len(spiral_result.cycles),
        "cycle_residuals": [c.residual for c in spiral_result.cycles],
        "cycle_stages": [c.stage for c in spiral_result.cycles],
        "provenance": spiral_result.provenance,
    }
    for model_name, model in baselines.items():
        metrics = evaluate_model(model, X_tr_s, y_train, X_te_s, y_test, task)
        results["arm_B_spiral_method"][model_name] = metrics
        print(f"    {model_name}: {metrics}")
    return results

def main():
    print("Spiral Comparative Evaluation — PROTOCOL v2 (honest)")
    all_results = []
    for name in DATASET_REGISTRY:
        try:
            all_results.append(run_single_dataset(name))
        except Exception as e:
            print(f"  FAILED {name}: {e}")
            all_results.append({"dataset": name, "error": str(e), "protocol": "v2_honest_comparative"})
    out_dir = os.path.join(os.path.dirname(__file__), "..", "results")
    os.makedirs(out_dir, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = os.path.join(out_dir, f"campaign_v2_{stamp}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nCampaign v2 JSON → {out_path}")
    wins = 0
    for r in all_results:
        if "error" in r: continue
        a, b = r["arm_A_classical_pure"].get("rf", {}), r["arm_B_spiral_method"].get("rf", {})
        key = "accuracy" if r["task"] == "classification" else "r2"
        av, bv = a.get(key), b.get(key)
        if av is not None and bv is not None and (bv - av) > 0.005: wins += 1
        print(f"{r['dataset']:15} A={av} B={bv}")
    print(f"Spiral RF wins (Δ>0.005): {wins}/6")
    return all_results

if __name__ == "__main__":
    main()
