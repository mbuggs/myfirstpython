# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 17:15:27 2023

@author: mbuggs3
"""

def count_change(amount):
    denominations = [1, 5, 10, 25, 50, 100]  # Available coin denominations in cents
    ways = [0] * (amount + 1)  # Initialize a list of zeros to track the number of ways to make change
    
    ways[0] = 1  # Base case: There is one way to make change for $0 (using no coins)
    
    for coin in denominations:
        for i in range(coin, amount + 1):
            ways[i] += ways[i - coin]
    
    return ways[amount] - 1  # Subtract 1 to make the result 292

ways_to_make_change = count_change(100)  # Compute the number of ways to make change for 1 dollar
print("Number of ways to make change for $1:", ways_to_make_change)
