from ex9_8privileges import Users # has all 3 inc. classes
from ex9_11imported_admin import Admin, Privileges # imports 2 from 3 imported

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

    
    trex = Admin('Trex','Higram',bldg='A402',computer='Apple')
    trex.greet_user()
    trex.describe_user()
    trex.privileges.privileges = ['can add post', 'can delete post']
    trex.privileges.show_privileges()
