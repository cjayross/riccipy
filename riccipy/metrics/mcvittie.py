"""
Name: McVittie Einstein-Maxwell Field
References:
    - McVittie, Prog. Roy. Soc. Lond., v124, p366, (1929)
    - Stephani (13.26) p158
Coordinates: Cartesian
"""
from sympy import diag, symbols

coords = symbols("t x y z", real=True)
variables = symbols("M Q", constant=True)
functions = ()
t, x, y, z = coords
M, Q = variables
metric = diag(-(M / z + Q ** 2 / z ** 2), z ** 2, z ** 2, 1 / (M / z + Q ** 2 / z ** 2))
