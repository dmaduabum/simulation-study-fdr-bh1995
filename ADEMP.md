# ADEMP: Simulation Design Document
**Project:** Reproducing Benjamini & Hochberg (1995) – False Discovery Rate Control  
**Author:** Dili K. Maduabum  
**Date:** October 21, 2025  

---

## Aims

The goal of this project is to reproduce the main findings from **Benjamini & Hochberg (1995)** on the False Discovery Rate (FDR) control procedure.

I want to see how well the **BH procedure** keeps the false discovery rate close to the chosen level (α), and how it compares to simpler approaches like Bonferroni correction and no correction at all.

Main questions:
- Does the BH method actually control FDR at or below α?  
- What happens to FDR and power when I change the number of tests or the proportion of true nulls?  
- How different is BH from Bonferroni in practice?

---

## Data-Generating Mechanism (DGP)

In this simulation, I generate p-values from a **normal means model** (matching the paper's Section 4.1).

Steps:
1. Pick the total number of tests m ∈ {16, 32, 64}.  
2. Choose what percent are true nulls: π₀ ∈ {0.75, 0.50, 0.25}.  
3. For each test:
   - If it's a **true null**: X ~ N(0, 1)  
   - If it's an **alternative**: X ~ N(μ, 1) where μ ∈ {0.5, 1.0, 1.5}  
4. Convert to two-sided z-test p-values.  
5. Repeat this whole process R = 1000 times to get stable results.

---

## Estimands / Targets

I want to estimate:
- **False Discovery Rate (FDR):** the average proportion of false positives among all rejections.  
- **Power:** the proportion of true alternatives that are correctly rejected.

These will show how well each method balances Type I and Type II errors.

---

## Methods

I will compare three multiple-testing methods:

1. **Benjamini–Hochberg (BH):** the main method from the paper.  
   - Sort p-values from smallest to largest.  
   - Find the largest k where p₍ₖ₎ ≤ (k/m) × α.  
   - Reject all p-values ≤ p₍ₖ₎.  

2. **Bonferroni correction:** divide α by m; reject if pᵢ ≤ α/m.  

3. **Uncorrected testing:** reject if pᵢ ≤ α (for comparison).

---

## Performance Measures

For each simulation and each method, I will record:
- Estimated **FDR** = (false rejections / total rejections)  
- Estimated **Power** = (true rejections / total true alternatives)  
- Average values and standard deviations across 1000 runs.

I'll make plots that show:
- FDR vs α for different π₀ values  
- Power vs π₀ for different α values

---

## Design Summary Table

| m  | π₀   | Effect Size | α    | Replicates |
|----|------|-------------|------|------------|
| 16 | 0.75 | 0.5, 1.0, 1.5 | 0.05 | 1000 |
| 32 | 0.50 | 0.5, 1.0, 1.5 | 0.05 | 1000 |
| 64 | 0.25 | 0.5, 1.0, 1.5 | 0.05 | 1000 |

---

## Reproducibility

- I'll set a random seed (42) so results can be repeated.  
- All raw results will be saved in `results/raw/` as CSV files.  
- Figures will be created automatically and stored in `results/figures/`.  
- The full pipeline can be run with `make all`.

---

## Notes

I expect:
- BH should control FDR close to or below α.  
- Bonferroni will be more conservative (lower FDR but also lower power).  
- Uncorrected tests will exceed α substantially.  

This design matches the paper's simulation setup (Section 4.1) using normal means 

