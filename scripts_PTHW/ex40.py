# Exercise 40: Modules, Classes, and Objects
# (1)Python looks through Song() to understand the class definition
# class X that has-a __init__ that takes self and lyrics parameters
# class X has-a function named sing_me_a_song that takes self parameters
# this step creates a container for the functions to exist and be called
# (2) python uses __init__ to create an empty object with all the functions
# (3) python checks for the existance of the __init__ function and if it 
# exist, Python initializes the new empty object
class Song(object):
    # within the fuctions inside of a class...
    # self is a variable for the instance or object being accessed
    # using self in this way, self acts like a module or dictionary
    # we can then set instance variables on it, much in the same way as we do
    # a module. This allows a substitution relationship between the instance of
    # the class instance (i.e., happy_bday) and self: 
    # (4)In the Song function __init__ I then get this extra variable self, 
    # which is that empty object Python made for me, and I can set variables 
    # on it just like you would with a module, dictionary, or other object.
    def __init__(self, lyrics):
        self.lyrics = lyrics # (5) initialize the empty object by setting 
        # self.lyrics to the lyrics argument in the function definition.

    # The function loops through the list: self.lyrics & prnts
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

# this is instansiation.
# happy_bday = Song(object) acts as similar to an import statement 
# An instance of the class is created that contains a
# arg. The Song class takes this list argument, intitiates the class Song, and
# creates a new instance of the class; assigned to a var. object.
# (6) Now Python can take this newly minted object (the list) and assign it to 
# the variable: happy_bday, for me to work with.
happy_bday = Song([ "Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

# create a class by calling the Class Song 'blueprint'
# the argument is initialized insied of the new class instance 
# and is made available for use.
# (6) Now Python can take this newly minted object (the list) and assign it to 
# the variable: happy_bday.
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

# from happy_bday get the sing_me_a_song function
# and call it with self and lyrics parmeters.
happy_bday.sing_me_a_song()
print "*" * 20
# the dot operator get access to the function inside of the class instance
# all functions have been initialized and have access to all instance vars
# the __init__ function creates a module like object that imports all instance
# variables: i.e., self.lyrics, etc. using the self namespace?
# sing_me_a_song funtion loops through the lyrics of the previouly initialized
# class object. Ths prints each item of the list argument
bulls_on_parade.sing_me_a_song()
