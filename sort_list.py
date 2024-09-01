def sort_by_age(people):
    """
    This function sorts a list of tuples by age in ascending order.
    
    Parameters:
    people (list of tuples): A list of tuples where each tuple contains a name and an age.
    
    Returns:
    list of tuples: The sorted list of tuples by age.
    """
    return sorted(people, key=lambda person: person[1])
