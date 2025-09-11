def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input types. Please provide numbers."

# Example usage
print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers(10, "a"))