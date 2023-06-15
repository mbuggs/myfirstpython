# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 18:35:51 2023

@author: mbuggs3
"""

def calculate_monthly_repayment(PV, r, n):
    # Convert APR to monthly interest rate
    monthly_interest = r / (12 * 100)

    # Calculate the denominator part of the formula
    denominator = 1 - (1 + monthly_interest) ** -n

    # Calculate the monthly repayment amount
    Pmt = monthly_interest * PV / denominator

    return int(Pmt)  # Convert the result to an integer

# Test the function with the given values
PV = 12000
r = 7.45
n = 48

monthly_repayment = calculate_monthly_repayment(PV, r, n)
print("Monthly Repayment Amount:", monthly_repayment)
