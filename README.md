# warp-bubble-exotic-matter-density

Automates the extraction and simplification of the warp-bubble stress–energy tensor’s energy-density component \(T^{00}\), determines analytic conditions for its negative-energy regions, and produces a standalone LaTeX report.

## Contents

- **isolate_exotic.py**  
  - Fetches the LaTeX source from the previous repo  
  - Extracts and sympifies the 4×4 matrix  
  - Simplifies the \(T^{00}\) entry  
  - Solves \(T^{00}(r,t) < 0\) for \(f(r,t)\)  
  - Writes out **exotic_matter_density.tex**

- **exotic_matter_density.tex**  
  A self-contained LaTeX document displaying:
  1. \(\widetilde T^{00}(r,t)\) in simplified form  
  2. The analytic condition \(\widetilde T^{00}(r,t) < 0 \iff \dots\)

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

The resulting PDF will contain the simplified expression for $\widetilde T^{00}(r,t)$ and the precise condition under which it becomes negative.
