#@param def of function takes two parameters 
#@return outputs neatly formatted name of a person
#def get_formatted_name(first_name, last_name):
# take optional arg
def get_formatted_name(first_name, last_name, middle_name=''): # optional arg
    """Return a full name, neatly formatted"""
    # conditional happens only if optional argument is non empty string.
    if middle_name: 
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
