def add_numbers(num1, num2):
    """
    Returns the sum of num1 and num2.
    """
    if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
        raise ValueError("Both arguments must be numbers (int or float).")
    return num1 + num2

if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The sum is: {add_numbers(num1, num2)}")
    except ValueError as e:
        print(e)

