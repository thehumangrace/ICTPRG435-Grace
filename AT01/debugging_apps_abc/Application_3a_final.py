#!/usr/bin/env python3

# Coded Python Script
# Author Linus Torvalds
# Date: 18/09/2025

# Import math module for accurate pi value
import math

# CamelCase is preferable when creating a class
class Areas:
    # Added a missing colon for function definition
    def rect_square(self, side_length):
        # Uses a local variable
        square_area = side_length * side_length
        return square_area

    # Added a space for function and deleted semicolons
    def circle_area(self, radius_length):
        # Made calculation more concise
        # Use math.pi for more accurate value (3.14)
        circle_area = math.pi * radius_length ** 2
        return circle_area

def main():
    # This function is not part of the class Areas()
    # Create an instance of Areas class
    calculator = Areas()
    # Removed any redundancies
    # Format output to 2 decimal places for cleaner display
    print(f"Area of square is: {calculator.rect_square(2):.2f}")
    print(f"Area of circle is: {calculator.circle_area(3):.2f}")

# Added condition to only run main when script is executed directly
if __name__ == "__main__":
    main()