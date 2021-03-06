"""
Name: Levi-Civita
References: Stephani (Table 16.2) p188
Coordinates: Spherical
Symmetry: Spherical
Notes: Class B1
"""
from sympy import diag, sin, symbols

coords = symbols("t r theta phi", real=True)
variables = symbols("M", constant=True)
functions = ()
t, r, th, ph = coords
M = variables
metric = diag(-(r ** 2) * sin(th) ** 2, 1 / (1 - 2 * M / r), r ** 2, 1 - 2 * M / r)
