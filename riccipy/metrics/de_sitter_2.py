"""
Name: de Sitter
References: Hawking and Ellis p125
Coordinates: Cartesian
Symmetry: Maximal
"""
from sympy import diag, exp, symbols

coords = symbols("t x y z", real=True)
variables = symbols("alpha", constant=True)
functions = ()
t, x, y, z = coords
al = variables
expr = exp(2 * t / al)
metric = diag(-1, expr, expr, expr)
