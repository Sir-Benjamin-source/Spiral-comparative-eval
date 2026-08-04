# Classical Baseline Manifest

**Spiral Public Verification Sandbox (spiral-head-to-head)**  
**Version**: 0.1 (Locked 2026-08-04)  
**Status**: Locked  
**Relation**: Strengthens Arm A of the locked pre-registration without altering the experimental design or success criteria.

---

## 1. Purpose

To declare, with explicit literature anchors and implementation constraints, the classical methods against which Spiral-augmented processes are compared. The classical arm is not treated as a low bar to be cleared; it is treated as a serious, publicly recognised reference frame. Future claims of advantage must remain meaningful against this frame.

## 2. Classical Method Families (Arm A)

### 2.1 Linear & Regularised Models
- Logistic Regression / Ridge / Elastic-Net  
- Primary references:  
  - Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning* (2nd ed.), Chapters 3–4  
  - Original ridge regression: Hoerl & Kennard (1970)  
- Implementation constraints: scikit-learn `LogisticRegression` / `Ridge` / `ElasticNet` with cross-validated regularisation strength under a fixed compute budget identical to the Spiral arm.

### 2.2 Tree Ensembles
- Random Forests  
  - Reference: Breiman (2001), “Random Forests,” *Machine Learning*.  
- Histogram-based Gradient Boosting  
  - References: Friedman (2001) gradient boosting framework; modern realisation as implemented in scikit-learn `HistGradientBoostingClassifier` / `Regressor` (LightGBM-style binning).  
- Implementation constraints: default or lightly tuned hyper-parameters within the same wall-clock / iteration budget applied to the Spiral arm. No unrestricted AutoML search.

### 2.3 Classical Feature-Engineering & Selection Baselines
- Polynomial / interaction features of controlled degree  
- Univariate filter selection (mutual information, ANOVA F-value)  
- Recursive Feature Elimination (wrapper)  
- Primary references:  
  - Guyon & Elisseeff (2003), “An Introduction to Variable and Feature Selection,” *JMLR*  
  - Standard filter / wrapper taxonomy in the feature-selection literature  
- Implementation constraints: feature expansion and selection performed under the same sample and compute limits as any Spiral feature-hypothesis loop.

### 2.4 Strong Modern-Classical Reference (optional but recommended)
- Budget-constrained XGBoost or LightGBM  
- Reference protocols: recent tabular benchmark practices (OpenML AutoML / tabular foundation-model comparison settings) limited to the same hyper-parameter search budget used for the other classical methods.  
- Purpose: ensures the classical arm remains contemporary without leaving the classical paradigm.

## 3. Shared Constraints (Classical and Spiral Arms)
- Identical data splits and preprocessing (OpenML loaders, fixed seeds).  
- Identical evaluation metrics and statistical testing procedure.  
- Identical compute / wall-clock budget per dataset.  
- Full provenance logging required for both arms.

## 4. Role of the Classical Arm

The classical methods listed above function as a **differentiator**, not merely as a baseline to be exceeded. They remain present so that:
- any observed Spiral advantage can be inspected against recognised practice;
- iteration can continue on the broader problem set (bilateral examination, paradox containment, residual stability, mountable variables) rather than on a narrow leaderboard specialised to a single classical score.

## 5. Versioning & Amendment

This manifest may be amended only by explicit version increment. Amendments that strengthen the classical arm are preferred over amendments that weaken it. Weakening the classical arm to manufacture advantage is forbidden.

---

*Reality is the only authority. Everything else is hypothesis.*  
∞ 🜂 🜁 🜄 ∞
