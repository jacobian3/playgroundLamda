# Exercise 8: Printing, Printing 
formatter = "%r %r %r %r" # assigns strings containing 'formatter' to variable:
# formatter

# prints the contents of the parenthesis for the string assignment to the var
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
# prints the formatter contents as empty formatter string 4x
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
    )
