# NOTE: the word Class is a synanym for word Type   


# ??? 5 key ideas of a class:?


# What is a constructor? @24:38
    # name of the class + partenthesis '()'
    # returns an object/instance of a class

# What is setter and getter methods?
    #

# What are the three pillars of object-oriented programming?
    # Encapsulation: data preserved behind the interface
    # Inheritance: 
    # Polymorphism:  
    
# What is an interface? @2:30
    # expected operators/functions that we can use an object => behavior

# What is a custom object? why is it important? How is it created?

# How do we add object to a class? (pykids, 96)
    # introduction of a spec. instance object, bound to a class, is called 
    # instansiation. i.e., reginald = Giraffes()
    # ANALOG: ATM ..just any machine b/4 card insert; afterwards it's your ATM,
    # with access to your account

# How do we define functions of a class? (pykids,97)
    # functions defined in a class, are the 'verbs.' they allow 
    # the instance objects to do smth.
    # to add a function to a class use 'def' keyword
    # 'def' replaces the pass keyword scaffolding
   
# are Class and module attribes the same? if not how not?
    #???

# What are class characteristics? How do we apply them? (pykids,97)
    # characteristic: trait shared by all members of 
    # the class (and its children)
    # characteristics: aka actions, or functions)
    # ea. class can use characteristics (functions) of its parent.

    # like mini-modules. you can make many individual imports that don't 
    # interfere with one-another. AKA: instantiation

    # Common pattern in PY: 1. key=val style continer. 2. get smth. out 
    # by the key's name. classes are like modules in this way. 
    # a module is a spec. dictionary (key/val pair)
    # accessed with the dot operator. A class: A container/ group of 
    # functions and data (attributes); accessed with the . (dot) operator
        # mystuff['apple'] # get apple value from dict
        # mystuff.apple() # get apple from module
        # mysturff.tangerine # get tangerine val from the module

    # we call functions of an object by using the dot operator and the name 
    # of the function.
    
# Explain the instaniation process: iclude def, __init__, and self? (PTHW,ex40)
    # 1. py looks for the user defined class def
    # 2. py crafts empty object with all function specified using def 
    # 3. py looks for 'magic' __init__ function, if True: it inits empty object
    # 4. __init__  makes empty object:self ; is2b bound 2 name like dict/module
    # 5.  arg assigned to attribute using self.<attribue name>
    # 'self' means the current object
    # 6. new instance name and self bound

# How do funcitons in one Class call a function from another class?(pykids,104)
    # self parameter is a way for one function in a class to call 
    # another function in that class (and the parent class)
    # functions in any parent class are available to its child classes


# CLASS EXAMPLE: THE DATE AND TIMEDELTA OBJECT TYPES
# (see example file)
# CLASS EXAMPLE: THE PROPOSED SERVER OBJECT TYPE
# (see example file)

# A CLASS BLOCK DEFINES AN OBJECT "FACTORY" WHICH PRODUCES 
# OBJECTS (INSTANCES) OF THE CLASS.
# Describe the concept of an object factory? How do method calls relate to
# functions in the class?
# How are the words class and type nearly synonomous?

# What is a class? 
    # a definition of an object type @ 23:20
    # it is a way to classify objects into groups.
    # it is also a way to define objects.
    # object are class members.
    # any number of objects can be defined in a class: using the class keyword
    # followed by a name.

# Describe child/parent analog to classes and parameters? (pykids, 95)
    # to tell python that a class is a child of another class, we add the name
    # of the parent class in parenthesis after the name of our new class
    # pass keyword says we will provide no more info on function; so move on
    # common practice: scaffold class outline using pass statements


    # 1. when we call a class (i.e. with parenthesis), it produces an object of
    # that class. the object knows that it belongs to that class

    # What is an object? ( 3 parts ) @48:10
    # object: 1.a unit of data(has its own) 2. of a particular type that has
    # 3. 'characteristic functionality'
    # aka: an instance of a class @23:20


# EACH OBJECT HOLDS AN ATTRIBUTE DICTIONARY
# How is data stored in an object? 

    # 2. every user-def object has its own attribute dictionary.this dictionary
    # is written to and read through object.attribute syntax
    #   obj.a = 5 # setting an attributes value
    #   z = obj.a # getting an attributes value
    #   obj.a = 5   # obj.__dict__['a'] = 5
    #   obj2.a = 100 # obj2.__dict__['a'] = 100

# THE CLASS ALSO HOLDS AN ATTRIBUTE DICTIONARY
# How is data stored in a class? 
# what attributes are automatically added? What do they do?

# OBJECT.ATTRIBUTE LOOKUP TRIES TO READ FROM OBJECT, THEN FROM CLASS
# If an attribute can't be found in an object, where is it is searched?

# METHOD CALLS PASS THE OBJECT AS FIRST (IMPLICIT) ARGUMENT, CALLED SELF
# Explain (object/instance)method, and self?

    # What is a method? @46:30
    # a specialized funciton: a function defined within a Class def.
    # it is a objec/type specific function
    # this is 'behvior'; something it can do
    # THIS IS CHARACTERISTIC FUNCTIONALITY!!!!!

# INSTANCE METHODS / OBJECT METHODS AND OBJECT ATTRIBUTES: CHANGING 
# OBJECT "STATE"
# How do we use (insance / object)methods to change an object's state?

    # 3. when we call a method on an object, the object itself is passed as the
    # first argument implicitly; this is how 'self' works!!!!

    # 4. 'self' in the method is the object upon which the method was called:
    # IF  x.this() # THEN IMPLICATION: def this(self): #THERFORE: 'self' is 'x'

# OBJECTS ARE OFTEN MODIFIED USING GETTER AND SETTER METHODS
# How are getter and setter methods used to modify object behavior?
# ???? not in notes or video

# __INIT__() IS AUTOMAGICALLY CALLED WHEN A NEW INSTANCE IS CREATED
# When is initializer method called?
# What does it allow us to do?
# Why whould and how do we initialize an object?
    # sometimes when creating an object, we want to set some values?
    # thes values are called 'properties'
    # properties are 'object variables': self pairs the object w/ the instance.
    # the __init__ argument pairs a value(the instnace's argument) with a name

    # 5. upon construction of a new object, if def__init__() is defined, it
    # will be called ('self' is the new object); otherwise not called
    # 'self' will become, at this moment, 'x'

# CLASSES CAN BE ORGANIZED INTO AN AN INHERITANCE TREE
# Explain the concept of an inheritance tree?

# CONCEPTUALLY SIMILAR METHODS CAN BE UNIFIED THROUGH POLYMORPHISM
# How do we unify similar methods?
