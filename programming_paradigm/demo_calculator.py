#!/usr/bin/env python3
"""
Demonstration script for the SimpleCalculator class.
This script shows the calculator functionality and some test cases.
"""

from simple_calculator import SimpleCalculator

def demo_calculator():
    """Demonstrate the SimpleCalculator functionality."""
    print("=== SimpleCalculator Demonstration ===\n")
    
    # Create calculator instance
    calc = SimpleCalculator()
    
    # Test addition
    print("Testing Addition:")
    print(f"2 + 3 = {calc.add(2, 3)}")
    print(f"-1 + 1 = {calc.add(-1, 1)}")
    print(f"2.5 + 3.5 = {calc.add(2.5, 3.5)}")
    print()
    
    # Test subtraction
    print("Testing Subtraction:")
    print(f"5 - 3 = {calc.subtract(5, 3)}")
    print(f"-1 - 1 = {calc.subtract(-1, 1)}")
    print(f"5.5 - 2.5 = {calc.subtract(5.5, 2.5)}")
    print()
    
    # Test multiplication
    print("Testing Multiplication:")
    print(f"2 * 3 = {calc.multiply(2, 3)}")
    print(f"-5 * -3 = {calc.multiply(-5, -3)}")
    print(f"2.5 * 4 = {calc.multiply(2.5, 4)}")
    print()
    
    # Test division
    print("Testing Division:")
    print(f"10 / 2 = {calc.divide(10, 2)}")
    print(f"-10 / 2 = {calc.divide(-10, 2)}")
    print(f"7.5 / 2.5 = {calc.divide(7.5, 2.5)}")
    print()
    
    # Test division by zero
    print("Testing Division by Zero:")
    print(f"10 / 0 = {calc.divide(10, 0)}")
    print(f"0 / 0 = {calc.divide(0, 0)}")
    print()
    
    # Test edge cases
    print("Testing Edge Cases:")
    print(f"0 + 5 = {calc.add(0, 5)}")
    print(f"5 * 0 = {calc.multiply(5, 0)}")
    print(f"0 / 5 = {calc.divide(0, 5)}")
    print(f"1 / 1000000 = {calc.divide(1, 1000000)}")

if __name__ == "__main__":
    demo_calculator()
