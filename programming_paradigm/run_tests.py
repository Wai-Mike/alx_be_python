#!/usr/bin/env python3
"""
Simple test runner to demonstrate the unit tests functionality.
This script runs the unit tests and displays the results.
"""

import sys
import os

# Add current directory to path to import modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import unittest
    from simple_calculator import SimpleCalculator
    from test_simple_calculator import TestSimpleCalculator
    
    def run_tests():
        """Run the unit tests and display results."""
        print("=== Running Unit Tests for SimpleCalculator ===\n")
        
        # Create test suite
        suite = unittest.TestLoader().loadTestsFromTestCase(TestSimpleCalculator)
        
        # Run tests with detailed output
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        
        # Print summary
        print(f"\n=== Test Summary ===")
        print(f"Tests run: {result.testsRun}")
        print(f"Failures: {len(result.failures)}")
        print(f"Errors: {len(result.errors)}")
        
        if result.failures:
            print(f"\n=== Failures ===")
            for test, traceback in result.failures:
                print(f"FAIL: {test}")
                print(traceback)
        
        if result.errors:
            print(f"\n=== Errors ===")
            for test, traceback in result.errors:
                print(f"ERROR: {test}")
                print(traceback)
        
        if result.wasSuccessful():
            print(f"\n✅ All tests passed successfully!")
        else:
            print(f"\n❌ Some tests failed.")
    
    if __name__ == "__main__":
        run_tests()
        
except ImportError as e:
    print(f"Import error: {e}")
    print("Make sure both simple_calculator.py and test_simple_calculator.py are in the same directory.")
except Exception as e:
    print(f"Error running tests: {e}")
