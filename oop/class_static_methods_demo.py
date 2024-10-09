class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        Args:
            a (int/float): The first number.
            b (int/float): The second number.
        Returns:
            int/float: The sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        Prints the class attribute 'calculation_type'.
        Args:
            a (int/float): The first number.
            b (int/float): The second number.
        Returns:
            int/float: The product of a and b.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
