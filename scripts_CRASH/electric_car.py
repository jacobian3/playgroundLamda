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

