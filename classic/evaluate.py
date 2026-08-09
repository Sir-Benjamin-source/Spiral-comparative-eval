"""Pure classical evaluation. spiral_informed=False."""
from __future__ import annotations
import json, os
from datetime import datetime, timezone
from typing import Any, Dict, List
from datasets import DATASET_REGISTRY, load_dataset
from metrics import score_model
from models import get_models

def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def run_dataset(name: str, random_state: int = 42) -> Dict[str, Any]:
    print(f"\n===== classic: {name} =====")
    data = load_dataset(name, random_state=random_state)
    task = data["task"]
    models = get_models(task, random_state=random_state)
    results = {"dataset": name, "openml_id": data["openml_id"], "task": task, "n_features": data["n_features"],
               "n_train": data["n_train"], "n_test": data["n_test"], "timestamp": _now(),
               "package": "classic", "spiral_informed": False, "models": {}}
    for model_name, model in models.items():
        model.fit(data["X_train"], data["y_train"])
        metrics = score_model(model, data["X_test"], data["y_test"], task)
        results["models"][model_name] = metrics
        print(f"  {model_name}: {metrics}")
    return results

def main() -> List[Dict[str, Any]]:
    print("classic — pure scikit-learn / OpenML baseline\nspiral_informed: False")
    all_results = []
    for name in DATASET_REGISTRY:
        try:
            all_results.append(run_dataset(name))
        except Exception as e:
            print(f"  FAILED {name}: {e}")
            all_results.append({"dataset": name, "error": str(e), "package": "classic", "spiral_informed": False})
    out_dir = os.path.join(os.path.dirname(__file__), "..", "results")
    os.makedirs(out_dir, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = os.path.join(out_dir, f"classic_baseline_{stamp}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nWrote {out_path}")
    for r in all_results:
        if "error" in r: continue
        rf = r["models"].get("rf", {})
        key = "accuracy" if r["task"] == "classification" else "r2"
        print(f"{r['dataset']:15} rf_{key}={rf.get(key)}")
    return all_results

if __name__ == "__main__":
    main()
