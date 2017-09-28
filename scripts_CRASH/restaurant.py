class Restaurant():
    def __init__(self, name, cuisine):
        """initialize the restaurant's attributes """
        self.restaurant_name = name
        self.cuisine_type = cuisine
    
    def describe_restaurant(self):
        """print a statement describing the restaurant"""

        print("This restaurant is named " + self.restaurant_name)
        print(self.restaurant_name.title() + "'s best meal is " + \
self.cuisine_type.title() + \
                ".")

fav_joint = Restaurant('Chick-fil-A','chick-burger')
fav_joint.describe_restaurant()
