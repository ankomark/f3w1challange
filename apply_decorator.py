def decorator_func(func):
    """
    Decorator function that prints a message before calling the original function.
    """
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

@decorator_func
def apply_decorator():
    """
    Function to demonstrate decorator application.
    """
    print("Function Executed")

if __name__ == "__main__":
    apply_decorator()
    # Output:
    # Decorator Applied
    # Function Executed

