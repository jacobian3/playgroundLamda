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

    def describe_battery(self):
        """ Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


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

def main():
    """ run function calls """
    my_tesla = ElectricCar('tesla','model s', 2016)
    print(my_tesla.get_descriptive_name())

    # call for battery size from Battery() instead of from function defined 
    # inside of ElectricCar()
    #my_tesla.describe_battery()
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()


if __name__ == "__main__": # gateway to module access
    main()

