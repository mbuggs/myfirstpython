# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 18:20:15 2023

@author: mbuggs3
"""

import numpy as np 
import matplotlib.pyplot as plt
def f(x):
    """
  x**2 - 3x + 1

    Parameters
    ----------
    x : TYPE float 
        DESCRIPTION. input to the function f(x)

    Returns
    -------
    y: output the function f(x)

    """
    
    y = x**2 - 3*x + 1
    return y

## find x so that x is = 0 

xAxis =np.linspace (-3,1)
y = f(xAxis)
   
plt.plot(xAxis, y)
plt.axline(y=0, color = "red", ls= ':')
xLow= 1
xHigh= -1

for i in range (15):
    xTry = (xLow+xHigh)/2
    if f(xTry) > 0 :
        xHigh = xTry 
    else: 
        xLow = xTry
    print(f"x = {xTry}, f(x) = {f(xTry)}")
    
print(f"final ans= {xTry}, f = {f(xTry)}")