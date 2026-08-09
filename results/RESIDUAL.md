# Residual Continuity Packet — Spiral Comparative Evaluation

**Date:** 2026-08-09  
**Subject:** Spiral-comparative-eval campaign process surface  
**Source:** Smurf Town examination cycle (`The-Spiral-Codex/station-identification/smurf-town`)  
**Cycle id:** exam-20260809T163301Z  
**Constraint:** Residual-only. No host content. Does not claim task superiority.

---

## Sense (population residual)

| Metric | Value |
|--------|--------|
| mean residual | **0.156** |
| band | **good** |
| all continuous | True |
| meets_good | True |
| meets_strong | False |

## Differentiate (multi-config)

| config | residual | strength | valid (survey=acceptable) |
|--------|----------|----------|---------------------------|
| handshake_baseline | 0.1335 | good | True |
| handshake_spiral_feat | 0.155 | good | True |
| mapping_openml_norms | 0.232 | acceptable | True |
| mapping_stress_shift | 0.6065 | invalid | False |

| Aggregate | Value |
|-----------|--------|
| mean residual | **0.282** |
| overall band | **acceptable** |
| handshake_valid (survey) | True |
| **handshake_valid (bar=good)** | **True** |
| any discontinuous | True (stress_shift only) |

## Express (merge-ready)

```yaml
# float.current_designations (append)
- target: "smurf-town residual continuity"
  designation: "residual band=good (mean=0.156); handshake_valid=True (bar=good)"
  since: "2026-08-09T16:33:01Z"

# fsheet.coherence_notes (append)
- timestamp: "2026-08-09T16:33:01Z"
  note: "comparative-eval process continuity: mean residual=0.156 band=good; multi-config mean=0.282 acceptable; handshake_valid under good bar; mapping_stress_shift residual=0.6065 invalid. Residual-only."
```

## Relation to task SUMMARY

Task Acc/AUC/F1 remain in `SUMMARY.md`. This packet certifies **process continuity** of the evaluation campaign itself. Stress-shift failure is the expected differential, not a campaign failure.

## Division of labor

| Surface | Question |
|---------|----------|
| This residual packet | Is the campaign process continuous? |
| SUMMARY task table | Do Spiral features beat classical baselines? |
| qsc-stabilization | Is readiness residual-stability high? |

---

*Reality is the only authority. Everything else is hypothesis.*  
*Residual is the continuity ledger.*
