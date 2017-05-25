# Exercise 24: More Practice
print "Let's practice everything."
print """You\'d need to know \'bout escapes with \\""" + """that do\n newlines and \t tabs.
""" # I got this to work in a funky way; return later to examine

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires and explanation
\n\t\twhere there is none.
""" # the last '\n' character prints 2; not one new line other is implicit

print "-" * 15 # prints the line
print poem
print "-" * 15 # prints the line


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 1000

# function secret_formula unpacts vars
beans, jars, crates = secret_formula(start_point) 

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)
