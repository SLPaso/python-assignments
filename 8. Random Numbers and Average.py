import random

def generate_random_numbers_and_average():
    # Generate 10 random integers between 1 and 100
    numbers = [random.randint(1, 100) for _ in range(10)]
    average = sum(numbers) / len(numbers)
    print("Generated numbers:", numbers)
    print("Average:", average)

generate_random_numbers_and_average()