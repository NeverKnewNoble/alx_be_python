def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            return "Error: Cannot divide by zero."
        result = num / denom
        return f"The result of the division is {result:.1f}" if result % 1 != 0 else f"The result of the division is {int(result)}"
    except ValueError:
        return "Error: Please enter numeric values only."
