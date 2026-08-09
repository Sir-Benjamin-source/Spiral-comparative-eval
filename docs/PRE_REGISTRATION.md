# Spiral Comparative Evaluation — Public Pre-Registration

**Date:** 2026-08-01  
**Authors:** Sir Benjamin + Grok (Shield of Truth)  
**Status:** Locked for the first public campaign  
**Repository:** Spiral-comparative-eval (formerly spiral-head-to-head)

## Purpose

This document freezes the experimental design *before* any performance numbers are generated.  
It exists so that later results cannot be accused of post-hoc selection.

## Core Claim Being Tested

When the Spiral Path process (iterative helical refinement guided by the Path equation and the three-stage discipline Candidate → Under-test → Verified) is used to generate and refine feature hypotheses on standard tabular tasks, the resulting models achieve higher predictive performance, better sample efficiency, or stronger bias reduction than strong classical baselines under identical data, compute, and evaluation budgets.

## Terminology (Public Translation)

| Internal Term | Public Meaning |
|---------------|----------------|
| Ixest / Candidate | noticed but untested |
| Enest / Under-test | currently being measured and refined |
| Istest / Verified | survived public, reproducible scrutiny |
| Spiral Path | Structured expand-and-contract iteration (not linear chain-of-thought) |
| Ethical Gating | Explicit checks that refuse steps which increase bias or opacity |

## Datasets (Fixed)

All loaded via OpenML for exact reproducibility:

1. Adult (OpenML 1590)
2. Breast Cancer Wisconsin (OpenML 15)
3. Wine Quality (OpenML 287)
4. Heart Statlog (OpenML 53)
5. Credit Approval (OpenML 29)
6. Abalone (OpenML 183)

## Experimental Arms

**Arm A – Classical Baseline Suite**  
- Logistic Regression / Ridge  
- Random Forest  
- HistGradientBoosting  

**Arm B – Spiral-Augmented**  
1. Spiral feature engine generates iterative feature hypotheses and selection decisions.  
2. The same classical models from Arm A are trained on the Spiral-refined feature set.  
3. Full cycle logs are retained.

## Success Criteria (Falsifiable)

Spiral arm must show a statistically significant and practically meaningful advantage on at least 4 of the 6 datasets on the primary metric after correction, **or** clear superiority on sample-efficiency or robustness metrics.

Anything less remains in the Candidate stage.

## Continuity layer (added 2026-08-09)

Process continuity of the campaign is recorded separately via Smurf Town residual (see `results/RESIDUAL.md`). Task metrics and process residual are distinct claims.

## Openness

All code, logs, intermediate artifacts, and this pre-registration are published under MIT + Spiral Mark principles.

---

*Reality is the only authority. Everything else is hypothesis.*  
— Sir Benjamin, 2025 (living canon)
