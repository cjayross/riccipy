"""
Name: Szekeres Stiff Perfect Fluid
References: Szekeres, Commun. Math. Phys., v41, p55, (1975)
Coordinates: Cartesian
"""
from sympy import cos, diag, symbols

coords = symbols("t x y z", real=True)
variables = ()
functions = ()
t, x, y, z = coords
metric = diag(
    -(x ** 6), x ** 4 * cos(2 * t) ** 2, x ** 2 / cos(2 * t), x ** 2 / cos(2 * t)
)
