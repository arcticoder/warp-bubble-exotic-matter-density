# warp-bubble-exotic-matter-density

This repository provides tools to extract and simplify the exotic-matter energy-density component \(T^{00}\) from the warp-bubble stress–energy tensor, highlight regions where it is negative, and generate a LaTeX report of the results.

## Contents

- **isolate_exotic.py**  
  - Downloads the LaTeX source of the stress–energy tensor  
  - Parses the 4×4 matrix into a SymPy `Matrix`  
  - Simplifies the \(T^{00}\) component  
  - Solves the inequality \(T^{00}<0\) to find analytic conditions on the profile function  
  - Writes out `exotic_matter_density.tex`

- **exotic_matter_density.tex**  
  A self-contained LaTeX document that displays:
  1. The simplified energy-density \(\widetilde T^{00}(r,t)\)  
  2. The analytic condition \(\widetilde T^{00}(r,t)<0 \iff \dots\)

## Requirements

- Python 3.x  
- [SymPy](https://www.sympy.org/)  
- [requests](https://pypi.org/project/requests/)

## Installation & Usage

1. **Clone the repo**  
```bash
   git clone https://github.com/arcticoder/warp-bubble-exotic-matter-density.git
   cd warp-bubble-exotic-matter-density
```

2.  **Install dependencies**
    
```bash
pip install sympy requests
```
    
3.  **Run the extraction script**
    
```bash
python isolate_exotic.py
```
    
4.  **Compile the LaTeX report**
    
```bash
pdflatex exotic_matter_density.tex
```
    

The output PDF will contain the simplified expression for $\widetilde T^{00}$ and the condition under which it becomes negative.
