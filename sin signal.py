import numpy as np
from sympy import plot,sin,Symbol
t=Symbol('t')
y=sin(np.pi/4*t)
plot(y)