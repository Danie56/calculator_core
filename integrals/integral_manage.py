from .models import Integral
from .constants import *
import numpy as np
import re
import pandas as pd
import matplotlib.pyplot as plt

def solve_integrals(expression,sub_intervals,type_method):
    match = re.search(r'\\int_{(-?\d*\.?\d+)}\^{(-?\d*\.?\d+)}\s+(.+?)\s*\\, dx', expression)
    if not match:
        raise ValueError("La expresión de la integral no es válida.")
    
    lower_limit = float(match.group(1))
    upper_limit = float(match.group(2))
    func_str = match.group(3).replace('^', '**').replace('{','(').replace('}',')')

    if type_method == TRAPEZOIDAL_METHOD:
        integral_value =trapezoidal_rule(integrand,lower_limit,upper_limit,sub_intervals,func_str)
        return integral_value;
    
    elif type_method == JORGE:
        integral_value = jorge_rule(lower_limit,upper_limit,integrand,func_str)
        return integral_value



def integrand(x, func_str):
    allowed_funcs = {
        'sin': np.sin,
        'cos': np.cos,
        'tan': np.tan,
        'exp': np.exp,
        'log': np.log,
        'log10': np.log10,
        'sqrt': np.sqrt,
        'pi': np.pi,
        'e': np.e
    }
    
    return eval(func_str, {"__builtins__": None}, {**allowed_funcs, 'x': x})
def trapezoidal_rule(func, a, b, n, func_str):
    n= int(n)

    h = (float(b) - float(a)) / int(n)
    integral = 0.5 * (func(a, func_str) + func(b, func_str))
    for i in range(1, n):
        integral += func(a + i * h, func_str)
    integral *= h
    return integral
def jorge_rule(a, b,func,func_str):
    h = (float(b) - float(a)) /4
    limit = a
    x=[]
    y=[]
    z = [7,32,12,32,7]

    for i in range(0,4):
        x.append(limit)
        y.append(func(limit,func_str)*z[i])
        limit += h
        if limit == b:
            x.append(limit)
            y.append(func(limit,func_str)*z[4])

            break
    
    addition = sum(y)
    ir = 2 * h * addition / 45

    data = {'x': x, 'y': y}
    df = pd.DataFrame(data)
    df.loc['Total'] = pd.Series(df['y'].sum(), index=['y'])
    df.loc['I'] = pd.Series(ir, index=['y'])
    fig, ax = plt.subplots(figsize=(8, 4))  
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=df.values,
                    colLabels=df.columns,
                    rowLabels=df.index,
                    cellLoc='center',
                    loc='center')

    plt.show()
    
    return ir
