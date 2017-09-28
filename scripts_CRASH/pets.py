## function is defined with 2 two parameters
# @param type of animal 
# @param pet's name
# function definition takes two parameters  
#def describe_pet(animal_type, pet_name):
def describe_pet(pet_name, animal_type='dog'):
    # docstring provides information 
    """Display informatin about a pet"""
    
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# call function with two positional arguments
# arguments are stored in the parameters
describe_pet(pet_name='harry', animal_type='hamster')
#describe_pet(animal_type='cat',pet_name='harry')
#describe_pet(pet_name='ronald',animal_type='snake')
#describe_pet(pet_name='charles')
#describe_pet('dog', 'chuck') # mult-function call example
#describe_pet('willie')
describe_pet('Troy','turtle')
