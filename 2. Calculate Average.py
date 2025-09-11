def calculate_average(*args):
    """
    This function calculates the average of a variable number of arguments.
    :param args: A variable number of numerical inputs.
    :return: The average of the numbers.
    """
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

# Example usage
average = calculate_average(10, 20, 30, 40)
print(f"The average is: {average}")