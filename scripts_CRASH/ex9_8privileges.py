class Users():
    """ prints a summary of user information. """
    def __init__(self, fname, lname, **additional):
        "Initialize parameters first and last name. """
        self.profile = {}
        self.profile['First_name'] = fname.title()
        self.profile['Last_name'] = lname.title()
        for key, value in additional.items():
            self.profile[key.title()] = value.title()
        
    def describe_user(self):
        print("\nBelow is dictionary dump of all user info.")
        print(self.profile)

    def greet_user(self):
        print("\nHello {} {}".format(self.profile['First_name'], 
            self.profile['Last_name']))


class Admin(Users):
    """ admin account for managing privileges """
    def __init__(self, fname, lname, **additional):
        """ init the Admin class """
        super().__init__(fname, lname, **additional)
        self.privileges = Privileges()


class Privileges():
    """ simple application to demonstrate setting an instance to a class """
    def __init__(self, privileges=[]):
        """ init the class """
        self.privileges = privileges

    def show_privileges(self):
        """ display privileges of the admin """
        for privilege in self.privileges:
            print("- " + privilege)

if __name__ == '__main__':
#    user_profile = Users('albert', 'einstein',
#                                location='prinston',
#                                field='physics')
#    user_profile.describe_user()
#    user_profile.greet_user()
#    
#    user2 = Users('tom','williams',
#                address='2259 Warten Rd.',
#                auto='Audi')
#    user2.describe_user()
#    user2.greet_user()

    # ex9_8 calls  #???
    trex = Admin('Trex','Higram',bldg='A402',computer='Apple')
    trex.greet_user()
    trex.describe_user()
    trex.privileges.privileges = ['can add post', 'can delete post']
    trex.privileges.show_privileges()
