"""
Name: Datta
References:
    - Datta, Nuovo Cim., v36, p109
    - Stephani (11.60) p137
Coordinates: Cartesian
Notes: Type 2
"""
from sympy import diag, symbols

coords = symbols("t x y z", real=True)
variables = symbols("C_1 C_2 mu", constant=True)
functions = ()
t, x, y, z = coords
C1, C2, mu = variables
expr = (C1 * t ** mu + C2 / t ** mu) ** 2
metric = diag(
    -expr * t ** (2 * mu ** 2), 1 / expr, expr * t ** (2 * mu ** 2), t ** 2 * expr
)
