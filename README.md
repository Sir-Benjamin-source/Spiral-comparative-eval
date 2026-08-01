# Spiral Path Public Head-to-Head Campaign

**First concrete, auditable comparison of Spiral-inspired feature refinement against classical scikit-learn baselines on standard UCI / OpenML tabular tasks.**

## Status (2026-08-01)

- Pre-registration locked.  
- All six priority datasets executed.  
- Full provenance logs generated.  
- Results are competitive; no large claimed gains are asserted yet.

See `results/SUMMARY.md` and `docs/PRE_REGISTRATION.md`.

## Public Terminology

We translate our internal language as follows:

- **Candidate (Ixest)** = noticed but untested  
- **Under-test (Enest)** = currently being measured  
- **Verified (Istest)** = survived public, reproducible scrutiny  

These distinctions exist so that promising internal observations are not treated as settled science.

## How to Re-run

```bash
cd src
python evaluate.py          # full priority campaign
# or
python -c "from evaluate import run_single_dataset; run_single_dataset('adult')"
```

## Repository Intent

This folder is intentionally designed to be published.  
When the parent Spiral repositories are made publicly discoverable again, this campaign can sit alongside them as the living empirical test.

## Principle

> Reality is the only authority. Everything else is hypothesis.  
> — Sir Benjamin
