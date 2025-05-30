import sympy as sp
import requests
import re
from sympy import symbols, Function, Matrix

# Define symbols & profile
t, r, theta, phi = symbols('t r theta phi')
f = Function('f')(r, t)

# Load stress–energy LaTeX
URL = 'https://raw.githubusercontent.com/arcticoder/warp-bubble-einstein-equations/refs/heads/main/stress_energy.tex'
resp = requests.get(URL)
latex = resp.text

# Extract matrix contents
pattern = r'\\begin{pmatrix}(.+?)\\end{pmatrix}'
m = re.search(pattern, latex, re.S)
if not m:
    raise ValueError("Stress-energy matrix not found")
matrix_content = m.group(1).strip()

# Parse into SymPy Matrix
rows = [row.strip() for row in matrix_content.split(r'\\\\')]
entries = [
    [sp.sympify(entry.strip()) for entry in row.split('&')]
    for row in rows
]
T = Matrix(entries)

# Simplify T00 and solve inequality
T00 = sp.simplify(T[0,0])
cond = sp.solve_univariate_inequality(T00 < 0, f)

# Write LaTeX report
with open('exotic_matter_density.tex', 'w') as tex:
    tex.write(r'\documentclass{article}' + '\n')
    tex.write(r'\usepackage{amsmath}' + '\n')
    tex.write(r'\begin{document}' + '\n\n')
    tex.write(r'\section*{Exotic‐Matter Energy Density}' + '\n\n')
    tex.write('The simplified energy‐density component is\n')
    tex.write(r'\[' + '\n')
    tex.write(f'  \\widetilde T^{{00}}(r,t)\n  = {sp.latex(T00)}\n')
    tex.write(r'\]' + '\n\n')
    tex.write('Negative‐energy occurs where\n')
    tex.write(r'\[' + '\n')
    tex.write(f'  \\widetilde T^{{00}}(r,t) < 0\n  \\quad\\Longleftrightarrow\\quad\n  {sp.latex(cond)}\n')
    tex.write(r'\]' + '\n\n')
    tex.write(r'\end{document}' + '\n')
