def count_vowels(text):
    """
    Returns the count of vowels in the input string text, ignoring case.
    """
    if not isinstance(text, str):
        raise ValueError("The argument must be a string.")
    vowels = set("aeiou")
    return sum(1 for char in text.lower() if char in vowels)

if __name__ == "__main__":
    text = input("Enter a string to count vowels: ")
    print(f"Number of vowels in the string: {count_vowels(text)}")
