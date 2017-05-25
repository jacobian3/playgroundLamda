# Exercise 14: Prompting and Passing
# *** this script accepts arguments ***
# import adds the system library to the script
# argv holds the arguments passed to the script at runtime
from sys import argv

script, user_name = argv # argv unpacts the arguments into the assigned vars
prompt = "> " # assignment

# prints string containing mulitple formatters
print "Hi %s, I'm the %s script." % (user_name, script) 
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt) # reads standard input; makes assignment

print "Where do you live %s?" % user_name
lives = raw_input(prompt) # reads standard input; makes assignment

print "What kind of computer do you have?"
computer = raw_input(prompt) # reads standard input; makes assignment


print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
