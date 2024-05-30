from .models import Integral
from .constants import *
import numpy as np
import re
import pandas as pd
import matplotlib.pyplot as plt
from fractions import Fraction

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

    elif type_method == SIMPSON_3_8:
        integral_value = simpson_rule(lower_limit,upper_limit,integrand,func_str)

        return integral_value 
    elif  type_method == SIMPSON_1_3:
        integral_value = simpson_1_3(lower_limit,upper_limit,integrand,func_str)
        return integral_value
    elif type_method == OPEN_SIMPSON:
        integral_value =open_simpson(integrand,lower_limit,upper_limit,sub_intervals,func_str)
        return integral_value;

def nth_root(x, n):
    return np.power(x, 1/n)

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
        'e': np.e,
        'nth_root': nth_root  

        
        
    }
    
    return eval(func_str, {"__builtins__": None}, {**allowed_funcs, 'x': x})
def trapezoidal_rule(func, a, b, n, func_str):
    a = float(a)
    b = float(b)
    n = int(n)
    h = (b - a) / n

    x = [a + i * h for i in range(n + 1)]

    y = [(func(xi,func_str) if (i == 0 or i == n) else 2 * func(xi,func_str)) for i, xi in enumerate(x)]

    ir = (h * sum(y))/2
    show_table(x,y,ir,sum(y))
    yg = [func(float(xi), func_str) for xi in x]
    plot_points(x,yg)

    return ir
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
    ir = (2 * h * addition) / 45
    yg = [func(float(xi), func_str) for xi in x]
    show_table(x,y,ir,addition)
    plot_points(x,yg)


    
    return ir


def simpson_rule(a, b, func, func_str):
    a = Fraction(a)
    b = Fraction(b)
    
    h = (b - a) / 3
    
    x = [a + i * h for i in range(4)]
    
    y = [func(float(xi), func_str) for xi in x]
    
    integral = ((y[0] + 3*y[1] + 3*y[2] + y[3]) * 3 * h) / 8
    print(y)

    show_table(x,y,integral,sum(y))
    yg = [func(float(xi), func_str) for xi in x]
    plot_points(x,yg)


    return float(integral)
def simpson_1_3(a, b, func, func_str):
        limit = a
        x=[]

        h = (b - a) / 2
        for i in range(0,3):
            x.append(limit)
            limit += h
        
        y=[func(x[0],func_str),(func(x[1],func_str))*4,func(x[2],func_str)]
        addition = sum(y)
        ir = (h * addition) / 3
        show_table(x,y,ir,sum(y))
        yg = [func(float(xi), func_str) for xi in x]
        plot_points(x,yg)


        return ir
def open_simpson (func, a, b, n, func_str):
    a = float(a)
    b = float(b)
    n = int(n)
    h = (b - a) / n

    x = [a + i * h for i in range(n + 1)]

    y = [(func(xi,func_str) if (i == 0 or i == n) else (func(xi,func_str)*2 if i% 2 == 0 else 4* func(xi,func_str)*4)) for i, xi in enumerate(x)]
    print(y)
    ir = (h * sum(y))/3
    show_table(x,y,ir,sum(y))
    yg = [func(float(xi), func_str) for xi in x]
    plot_points(x,yg)


    return ir

def show_table (x,y,ir,addition):
    data = {'x': x, 'y': y}
    df = pd.DataFrame(data)
    df.loc['Total'] = pd.Series(addition, index=['y'])
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
def plot_points(x, y):
    plt.scatter(x, y, color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Puntos de integración')
    plt.show()
