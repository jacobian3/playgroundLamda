# false values include: False, None, 0 and []
def hello(name=None): # STEP 1: name = None => False condition; no name given 
    # It states that if there no name is True, THEN execute
    if not name: # -> True condition; must be true to activeate
        name = 'world!'
    print('hello, {}'.format(name))
