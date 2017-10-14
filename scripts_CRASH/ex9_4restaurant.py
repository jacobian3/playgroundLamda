class Restaurant():
    """ simple class to simulate a restaurant """
    
    def __init__(self, name, cuisine):
        """initialize the restaurant's attributes """
        self.restaurant_name = name.title()
        self.cuisine_type = cuisine
        self.number_served = 0
    
    def set_number_served(self, number):
        """ set the number of customers that have been served. """
        self.number_served = number

    def describe_restaurant(self):
        """print a statement describing the restaurant"""

        #print("\nThis restaurant is named " + self.restaurant_name)
        #print(self.restaurant_name.title() + "'s best meal are " + \
        #    self.cuisine_type.title() +  ".")
        msg = self.restaurant_name + " serves a wounderful " + \
                self.cuisine_type.title() + "."
        print("\n" + msg)

        num = "There are {} patrions being served.".format(self.number_served)
        print(num)

if __name__ == '__main__':

    fav_joint = Restaurant('Chick-fil-A','chick-burger')
    fav_joint.describe_restaurant()

    restaurant = Restaurant('applebees','dinner cuisine')
    restaurant.set_number_served(5)
    restaurant.describe_restaurant()
