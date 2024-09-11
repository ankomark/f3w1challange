def is_even(number):
    """
    Returns True if the number is even, False otherwise.
    """
    if not isinstance(number, int):
        raise ValueError("The argument must be an integer.")
    return number % 2 == 0

if __name__ == "__main__":
    try:
        number = int(input("Enter an integer: "))
        print(f"Is the number even? {is_even(number)}")
    except ValueError as e:
        print(e)

