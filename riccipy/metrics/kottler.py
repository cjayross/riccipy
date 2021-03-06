"""
Name: Schwarzschild-de Sitter
Coordinates: Spherical
Symmetry: Spherical
Notes: Cosmological Constant
"""
from sympy import diag, sin, symbols

coords = symbols("t r theta phi", real=True)
variables = symbols("M Lambda", constant=True)
functions = ()
t, r, th, ph = coords
M, La = variables
expr = 1 - 2 * M / r - La * r ** 2 / 3
metric = diag(-expr, 1 / expr, r ** 2, r ** 2 * sin(th) ** 2)
