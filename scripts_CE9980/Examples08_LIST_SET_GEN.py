## LIST EXAMPLE: LIST TO CREATE LETTER, NUMBER PAIRS USING FOR LOOPS
#
#my_list = []
#for letter in 'abcd':
#    for number in '0123':
#        my_list.append((letter,number))
#print(my_list)


#S6P1;(07:11) SORTING
# sorted() takes an 'iterable' and returns a list
# a dict passed to sorted() returns a list of its keys
# default sorting is done numerically or lexicographically

#S6P2;(37:18) THE WAY COMPLEX SORTING WORKS:
# 1. We pass an iterable (list, dict, etc.) as arg to sorted()
# 2. We specify a 'sort function' with the key= parameter
# 3. sorted() sends each item as argument to the function
# 4. the value that coms back from the function is the value
#   by which that item will be sorted

#S6P3:(19:03) STEPS TO SORTING
# 1. what is an item to be sorted?
# 2. what value would you like that item to be sorted by?
# 3. can you write a function that takes one item and returns the 'by' value?

#S6P3; () MULTIDIMENSIONAL STRUCURES: LIST OF LIST
# similar to Excel spreadsheet

#S7P2:(2:10) QUESTION/STEPS TO COMPLEX SORTING
# 1. what is one item to be sorted?
# ... this will be the arg to your sort function
# 2. what is the value by which that item shoud be sorted?
# ... this will be the return value from your sort function
# 3. can you write a function that takes the one item and returns the value
# by which you'd like it sorted
