class Car():
    """A set of classes to represent gas and electic cars."""

    def __init__(self, make, model, year):
        """ Initialize attributes to describe a car. """
        self.make = make # store parameters in instance name space
        self.model = model # instance namespace => attributes
        self.year = year
        self.odometer_reading = 0 # set odometer in attribute so no parameter

    def get_descriptive_name(self):
        """ Return a neatly formatted descriptive name. """
        # store attributes values in a variable for convenience
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()

    def read_odometer(self):
        """ Print a statement showing the car's mileage."""
        # make it easy to read by using a function to repeat task, when needed
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """ 
        Set the odometer reading to the given value.
        Reject the change, if it attempts to roll the odometer back. 
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """ Add the given amount to the odometer reading. """
        self.odometer_reading += miles

class ElectricCar(Car):
    """ Represent aspects of a car, specific to electric vehicles."""
    # Initialize the new class and accept parameters passed from the intance
    # Initialize all new attibutes of child class
    def __init__(self, make, model, year):
        """ 
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car
        """
        # connect the parrent class to the child class and access all attribute
        # data
        super().__init__(make, model, year)
        # add new attributes to differentiate parent child relationship
        self.battery = Battery() # call Battery class to get battery
        # information
        # or said another way: create an instance of the Batery class and set 
        # self to 'battery'

class Battery():
    """A simple attempt to model a battery. """
    # set default battery to 70 to facilitate later function calls out of class
    def __init__(self, battery_size=70):
        """ Initialize battery attributes. """
        self.battery_size = battery_size

    def describe_battery(self):
        """ Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """ Print a statement about the range of of this battery."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

