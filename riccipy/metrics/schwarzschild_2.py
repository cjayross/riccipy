"""
Name: Schwarzschild
References:
    - Eddington, Nature, v113, p192, (1924)
    - Finkelstein, Phys. Rev., v110, p965, (1958)
    - Stephani (13.23) p158
Coordinates: Eddington-Finkelstein
Symmetry:
    - Spherical
    - Static
Notes: Outgoing Coordinates
"""
from sympy import diag, sin, symbols

coords = symbols("r u theta phi", real=True)
variables = symbols("M", constant=True)
functions = ()
r, u, th, ph = coords
M = variables
metric = diag(0, -(1 - 2 * M / r), r ** 2, r ** 2 * sin(th) ** 2)
metric[0, 1] = metric[1, 0] = -1
