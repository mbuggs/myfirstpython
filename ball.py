# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 17:54:51 2023

@author: mbuggs3
"""

def height(v0,t):
    g = 32.8
    y = v0*t- 0.5*g*t**2
    return y
t=1
while t > 0:
    v0 = input(' enter velocity')
    v0 = float(v0)
    t = input(' enter the time, sec: ')
    t = float(t)
    y = height(v0,t)
    print(f"after {t} seconds height = {y}")
    