def sort_by_age(people):
    """
    Sorts a list of tuples (name, age) by age in ascending order.
    """
    if not all(isinstance(person, tuple) and len(person) == 2 for person in people):
        raise ValueError("Each item in the list must be a tuple of (name, age).")
    return sorted(people, key=lambda person: person[1])

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of people: "))
        people = []
        for _ in range(n):
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            people.append((name, age))
        print(f"Sorted by age: {sort_by_age(people)}")
    except ValueError as e:
        print(e)

