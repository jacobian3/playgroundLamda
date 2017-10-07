class Car():
    """ A simple attempt to represent a car. """

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


