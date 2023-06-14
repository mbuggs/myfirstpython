# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def calculate_max_height(v0, g):
    t = v0 / g
    max_height = (v0 ** 2) / (2 * g) 
    return max_height
v0 = float(input("Enter the initial velocity of the ball (ft/sec): "))
g = 32.8
max_height = calculate_max_height(v0, g)
print(f"The maximum height reached by the ball is: {max_height} ft")


def calculate_max_height(v0, g):
    """
    Calculates the maximum height reached by a ball thrown upward.

    Args:
        v0: Initial velocity of the ball in ft/sec (thrown upward).
        g: Force of gravity in ft/sec^2.

    Returns:
        The maximum height reached by the ball in ft.
    """
    t = v0 / g  # Time taken to reach the highest point
    max_height = (v0 ** 2) / (2 * g)  # Maximum height formula

    return max_height

# Get inputs from the user
v0 = float(input("Enter the initial velocity of the ball (ft/sec): "))
g = 32.8  # Acceleration due to gravity in ft/sec^2

# Calculate the maximum height
max_height = calculate_max_height(v0, g)

# Print the result
print(f"The maximum height reached by the ball is: {max_height} ft")
