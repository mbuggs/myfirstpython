# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

def aliens (f, n):
    """
    

    Parameters
    ----------
    f : integer arry 
        DESCRIPTION.
    n : integer
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    F [n +1] = F[n] + F[n-1]
    return F

F = np.zeros(100, dtype=int)
F[0] = 0
F[1] = 1

for n in range (2,99):
    F[n] = aliens (F, n)