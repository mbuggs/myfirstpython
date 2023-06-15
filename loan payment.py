# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 17:25:34 2023

@author: mbuggs3
"""

import numpy as np
 
n = 48
PV = input('enter PV:')
PV = float(PV)
print(f"PV = {PV}")

r = input ('enter APR: ')
r = float(r)/100
r = r/12
print(f"interest = {r: 0.3f}")
def Idunno (PV, r, n):
     Pmt = r * PV/(1-(1+r)**-n)
     return Pmt
 
pmt= Idunno(PV, r, n)
pmt = np.round (pmt, 2)
print(f" payment is {pmt: } per month") 