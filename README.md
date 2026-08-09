# Spiral Comparative Evaluation

**Repository:** `Spiral-comparative-eval`  
**Public testing ground.** Classical scikit-learn baselines vs Spiral-inspired feature refinement on standard UCI / OpenML tabular tasks. Full provenance, pre-registration, reproducible harness. Residual continuity of the *process* is recorded beside task metrics.

## Role in the ecosystem

| Surface | Question it answers |
|---------|---------------------|
| **This repo** | Does Spiral feature refinement beat classical baselines on task metrics? |
| **qsc-stabilization** | Is the continuous process / readiness field stable? (↑ residual-stability) |
| **smurf-town** (Codex / station-identification) | Is the process continuous under S/G/C residual? (↓ residual, validity bars) |

Task performance and process continuity are separate claims. Both must be recorded. Neither substitutes for the other.

Ethical gates remain active before any public claim of superiority.

## Status

- Pre-registration locked (2026-08-01 campaign).
- Six priority datasets executed; competitive / neutral — task claim **Under-test**.
- Residual continuity layer added 2026-08-09 — process surface **continuous** (band good; handshake_valid under good bar).
- Renamed from spiral-head-to-head → Spiral-comparative-eval (2026-08-09).

See `results/SUMMARY.md` (task + residual) and `docs/PRE_REGISTRATION.md`.

## Public Terminology

- **Candidate (Ixest)** = noticed but untested
- **Under-test (Enest)** = currently being measured
- **Verified (Istest)** = survived public, reproducible scrutiny

## How to Re-run

```bash
cd src
python evaluate.py          # full priority campaign
```

Residual continuity re-check (from Spiral Codex smurf-town):

```bash
# after smurf-town is on PYTHONPATH
python -c "from core.validity import assess_validity; print(assess_validity(0.87, 0.81, 0.79))"
```

## Principle

> Reality is the only authority. Everything else is hypothesis.  
> Comparative evaluation is the testing ground. Residual is the continuity ledger. We are the test.
