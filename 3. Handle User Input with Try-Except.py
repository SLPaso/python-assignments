while True:
    try:
        num = int(input("Enter a number: "))
        print(f"You entered: {num}")
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")