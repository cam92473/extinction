import numpy as np
from GUI.py import c1,c2,c4,c5,x0,c3,gamma,O3,O2,O1,k_IR,R_V,ir_shrtst,opt_shrtst,uvN_shrtst
from scipy.interpolate import CubicSpline

# -------------
# Model functions for various regions
# -------------

def func_D(x):
    return x**2/((x**2-x0**2)**2+x**2*gamma**2)

def ir_model(x):
    return k_IR * x ** 1.84 - R_V

def opt_model(x):
    xopt = np.array([1000/ir_shrtst, 1.8083, 2.5, 3.0303, 1000/opt_shrtst])
    yopt = np.array([ir_model(1000/ir_shrtst), O3, O2, O1, uv_lng_model(1000/opt_shrtst)])
    cs = CubicSpline(xopt, yopt, bc_type='natural')
    return cs(x)

def uv_lng_model(x):
    return c1+c2*x+c3*func_D(x)

def uv_srt_model(x):
    return c1+c2*x+c3*func_D(x)+c4*(x-c5)**2
