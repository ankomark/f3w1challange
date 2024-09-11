class Car:
    """
    Represents a Car object with attributes: make, model, year.
    """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """
        Prints the car's information.
        """
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")

if __name__ == "__main__":
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    try:
        year = int(input("Enter car year: "))
        car = Car(make, model, year)
        car.display_info()
    except ValueError:
        print("Invalid input for year. It must be an integer.")
