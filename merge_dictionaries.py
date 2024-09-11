def merge_dicts(dict1, dict2):
    """
    Merges two dictionaries. If there are common keys, their values are summed up.
    """
    if not (isinstance(dict1, dict) and isinstance(dict2, dict)):
        raise ValueError("Both arguments must be dictionaries.")
    merged = dict1.copy()
    for key, value in dict2.items():
        merged[key] = merged.get(key, 0) + value
    return merged

if __name__ == "__main__":
    try:
        dict1 = eval(input("Enter the first dictionary (e.g., {'a': 1, 'b': 2}): "))
        dict2 = eval(input("Enter the second dictionary (e.g., {'b': 3, 'c': 4}): "))
        if not isinstance(dict1, dict) or not isinstance(dict2, dict):
            raise ValueError("Inputs must be valid dictionaries.")
        print(f"Merged dictionary: {merge_dicts(dict1, dict2)}")
    except Exception as e:
        print(e)
