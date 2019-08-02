"""
Levi-Civita solution, Class BIII
Stephani (Table 16.2) p188
"""
from sympy import diag, symbols

coords = symbols('t z r phi', real=True)
variables = ()
functions = ()
t, z, r, ph = coords
metric = diag(-r ** 2 * z ** 2, z, z ** 2, 1 / z)