# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 18:30:59 2023

@author: mbuggs3
"""

def count_ways_to_make_change(coins, amount):
    ways = [0] * (amount + 1)
    ways[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            ways[i] += ways[i - coin]

    return ways[amount]

coins = [1, 2, 5, 10, 20, 50, 100]  # Updated coin denominations
amount = 100

num_ways = count_ways_to_make_change(coins, amount)
print("Number of ways to make change for a dollar:", num_ways)

