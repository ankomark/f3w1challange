class Car:
    """
    A class representing a car.
    
    Attributes:
    make (str): The manufacturer of the car.
    model (str): The model of the car.
    year (int): The year the car was manufactured.
    """
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        """
        This method prints out the car's information.
        """
        print(f"Car Information: {self.year} {self.make} {self.model}")
