class Restaurant():
    def __init__(self, name, cuisine):
        """initialize the restaurant's attributes """
        self.restaurant_name = name
        self.cuisine_type = cuisine
    
    def describe_restaurant(self):
        """print a statement describing the restaurant"""

        print("\nThis restaurant is named " + self.restaurant_name)
        print(self.restaurant_name.title() + "'s best meal are " + \
            self.cuisine_type.title() +  ".")

if __name__ == '__main__':
    fav_joint = Restaurant('Chick-fil-A','chick-burger')
    fav_joint.describe_restaurant()
