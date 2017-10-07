from car import ElectricCar

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

