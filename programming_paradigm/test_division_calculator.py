#!/usr/bin/env python3
"""
Test script to demonstrate the robust division calculator functionality.
This script simulates the command line operations for testing purposes.
"""

from robust_division_calculator import safe_divide

def test_division_calculator():
    """Test the safe_divide function with various inputs."""
    print("=== Robust Division Calculator Testing ===\n")
    
    # Test cases
    test_cases = [
        # Normal division
        ("10", "5", "Normal Division"),
        ("15", "3", "Normal Division with different numbers"),
        ("7.5", "2.5", "Decimal division"),
        
        # Division by zero
        ("10", "0", "Division by Zero"),
        ("100", "0", "Division by Zero with larger number"),
        
        # Non-numeric inputs
        ("ten", "5", "Non-numeric numerator"),
        ("10", "five", "Non-numeric denominator"),
        ("abc", "xyz", "Both non-numeric"),
        ("", "5", "Empty numerator"),
        ("10", "", "Empty denominator"),
        
        # Edge cases
        ("0", "5", "Zero numerator"),
        ("-10", "5", "Negative numerator"),
        ("10", "-5", "Negative denominator"),
        ("-10", "-5", "Both negative"),
    ]
    
    for numerator, denominator, test_name in test_cases:
        print(f"Test: {test_name}")
        print(f"Input: {numerator} / {denominator}")
        result = safe_divide(numerator, denominator)
        print(f"Output: {result}")
        print("-" * 50)

if __name__ == "__main__":
    test_division_calculator()
