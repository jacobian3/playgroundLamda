from car import Car

my_new_car = Car('Audi','a5',2006)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 25
my_new_car.read_odometer()
