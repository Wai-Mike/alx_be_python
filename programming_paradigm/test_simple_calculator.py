import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 15), 25)
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)
        
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 5), -5)
        self.assertEqual(self.calc.add(10, -5), 5)
        
        # Test decimal numbers
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertEqual(self.calc.add(0.1, 0.2), 0.3)
        self.assertEqual(self.calc.add(-2.5, 1.5), -1.0)

    def test_subtraction(self):
        """Test the subtraction method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-10, 5), -15)
        self.assertEqual(self.calc.subtract(10, -5), 15)
        
        # Test decimal numbers
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)
        self.assertEqual(self.calc.subtract(0.3, 0.1), 0.2)
        self.assertEqual(self.calc.subtract(-2.5, 1.5), -4.0)

    def test_multiplication(self):
        """Test the multiplication method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(5, 4), 20)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(1, 5), 5)
        self.assertEqual(self.calc.multiply(5, 1), 5)
        
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-5, -3), 15)
        self.assertEqual(self.calc.multiply(-10, 5), -50)
        self.assertEqual(self.calc.multiply(10, -5), -50)
        
        # Test decimal numbers
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(0.5, 0.5), 0.25)
        self.assertEqual(self.calc.multiply(-2.5, 2), -5.0)

    def test_division(self):
        """Test the division method with various scenarios."""
        # Test normal division
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(1, 1), 1.0)
        
        # Test negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        
        # Test decimal numbers
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertEqual(self.calc.divide(0.6, 0.2), 3.0)
        self.assertEqual(self.calc.divide(-7.5, 2.5), -3.0)

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        # Test division by zero
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(100, 0))

    def test_edge_cases(self):
        """Test edge cases and boundary values."""
        # Test very large numbers
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)
        self.assertEqual(self.calc.multiply(1000, 1000), 1000000)
        
        # Test very small numbers
        self.assertEqual(self.calc.add(0.0001, 0.0002), 0.0003)
        self.assertEqual(self.calc.multiply(0.001, 0.001), 0.000001)
        
        # Test division with very small numbers
        self.assertEqual(self.calc.divide(1, 1000000), 0.000001)
        self.assertEqual(self.calc.divide(0.000001, 0.000001), 1.0)

    def test_data_types(self):
        """Test that methods work with different numeric data types."""
        # Test with integers
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.multiply(6, 7), 42)
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        
        # Test with floats
        self.assertEqual(self.calc.add(5.0, 3.0), 8.0)
        self.assertEqual(self.calc.subtract(10.0, 4.0), 6.0)
        self.assertEqual(self.calc.multiply(6.0, 7.0), 42.0)
        self.assertEqual(self.calc.divide(15.0, 3.0), 5.0)

if __name__ == '__main__':
    # Run the tests
    unittest.main()
