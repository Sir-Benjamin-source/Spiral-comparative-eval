# Spiral Path Public Head-to-Head Campaign

**Public testing ground.** Classical scikit-learn baselines vs Spiral-inspired feature refinement on standard UCI / OpenML tabular tasks. Full provenance, pre-registration, reproducible harness.

## Role in the ecosystem

- **This repository** is the competition surface. Claims of improvement against classical methods are tested here under pre-registered protocol.
- **qsc-stabilization** (DOI [10.5281/zenodo.21750846](https://doi.org/10.5281/zenodo.21750846)) supplies the continuous stabilizer (readiness field, residual-stability control, TCRF, Poetry/SRM association). Transfer of those process ideas into tabular feature logic must be explicit, logged, and re-tested in this harness.
- Ethical gates (Generosity / E-shield style floors, harm-horizon) remain active before any public claim of superiority.

## Status (2026-08-01)

- Pre-registration locked.
- All six priority datasets executed.
- Full provenance logs generated.
- Results are competitive; no large claimed gains are asserted yet.

See `results/SUMMARY.md` and `docs/PRE_REGISTRATION.md`.

## Public Terminology

- **Candidate (Ixest)** = noticed but untested
- **Under-test (Enest)** = currently being measured
- **Verified (Istest)** = survived public, reproducible scrutiny

These distinctions exist so that promising internal observations are not treated as settled science.

## How to Re-run

```bash
cd src
python evaluate.py          # full priority campaign
```

## Principle

> Reality is the only authority. Everything else is hypothesis.  
> Head-to-head is the testing ground. We are the test.
