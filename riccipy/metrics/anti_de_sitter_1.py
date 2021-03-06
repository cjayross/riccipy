"""
Name: Anti-de Sitter
References: Hawking and Ellis (5.9) p131
Symmetry: Maximal
"""
from sympy import cos, diag, sin, sinh, symbols

coords = symbols("t chi theta phi", real=True)
variables = ()
functions = ()
t, ch, th, ph = coords
metric = diag(
    -1,
    cos(t) ** 2,
    cos(t) ** 2 * sinh(ch) ** 2,
    cos(t) ** 2 * sinh(ch) ** 2 * sin(th) ** 2,
)
