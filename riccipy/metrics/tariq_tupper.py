"""
Name: Tariq and Tupper
References:
    - Tariq et al., Gen. Rel. Grav., v6, p345, (1975)
    - Stephani (11.64) p138
Coordinates: Cartesian
Notes: Admits G3VIo on S3
"""
from sympy import diag, exp, symbols

coords = symbols("t x y z", real=True)
variables = ()
functions = ()
t, x, y, z = coords
metric = diag(-1, 4 * t ** 2 / 3, t / exp(2 * x), t * exp(2 * x))
