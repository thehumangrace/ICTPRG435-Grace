#!/usr/bin/env python3

# Coded Python Script
# Author Grace Hopper 
# Date: 29/10/2025

# Added space between import and os
import os

#initialise variables
hours=0
rate=0
pay=0

# Added closing quotation
os.system("clear")
# run the Linux system clear screen command

# input values with error handling
# Added while loop to keep asking until valid input
while True:
    try:
        # Added closing bracket and spaces
        hours = float(input("Enter your hours: "))
        # Check if hours is negative
        if hours < 0:
            print("Error: It can't be a negative number, chief.")
            continue
        break  # Exits loop if input is valid
    except ValueError:
        # Catches accidental letters or symbols
        print("Error: Try a number this time, buddy.")

# Added while loop for rate input validation
while True:
    try:
        # Added closing quotation spaces and removed semicolons
        rate = float(input("Enter pay rate: "))
        # Check if rate is negative
        if rate < 0:
            print("Error: It can't be a negative number, friend.")
            continue
        break  # Exit loop if input is valid
    except ValueError:
        # Catches accidental letters or symbols
        print("Error: Try a number this time, guy.")

# Added spaces
pay = hours*rate

# Added the print statement here to make calculated pay show
# the f indicates an f-string
# 2f formats for 2 decimal places instead of only 1
print(f"Total Pay is: ${pay:.2f}")