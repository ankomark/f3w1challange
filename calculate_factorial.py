def calculate_factorial(n):
    """
    This function calculates the factorial of a non-negative integer.
    
    Parameters:
    n (int): The non-negative integer to calculate the factorial of.
    
    Returns:
    int: The factorial of the input number.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)
