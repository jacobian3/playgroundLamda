class Dog():
    """ A simple attempt to model a dog."""

    def __init__(self, name, age):
        """ Initialize name and age attributes. """
        self.name = name
        self.age = age

    def sit(self):
        """ Simulate a dog sitting in response to a command. """
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """ Simulate a dog rolling over in response to a command. """
        print(self.name.title() + " rolled over.")


def main():
    """ Execute commands for the class """
    my_dog = Dog('willie', 6)

    print("My dog's name is " + my_dog.name.title() + ".")
    print("My dog is " + str(my_dog.age) + " years old.")

if __name__ == "__main__":
    main()
