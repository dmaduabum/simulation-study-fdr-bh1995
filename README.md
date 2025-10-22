# Benjamini-Hochberg FDR Simulation Study

Reproduction of Benjamini & Hochberg (1995): "Controlling the false discovery rate: a practical and powerful approach to multiple testing."

## Project Description

This simulation study reproduces the main theoretical result from the seminal BH (1995) paper: the Benjamini-Hochberg procedure controls the False Discovery Rate at level α while maintaining substantially higher power than traditional methods like Bonferroni correction.

## Setup Instructions

**Requirements:**
- Python 3.8+
- Dependencies listed in `requirements.txt`

**Installation:**
```bash
pip install -r requirements.txt
```

## How to Run the Complete Analysis

**Option 1: Using Makefile**
```bash
make all
```

**Option 2: Step-by-step**
```bash
python src/simulation.py    # Run simulation (~3 min)
python src/visualize.py     # Generate figures
pytest tests/ -v            # Run tests
```

## Estimated Runtime

- Simulation: ~3 minutes (27,000 replications across 27 conditions)
- Visualization: <10 seconds
- Tests: <5 seconds
- **Total: ~4 minutes**

## Summary of Key Findings

**Main result:** The BH procedure successfully controls FDR ≤ 0.05 across all tested scenarios (varying m, π₀, effect sizes), confirming Theorem 1 from the paper. Power is 2-3× higher than Bonferroni correction, especially when many hypotheses are false.

See `ANALYSIS.md` for detailed results and discussion.

## Project Structure
```
.
├── ADEMP.md              # Simulation design document
├── ANALYSIS.md           # Results and interpretation
├── README.md             # This file
├── Makefile              # Automation
├── requirements.txt      # Dependencies
├── src/
│   ├── dgps.py          # Data generation
│   ├── methods.py       # BH, Bonferroni, Uncorrected
│   ├── metrics.py       # FDR and Power calculation
│   ├── simulation.py    # Main simulation loop
│   └── visualize.py     # Figure generation
├── tests/
│   └── test_basic.py    # Unit tests
└── results/
    ├── raw/             # Simulation output (CSV)
    └── figures/         # Generated plots (PDF)
```

## Author

Dili K. Maduabum  
October 21, 2025
