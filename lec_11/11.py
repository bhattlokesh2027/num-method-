import numpy as np
from scipy.interpolate import CubicSpline
x =np.array([0,1,2])
y =np.array([1,2,4])
l = CubicSpline(x,y)
print("interpolated value is", l(1.5))
def f(x):
	return 2**x
print("exact value is",f(1.5))

