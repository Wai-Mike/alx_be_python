class Calculator:
    """A calculator class demonstrating class methods and static methods."""
    
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """Static method to add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """Class method to multiply two numbers.
        
        Args:
            cls: The class itself
            a: First number
            b: Second number
            
        Returns:
            The product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

