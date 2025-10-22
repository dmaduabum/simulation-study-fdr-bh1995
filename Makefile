# Makefile for BH FDR Simulation Study

.PHONY: all simulate figures clean test

all: simulate figures

simulate:
	python src/simulation.py

figures:
	python src/visualize.py

test:
	pytest tests/ -v

clean:
	rm -rf results/raw/*.csv results/figures/*.pdf results/figures/*.png

help:
	@echo "Targets:"
	@echo "  make all       - Run simulation and generate figures"
	@echo "  make simulate  - Run simulation only"
	@echo "  make figures   - Generate visualizations"
	@echo "  make test      - Run test suite"
	@echo "  make clean     - Remove generated files"