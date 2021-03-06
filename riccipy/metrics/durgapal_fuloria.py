"""
Name: Durgapal and Fuloria Perfect Fluid
References: Durgapal et al., Gen. Rel. Grav., v17, p671-681, (1985)
Coordinates: Spherical
Symmetry:
    - Spherical
    - Static
"""
from sympy import diag, sin, symbols

coords = symbols("t r theta phi", real=True)
variables = symbols("B C", constant=True)
functions = ()
t, r, th, ph = coords
B, C = variables
expr = 1 + C * r ** 2
metric = diag(
    -B * expr ** 4,
    7 * expr ** 2 / (-(expr ** 2) - 8 * expr + 16),
    r ** 2,
    r ** 2 * sin(th) ** 2,
)
