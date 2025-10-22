"""
test_basic.py
-----------------
Basic test suite for the Unit 2 FDR simulation study.

These tests check that:
1. Data generation works correctly.
2. Metrics (FDR, Power) return valid values.
3. The simulation script produces an output file.

Run with:
    pytest tests/
"""

import os
import pandas as pd
import numpy as np

from src.dgps import generate_pvalues
from src.methods import bh_procedure, bonferroni_method, uncorrected_method
from src.metrics import compute_fdr, compute_power
from src.simulation import run_single_simulation


def test_generate_pvalues_shape():
    """Test that generate_pvalues returns the correct number of rows."""
    df = generate_pvalues(m=50, pi0=0.8, effect_size=1.0, seed=1)
    assert len(df) == 50
    assert set(df.columns) == {"p_value", "is_null"}


def test_methods_return_booleans():
    """Test that each method returns a boolean array of the same length."""
    df = generate_pvalues(m=20, pi0=0.8, effect_size=1.0, seed=123)
    pvals = df["p_value"].values
    
    for method in [bh_procedure, bonferroni_method, uncorrected_method]:
        rejects = method(pvals, alpha=0.05)
        assert isinstance(rejects, np.ndarray)
        assert rejects.dtype == bool
        assert len(rejects) == len(pvals)


def test_metrics_valid_range():
    """Test that FDR and Power values are between 0 and 1."""
    df = generate_pvalues(m=30, pi0=0.7, effect_size=1.0, seed=99)
    pvals = df["p_value"].values
    is_null = df["is_null"].values
    
    rejects = bh_procedure(pvals, alpha=0.05)
    fdr = compute_fdr(rejects, is_null)
    power = compute_power(rejects, is_null)
    
    assert 0.0 <= fdr <= 1.0
    assert 0.0 <= power <= 1.0


def test_simulation_creates_results():
    """Test that a single simulation run returns valid results."""
    out = run_single_simulation(m=50, pi0=0.8, effect_size=1.0, alpha=0.05, seed=42)
    
    assert isinstance(out, dict)
    assert "BH" in out
    
    for metrics in out.values():
        assert 0.0 <= metrics["FDR"] <= 1.0
        assert 0.0 <= metrics["Power"] <= 1.0
