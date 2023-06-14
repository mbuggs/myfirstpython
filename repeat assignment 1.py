# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 18:50:03 2023

@author: mbuggs3
"""
import math

def calculate_max_height(initial_velocity):
    g = 32.2  # Acceleration due to gravity in ft/s²
    theta = 90  # Launch angle in degrees (straight up)
    
    # Convert launch angle to radians
    theta_rad = math.radians(theta)
    
    # Calculate the maximum height
    height = (initial_velocity**2 * math.sin(theta_rad)**2) / (2 * g)
    
    return height

# Call the function with initial velocity of 50 ft/s
max_height = calculate_max_height(50)
print(f"The maximum height reached is {max_height} feet.")


