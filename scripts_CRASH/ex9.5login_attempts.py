class Users():
    """ prints a summary of user information. """
    def __init__(self, fname, lname, **additional):
        "Initialize parameters first and last name. """
        self.profile = {}
        self.profile['First_name'] = fname.title()
        self.profile['Last_name'] = lname.title()
        self.login_attempts = 0
        for key, value in additional.items():
            self.profile[key.title()] = value.title()
        
    def describe_user(self):
        #print("\nBelow is dictionary dump of all user info.")
        print(self.profile)

    def greet_user(self):
        print("\nHello {} {}".format(self.profile['First_name'], 
            self.profile['Last_name']))
        print("your information is displayed below:")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

if __name__ == '__main__':

    # instance 1
    user_profile = Users('albert', 'einstein',
                                location='prinston',
                                field='physics')
    user_profile.greet_user()
    user_profile.describe_user()
    
    # instance 2
    user2 = Users('tom','williams',
                address='2259 Warten Rd.',
                auto='Audi')
    user2.greet_user()
    user2.describe_user()


    # instance 3
    userX = Users('john', 'doe',
                address='1234 rockbrior pl.',
                num_cats='3')
    userX.greet_user()
    userX.describe_user()

    # attempt repeated logins to examine incrementer with instance 3
    userX.increment_login_attempts() # 1st attempt
    print("User attempted login: {} time(s)".format(userX.login_attempts))
    userX.increment_login_attempts() # 2st attempt
    print("User attempted login: {} time(s)".format(userX.login_attempts))
    userX.increment_login_attempts() # 3st attempt
    print("User attempted login: {} time(s)".format(userX.login_attempts))

    # reset login_attempts
    userX.reset_login_attempts()
    print("\nUser attempted login: {} time(s)".format(userX.login_attempts))
    
