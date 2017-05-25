#=======================================New Topic==============================
#ADVANCED CONTAINER PROCESSING
# we are always looking at data in 1 of 2 ways (excluding binary!)
# 1. tabular data(row/column: excel sheet), 2. nested data (flexible)
# to converst column/row -> nested dictionaries, think of each key as a row
# ADVANCED TOOLS: SET OPERATIONS, LIST COMPREHENSIONS, LAMDA FUNCTION, TERNARY
# ASSIGNMENTS

##SET COMPARISON
#a = set('a b c'.split())
#b = set('b c d'.split())

## the set of all elements a that are not in b: A - B
#print(a.difference(b))
## the set of all elements b that are not in a: B - A
#print(b.difference(a))

## the set of all elements in a, in b or a and b is the union
## all the elements
#print(a.union(b))
#
## the set of all elements in common between a and b
#print(a.intersection(b))

#TERNARY ASSIGNMENT ??
#CONDITIONAL ASSIGNMENT ??

## LIST COMPREHENSION: FILTERING A CONTAINER'S ELEMENTS
## (list comp. loops through any iterable)
## iterable = any object that can be looped or iterated through
# pros: automatically build new list and return them when looping is done
# pros: can reduce a complex structue to a simple one-liner
# pros: easier and quick to read
# this is pseudo code:
# target list = item for item in source list if test
# three types: transforming a containers elements,
# filtering list, and combination of the two

##LIST COMPREHENSIONS: FILTERING A CONTAINERS ELEMENTS
## traditional filtering method:
#myints = [0, -1, -5, 7, -33, 18, 19, 55, -100]
##myposints = []
##for el in myints:
##    if el > 0:
##        myposints.append(el) # all pos ints
##
##print(myposints)
#
## filter with list comprehension method:
## no empty list init, no append method
#myposints = [el for el in myints if el > 0] #LC's auto-build a new list
#
#print(myposints)

##LIST COMPREHENSIONS: TRANSFORMING A CONTAINERS CONTENTS
##traditional transformation method:
#nums = [1, 2, 3, 4, 5]
#dblunms = []
#for val in nums:
#    dblunms.append(val*2)
#
#print(dblunms)
#
## filter with list comprehension method:
## tranforms ea. item in sorce list b/4 send to target list
#dblunms = [val*2 for val in nums]
#print(dblunms)

# common uses: strip lines, startswith

#LIST COMPREHENSIONS W/ DICTIONARIES
# dictionaries can be expressed as 2 item tuples!!; convert with items()

## conversion below is very useful for transforming and filtering dictionaries
#mydict = dict(zip(('a b c d e').split(),[5, 0, -3, 2, 1, 4]))
#mydict['f'] = 4
#
#my_items = list(mydict.items())
#print(my_items)
#print(dict(my_items))

#mydict = dict(zip(('a b c d e f').split(),[5, 0, -3, 2, -22, 4]))

## this will switch (in place) key/val pair as list then reassing to a dict
#filtered_dict = dict([ (j, i) for (i, j) in list(mydict.items()) ])


## Python databse module returns results as tuples; we can filter out values 
## using list comprehentions
## simulate a database return:
#tuple_db_result = [
#        ('joe',22,'clerk'),
#        ('pete',34,'salseman'),
#        ('mary',25,'manager')
#]
#
#names_jobs = dict([ (name, role) for name, age, role in tuple_db_result])
#print(names_jobs)

## LIST COMPREHENSION EXAMPLE (NESTED FOR STRUCTURE)
#
#mylist = [ (letter,number) for letter in 'abcd' for number in range(4) ]
#print(mylist)

## SET EXAMPLE
#
## set is like a list (has only unique values)
#nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
## notation to create empty set
#my_set = set() 
#for n in nums:
#    my_set.add(n) # 'add()' is used with sets b/c sets are immutable
#
#print(my_set)

## SET COMPREHENSION EXAMPLE
#
#nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
## set comprehensions: has braces(just like dic comp; but no ':')
## set comprehension can take filters and nested loops!
#my_set = {n for n in nums}
#print(my_set)

# NESTED COMPREHENSION EXAMPLE
#??


## EXAMPLE GENERATOR EXPRESSION (VERY SIMILAR TO LIST COMPREHENSIONS)
## NOTE:1st example:generator function the following is a generator expression.


## SIMPLE GENERATOR EXAMPLE
##
## You can iterate over a generator. However, values only produced as needed
## READ: 'I want to yield 'n*n' for each 'n' in nums
## Advantage: processes each element and waits for next request; this is more 
## efficient in memory and speed.
## 
#nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
##this creates set comprehension, to get rid of duplicates
#nums = {n for n in nums}
#print(nums)
#
#def gen_func(nums):
#    for n in nums:
#        yield n*n
#
#my_gen = gen_func(nums)
#
#for i in my_gen:
#    print(i)

## GENERATOR EXPRESSION EXAMPLE
#
##list items not important to example!
#nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
#
## This creates set comprehension, 
## This is to get rid of duplicates
#nums = {n for n in nums} #uses braces to denote set coprehension
#
## the use of parenthesis assignment denotes generator comprehension
#my_gen = (n*n for n in nums)
#print(nums)

#=======================================New Topic===============================

# SORTING MULTIDIMENTIONAL STRUCTURES
# (s7p2,5:00)Questions/Steps to complex sorting:
# 1. what is one item to be sorted?
# ... this will be the arg to your sort function
# 2. what is the value by which that item should be sorted?
# ... this will be the return value from your sort function
# 3. can you write a function that takes the one item and returns
# the value by which you'd like it?????
# 
##EXAMPLE: how to think about sorting by last name
# 1. what is one item to be sorted? 
# A: a string
# 2. what is the value by which that item should be sorted?
# A: the last name; how do you arrive at that? 
# A: see custom sort function below
# mylist = ['David B', 'Joe Wilson']
# 
# 3. can you write a function that takes the one item and returns
# the value by which you'd like it?????
# A: see custom sort function below
# def bylastname(name):
#     names = name.split()
#     return names[1]

#SORTING DICTIONARY ITEMS BY VALUE: OPERATOR.ITEMGETTER
#render dict as list of tuples with dict.items()method
#import operator
#mydict = dict( zip( 'a b c z'.split(), [5, 2, 1, 0] ) )
#
#mydict_items = list( mydict.items() ) # turns it back into a tuple


# SORTING MULTIDIMENTIONAL STRUCTURES: SORT W/ CUSTOM FUNCTION
# for each structure, print out the first (and last) name
# start with students2, then students3, then students1 (hardest)
# next, sort the structues by last name
# AGAIN: start with students2, then students3, then students1 (hardest)

## students1: dict of dicts 
## THINK: 1st get key(ans: #1 question below), 
## 2nd get dict to use with key, 3rd use subscript key to 
## get inner value (ans: #2nd question)
#
#students1 = {
#        'jw3': {'fname': 'Joe', 'lname':'Wilson'},
#        'ma2': {'fname': 'Mike', 'lname':'Apple'},
#        'mx99': {'fname': 'Marie', 'lname':'Xander'}
#}
#
#def bylastname(dict_key):
#    #1. the item to be sorted is a dictionary-key(a string);
#    #THINK: dict that belongs 2 key = student1
#    # students1 is a dict, therefore ea. any use of the dict. uses this keys
#    # remember: looping of a dict is done through use of its 'keys'!
#    #2. value by which item is sorted is the lname string value
#    #3. return item value:the string of the return value
#    return students1[dict_key]['lname'] #nested dict
#
## invisible: sorted will take an iterable (students1 dict), loop through:
## students1's keys. it will assign ea. key as 'bylastname's' arg & ret. 1 val
## sorted (not bylastname) will return that list of keys; bylastname only will
## return an individual value
#sorted_students = sorted(students1, key=bylastname)
#
#
#for idkey in sorted_students: # list of idkeys
#    print(students1[idkey]['fname'])
#    print(students1[idkey]['lname'])


## students2: list of list
#students2 = [  
#        ['jw3','Joe','Wilson'],
#        ['ma2','Mike','Apple'],
#        ['mx99','Marie','Xander']
#]
#
#def bylastname(string_item): #1. one item to be sorted by is a list
#    #2. value by which item is sorted is the last name (3rd value in list)
#    # can't use split b/c typeError. therefore multi-item assign to get value
#    # for lname; also could use: lname_val = students2[2] # subscript method
#    id1, fname, lname_val = string_item # multi-item assignment method
#    #3. return item value
#    return lname_val
#
#sorted_students = sorted(students2, key=bylastname)
#
#for item in sorted_students:
#    print("fname: {}, lname: {}".format(item[1],item[2]))


## students3: list of dicts
#students3 = [
#        {'id':'jw3', 'fname':'Joe', 'lname':'Wilson'},
#        {'id':'ma2', 'fname':'Mike', 'lname':'Apple'},
#        {'id':'mx99', 'fname':'Marie', 'lname':'Xander'}
#]
#
#def bylastname(dict_item): #1. the one item to be sorted by is a dictionary
#    #2. value by which item is sorted is the lname value
#    #3. return item value (the object attacted to the name)
#    return dict_item['lname']
#
#sorted_students = sorted(students3, key=bylastname)
#
#for itemdict in sorted_students:
#   print(itemdict['fname']) 
#   print(itemdict['lname']) 



#=======================================New Topic==============================

# SORTING MULTIDIMENTIONAL STRUCTURES: SORTING W/ LAMDA CUSTOM FUNCTION
#LAMDA EXPRESSION: BREAKDOWN

#=======================================Summary================================
# ADVANCED CONTAINER PROCESSING COSIST OF: 
#   set operations, list comprehensions, lambda functions, ternary assignments
#   and conditional assignment

# SET COMPARISONS: compares sets using union, difference, and interseciton
#a = set('a b c'.split())
#b = set('b c d'.split())

## the set of all elements a that are not in b: A - B
#print(a.difference(b))
## the set of all elements b that are not in a: B - A
#print(b.difference(a))

## the set of all elements in a, in b or a and b is the union
## all the elements
#print(a.union(b))
#
## the set of all elements in common between a and b
#print(a.intersection(b))
# LIST COMPREHENSIONS: filter a container's elements and reduces the sized of 
# code needed to do this
# LIST COMPREHENSIONS: transforming a container's elements
# LIST COMPREHENSIONS WITH DICTIONARIES
#   dict -> list of 2-element tuples using items()
#   list -> dict using dict()

# SORTING MULTIDIMENSIONAL STRUCTURES
#     Normal dict sort: sort dict keys by value:
#     dict.get => sort calls w/key=; get returns assoc. value
#     (we use keys to get values)

#     # When we loop through a dict, we can loop through a list of (keys) or 
#     # loop through (items):a list of key,value tuple pairs

# SORTING DICTIONARY ITEMS BY VALUE: OPERATOR.ITEMGETTER
# CONVERT DICT -> TUPLE
# 1. import operator module
# 2. use list, dict, items to: dict=> tuple
# 3. sort 2-item tuple by 2nd element: operator.itemgetter()
# 4. loop through tuple:(both:key, val)

# MULTI-DIMENSIONAL STRUCTURES: SORTING WITH CUSTOM FUNCTION
# similar to itemgetter(), use of inner value to sort; However, we access the
# inner value by use of custom function
# 1. define custom sort funciton to extract innermost value
# 2. use sorted wtth key = <cust fuction name>

# NOTE: ALT CUSTOM SORT METHOD
#     *** <mydict>.sort(key=<custom function>) # sort method(not sorted method)

# MULTI-DIMENSIONAL STRUCTURES: SORTING WITH LAMBDA CUSTOM FUNCTION
#lambda: function in a single statement;no seperate custom function declaration

## lambda thought process
#def addthese( x, y):
#    return x + y
## is equivalent to:
#addthese2 = lambda x, y: x + y
#print(addthese2(2,2)) # In this way the lambda function is:
## anonymous: not identified by name.

# pros: because used where defined -> less maintenance
# behaves just like reg function
# most common use: sorting;format:   arg : return_val 

# LAMBDA EXPRESSION EXAMPLE: DICT.GET AND OPERATOR.ITEMGETTER

## standard methods of sorting: by value 
#import operator
#mydict = {'a': 5, 'b':2, 'c': 1, 'z': 0}
#for key, val in sorted(list(mydict.items()), key=operator.itemgetter(1)):
#    print("{0} = {1}".format(key, val))

## standard methods of sorting: by key and get()
#for key in sorted(mydict, key=mydict.get):
#    print("{0} = {1}".format(key, mydict[key]))

## imagine no access to dict.get or operator.itemgetter
## we would use lambda method sort: by value
## lambda takes a two-element tuple as an argument and return 2nd element
#for key, val in sorted(list(mydict.items()), key=lambda keyval: keyval[1]):
#    print("{0} = {1}".format(key, val))

## lambda takes a key as an argument and returns the assoc. value
#for key in sorted(mydict, key=lambda key: mydict[key]):
#    print("{0} = {1}".format(key, mydict[key]))
