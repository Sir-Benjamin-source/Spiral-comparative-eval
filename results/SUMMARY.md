# Spiral Comparative Evaluation — Full Six-Dataset Results

**Date:** 2026-08-01 (original campaign) · **2026-08-09 (re-run under new title + residual layer)**  
**Repo:** `Spiral-comparative-eval` (formerly spiral-head-to-head)  
**Status:** All six priority datasets completed under the locked pre-registration. Re-run 2026-08-09 confirms competitive/neutral profile. Residual continuity layer active.

## Design

- **Arm A**: Classical models on original features  
- **Arm B**: Same models after a transparent Spiral-inspired feature hypothesis loop  
- Fixed seeds, identical splits, full provenance logs  
- **Continuity layer**: Smurf Town residual / validity on the *process surface* (not task labels) — see `results/RESIDUAL.md`

## Results Summary (task performance)

| Dataset              | Task          | Notable Outcome                                      | Verdict          |
|----------------------|---------------|------------------------------------------------------|------------------|
| Breast Cancer        | Classification| Identical high performance (~0.96 Acc, ~0.99 AUC)   | Neutral         |
| Adult                | Classification| Tiny RF edge for Spiral; others tied                 | Competitive     |
| Wine Quality         | Classification| Small HGB edge for Spiral on F1                      | Competitive     |
| Heart (Statlog)      | Classification| LogReg AUC slight gain; tree models mixed/slight loss| Mixed           |
| Credit Approval      | Classification| RF and HGB slight gains for Spiral                   | Competitive+    |
| Abalone              | Regression    | Essentially identical                                | Neutral         |

### Re-run snapshot (2026-08-09, RF primary metric)

| Dataset | Arm A RF | Arm B RF |
|---------|----------|----------|
| adult | Acc 0.853 | Acc 0.854 |
| breast_cancer | Acc 0.964 | Acc 0.964 |
| wine_quality | Acc 0.612 | Acc 0.606 |
| heart | Acc 0.833 | Acc 0.815 |
| credit | Acc 0.824 | Acc 0.840 |
| abalone | R² 0.541 | R² 0.541 |

Campaign JSON: `results/campaign_20260809T163548Z.json` (local re-run artifact).

## Residual continuity (process surface)

Measured with Smurf Town residual (lower = better continuity). Handshake bar = **good**. Survey bar = **acceptable**.

| Subject / config | residual | band | valid |
|------------------|----------|------|-------|
| Campaign process | 0.156 | good | True |
| handshake_baseline | 0.134 | good | True |
| handshake_spiral_feat | 0.155 | good | True |
| mapping_openml_norms | 0.232 | acceptable | True |
| mapping_stress_shift | 0.607 | discontinuous | False |
| Multi-config mean | 0.282 | acceptable | — |
| handshake_valid (bar=good) | — | — | **True** |

Full packet: `results/RESIDUAL.md`.

**Interpretation (continuity):** The evaluation process remains continuous under the good handshake bar. Stress-shift fails validity as expected. Continuity residual does **not** claim task superiority.

## Interpretation (task + continuity)

- No large, consistent **task** performance advantage across the six datasets.
- Competitive; occasional small gains (credit RF/HGB); occasional small losses (heart trees, wine RF).
- Provenance logs complete under `logs/`.
- **Process continuity residual continuous** (band good; handshake_valid under good bar).

Task claim remains **Under-test**. Process continuity for this campaign is **recorded continuous**.

---

*Reality is the only authority. Everything else is hypothesis.*  
*Comparative evaluation is the testing ground. Residual is the continuity ledger.*
