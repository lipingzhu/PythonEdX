## this import method does not work in edx
from math import sin, cos

def _fun(x):
    y = sin(x) - cos(x) + sin(x)*cos(x)
    return y

print (_fun(100))

 
