def calculate_factorial(n):
    """
    Returns the factorial of a non-negative integer n.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("The argument must be a non-negative integer.")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

if __name__ == "__main__":
    try:
        n = int(input("Enter a non-negative integer to calculate its factorial: "))
        print(f"The factorial of {n} is: {calculate_factorial(n)}")
    except ValueError as e:
        print(e)

