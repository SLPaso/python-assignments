class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    return "Number is positive."

# Example usage
try:
    print(check_positive(10))
    print(check_positive(-5))
except NegativeNumberError as e:
    print(e)