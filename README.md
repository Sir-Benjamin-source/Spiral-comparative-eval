# Spiral Comparative Evaluation

**Target repository name:** `spiral-comparative-eval`  
*(GitHub Settings rename pending; this README reflects the professional name.)*

**Public testing ground.** Classical scikit-learn baselines vs Spiral-inspired feature refinement on standard UCI / OpenML tabular tasks. Full provenance, pre-registration, reproducible harness.

## Role in the ecosystem

- **This repository** is the competition / comparative surface. Claims of improvement against classical methods are tested here under pre-registered protocol.
- **qsc-stabilization** (DOI [10.5281/zenodo.21750846](https://doi.org/10.5281/zenodo.21750846)) supplies the continuous stabilizer (readiness field, residual-stability control, TCRF). Transfer of those process ideas into tabular feature logic must be explicit, logged, and re-tested in this harness.
- **smurf-town** (in The-Spiral-Codex / station-identification) supplies residual continuity / validity examination of process surfaces. Comparative eval remains the performance harness; Smurf Town measures continuity residual of the *process*, not task accuracy.
- Ethical gates remain active before any public claim of superiority.

## Status

- Pre-registration locked (2026-08-01 campaign).
- Six priority datasets executed; competitive / neutral — **Under-test**.
- Rename to `spiral-comparative-eval` adopted 2026-08-09.

See `results/SUMMARY.md` and `docs/PRE_REGISTRATION.md`.

## Public Terminology

- **Candidate (Ixest)** = noticed but untested
- **Under-test (Enest)** = currently being measured
- **Verified (Istest)** = survived public, reproducible scrutiny

## How to Re-run

```bash
cd src
python evaluate.py          # full priority campaign
```

## Principle

> Reality is the only authority. Everything else is hypothesis.  
> Comparative evaluation is the testing ground. We are the test.
