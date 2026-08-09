# Spiral Comparative Evaluation — Full Six-Dataset Results

**Date:** 2026-08-01 (campaign) · 2026-08-09 (residual continuity layer)  
**Repo:** `Spiral-comparative-eval` (formerly spiral-head-to-head)  
**Status:** All six priority datasets completed under the locked pre-registration. Residual continuity layer added.

## Design

- **Arm A**: Classical models on original features  
- **Arm B**: Same models after a transparent Spiral-inspired feature hypothesis loop  
- Fixed seeds, identical splits, full provenance logs  
- **Continuity layer (2026-08-09)**: Smurf Town residual / validity on the *process surface* (not task labels)

## Results Summary (task performance)

| Dataset              | Task          | Notable Outcome                                      | Verdict          |
|----------------------|---------------|------------------------------------------------------|------------------|
| Breast Cancer        | Classification| Identical high performance (~0.96 Acc, ~0.99 AUC)   | Neutral         |
| Adult                | Classification| Tiny RF edge for Spiral; others tied                 | Competitive     |
| Wine Quality         | Classification| Small HGB edge for Spiral on F1                      | Competitive     |
| Heart (Statlog)      | Classification| LogReg AUC slight gain; tree models mixed/slight loss| Mixed           |
| Credit Approval      | Classification| RF and HGB slight gains for Spiral                   | Competitive+    |
| Abalone              | Regression    | Essentially identical                                | Neutral         |

## Residual continuity (process surface)

Measured with Smurf Town residual (lower = better continuity). Handshake bar = **good**. Survey bar = **acceptable**.

| Subject / config | residual | band | valid (acceptable) |
|------------------|----------|------|--------------------|
| Campaign process (spiral-comparative-eval) | 0.166 | good | True |
| handshake_baseline | 0.119–0.141 | strong–good | True |
| mapping_openml_norms | ~0.256 | acceptable | True |
| mapping_stress_shift | ~0.635 | discontinuous | False |
| Multi-config mean | 0.282 | acceptable | — |
| handshake_valid (bar=good) | — | — | **True** |

**Interpretation (continuity):** The evaluation process itself remains continuous under the good handshake bar. Stress-shift configs fail validity as expected — differential holds. Continuity residual does **not** claim task superiority; it certifies that the harness stayed coherent while measuring.

Cross-check vs **qsc-stabilization**: QSC residual-*stability* (↑ better) strengthens the process field; Smurf residual (↓ better) gates discontinuity. Complementary metrics.

## Interpretation (task + continuity)

Under the current simple Spiral feature-refinement engine:
- No large, consistent **task** performance advantage appears across the six datasets.
- The method is competitive and occasionally produces small gains.
- Provenance logs are complete and inspectable.
- **Process continuity residual is continuous** (band good; handshake_valid under good bar).

Task claim remains **Under-test**. Process continuity for this campaign is **recorded continuous** under locked residual contracts.

---

*Reality is the only authority. Everything else is hypothesis.*  
*Comparative evaluation is the testing ground. Residual is the continuity ledger.*
