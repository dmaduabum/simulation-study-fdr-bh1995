# ADEMP: Simulation Design Document
**Project:** Reproducing Benjamini & Hochberg (1995) – False Discovery Rate (FDR)  
**Author:** Dili K. Maduabum  
**Date:** October 21, 2025  

---

## Aims
The goal of this project is to reproduce the main idea from the paper **Benjamini & Hochberg (1995)** — the False Discovery Rate (FDR) method.  

I want to see how well the **BH procedure** keeps the false discovery rate close to the chosen level ($\alpha$), and how it compares to simpler approaches like Bonferroni correction and no correction at all.

Main questions:
- Does the BH method actually control FDR at or below $\alpha$?  
- What happens to FDR and power when I change the number of tests or the amount of “true effects”?  
- How different is BH from Bonferroni in practice?

---

## Data-Generating Mechanism (DGP)
In this simulation, I will create many sets of *p-values* that represent results from hypothesis tests.  
Some of these tests will be “true nulls,” and some will be “false nulls.”

Steps:
1. Pick the total number of tests $m$ (like 100 or 1000).  
2. Choose what percent of them are true nulls ($\pi_0 = 0.5, 0.8,$ or $0.9$).  
3. For each test:
   - If it’s a **true null**, draw $p_i \sim U(0,1)$.  
   - If it’s a **false null**, draw $p_i$ from a **Beta** distribution that makes smaller p-values  
     (like $\text{Beta}(0.5, 1)$ for moderate signals or $\text{Beta}(0.3, 1)$ for strong signals).  
4. Repeat this whole process $R = 1000$ times to get stable results.

---

## Estimands / Targets
I want to estimate:
- **False Discovery Rate (FDR):** the average proportion of false positives among all rejections.  
- **Power:** the proportion of true effects that are correctly found.

These will show how well each method balances Type I and Type II errors.

---

## Methods
I will compare three multiple-testing methods:
1. **Benjamini–Hochberg (BH):** the main method from the paper.  
   - Sort p-values from smallest to largest.  
   - Find the largest $k$ where $p_{(k)} \le \frac{k}{m} \times \alpha$.  
   - Reject all p-values $\le p_{(k)}$.  
2. **Bonferroni correction:** divide $\alpha$ by $m$; reject if $p_i \le \frac{\alpha}{m}$.  
3. **Uncorrected testing:** reject if $p_i \le \alpha$ (for comparison).

---

## Performance Measures
For each simulation and each method, I will record:
- Estimated **FDR** = (false rejections / total rejections)  
- Estimated **Power** = (true rejections / total true alternatives)  
- Average values and standard deviations across 1000 runs.

I’ll make plots that show:
- FDR vs $\alpha$ for different $\pi_0$ values  
- Power vs $\pi_0$ for different $\alpha$ values

---

## Design Summary Table

| m  | π₀  | Beta Params (a,b) | α levels | Replicates |
|----|-----|-------------------|-----------|-------------|
| 100 | 0.5 | (0.5, 1) | 0.01, 0.05, 0.10 | 1000 |
| 100 | 0.8 | (0.3, 1) | 0.01, 0.05, 0.10 | 1000 |
| 1000 | 0.9 | (0.5, 1) | 0.01, 0.05, 0.10 | 1000 |

---

## Reproducibility
- I’ll set a random seed (like 1234) so results can be repeated.  
- All raw results will be saved in `results/raw/` as CSV files.  
- Figures will be created automatically and stored in `results/figures/`.  
- The full pipeline can be run with `make all`.

---

## Notes
I expect:
- BH should control FDR close to or below $\alpha$.  
- Bonferroni will be more conservative (lower FDR but also lower power).  
- Uncorrected tests will go way above $\alpha$.  

In the future, I will check what happens if tests are not independent (e.g., correlated p-values).


