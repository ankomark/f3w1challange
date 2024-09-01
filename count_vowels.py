def count_vowels(text):
    """
    This function counts the number of vowels in a string.
    
    Parameters:
    text (str): The input string.
    
    Returns:
    int: The number of vowels in the string.
    """
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in text if char in vowels)
    return count
