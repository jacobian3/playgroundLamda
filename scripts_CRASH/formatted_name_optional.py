#@param def of function takes two parameters 
#@return outputs neatly formatted name of a person
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + last_name

    return full_name.title()

musician = get_formatted_name('jimi','hendrix')

print(musician)

print(get_formatted_name('troy','sanders','tiki'))
print(get_formatted_name('troy','sanders'))
