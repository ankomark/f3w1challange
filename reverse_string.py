def reverse_string(text):
    """
    Returns the reversed version of the input string text.
    """
    if not isinstance(text, str):
        raise ValueError("The argument must be a string.")
    return text[::-1]

if __name__ == "__main__":
    text = input("Enter a string to reverse: ")
    print(f"The reversed string is: {reverse_string(text)}")

