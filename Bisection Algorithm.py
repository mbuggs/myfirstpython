# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np 
import matplotlib.pyplot as plt
def f(x):
    """
    f(x) = exp(x - x**2)

    Parameters
    ----------
    x : TYPE float 
        DESCRIPTION. input to the function f(x)

    Returns
    -------
    y: output the function f(x)

    """
    
    y = np.exp(x) - x**2
    return y 

## find x so that x is = 0 

xAxis =np.linspace (-3,1)
y = f(xAxis)
   
plt.plot(xAxis, y)
plt.axline(y=0, color = "red", ls= ':')
xLow= -1
xHigh= 2

for i in range (15):
    xTry = (xLow+xHigh)/2
    if f(xTry) > 0 :
        xHigh = xTry 
    else: 
        xLow = xTry
    print(f"x = {xTry}, f(x) = {f(xTry)}")
    
print(f"final ans= {xTry}, f = {f(xTry)}")