from ex9_4restaurant import Restaurant

if __name__ == '__main__':

    fav_joint = Restaurant('Chick-fil-A','chick-burger')
    fav_joint.describe_restaurant()

    restaurant = Restaurant('applebees','dinner cuisine')
    restaurant.set_number_served(5)
    restaurant.describe_restaurant()
