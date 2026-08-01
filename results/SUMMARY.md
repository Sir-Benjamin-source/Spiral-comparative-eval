# Spiral Head-to-Head Campaign — Full Six-Dataset Results

**Date:** 2026-08-01  
**Status:** All six priority datasets completed under the locked pre-registration.

## Design

- **Arm A**: Classical models on original features  
- **Arm B**: Same models after a transparent Spiral-inspired feature hypothesis loop  
- Fixed seeds, identical splits, full provenance logs  

## Results Summary

| Dataset              | Task          | Notable Outcome                                      | Verdict          |
|----------------------|---------------|------------------------------------------------------|------------------|
| Breast Cancer        | Classification| Identical high performance (~0.96 Acc, ~0.99 AUC)   | Neutral         |
| Adult                | Classification| Tiny RF edge for Spiral; others tied                 | Competitive     |
| Wine Quality         | Classification| Small HGB edge for Spiral on F1                      | Competitive     |
| Heart (Statlog)      | Classification| LogReg AUC slight gain; tree models mixed/slight loss| Mixed           |
| Credit Approval      | Classification| RF and HGB slight gains for Spiral                   | Competitive+    |
| Abalone              | Regression    | Essentially identical                                | Neutral         |

## Interpretation

Under the current simple Spiral feature-refinement engine:
- No large, consistent performance advantage appears across the six datasets.
- The method is competitive and occasionally produces small gains.
- The provenance logs are complete and inspectable.

This places the concrete tabular claim firmly in the **Under-test** stage.

---

*Reality is the only authority. Everything else is hypothesis.*
