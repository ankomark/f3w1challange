def merge_dicts(dict1, dict2):
    """
    This function merges two dictionaries. If a key is present in both dictionaries,
    their values are summed.
    
    Parameters:
    dict1 (dict): The first dictionary.
    dict2 (dict): The second dictionary.
    
    Returns:
    dict: The merged dictionary with summed values for common keys.
    """
    merged = dict1.copy()  # Start with dict1's keys and values
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged
