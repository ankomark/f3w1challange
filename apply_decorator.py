def decorator_func(func):
    """
    This is a decorator that prints "Decorator Applied" before
    calling the original function.
    """
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

@decorator_func
def apply_decorator(func):
    """
    This function takes another function as input and applies the decorator to it.
    
    Parameters:
    func (function): The function to be decorated.
    
    Returns:
    function: The decorated function.
    """
    return func()
