# KRAS G12C Computational Drug Discovery Pipeline

## Overview
This project analyzes the structure of KRAS G12C, a key cancer 
target, and compares three covalent inhibitors (ARS-1620, ARS-853, 
JDQ443) using molecular docking with HADDOCK.

## Key Findings
- Measured the covalent bond between Sotorasib and CYS12: 1.8 Å
- RMSD of 0.557 Å between apo and holo structures
- ARS-853 showed the strongest HADDOCK score (-43.8)
- JDQ443 bound the same pocket with a different chemical scaffold

## Tools Used
PyMOL, HADDOCK, Python (Biopython, Matplotlib)

## Project Structure
- `data/` - PDB structures
- `scripts/` - Python analysis scripts
- `figures/` - Visualizations
- `results/` - Analysis results and full report

## Full Report
See `results/biological_interpretation.md` for the complete 
scientific analysis.
