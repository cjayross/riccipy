"""
Name: Vaidya
References: Stephani (13.20) p158
Coordinates: Eddington-Finkelstein
Notes: Outgoing Coordinates
"""
from sympy import Function, diag, sin, symbols

coords = symbols("r v theta phi", real=True)
variables = ()
functions = symbols("M", cls=Function)
r, v, th, ph = coords
M = functions
metric = diag(0, -(1 - 2 * M(v) / r), r ** 2, r ** 2 * sin(th) ** 2)
metric[0, 1] = metric[1, 0] = -1
