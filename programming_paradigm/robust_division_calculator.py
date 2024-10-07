def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        
        if den == 0:
            return "Error: Cannot divide by zero."
        
        return f"The result of the division is {num / den:.1f}"
    
    except ValueError:
        return "Error: Please enter numeric values only."

