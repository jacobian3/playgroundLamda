#S6P1:(07:11) SORTING
# sorted() takes an 'iterable' and returns a list
# a dict passed to sorted() returns a list of its keys
# default sorting is done numerically or lexicographically

# WHAT IS COMPLEX SORTING?
# sort val by some other criteria
# in particular we do it by use of an item-criteria function: returns a value
# by which a given element can be sorted

## CUSTOM SORTING USING AN ITEM-CRITERIA FUNCITON
## an item-criteria function returns to python the value by which a given 
## element should be sorted 
#
#def by_value(dict_key): # a key to be sorted  (for ex. 'mike')
#    dict_value = bowling_scores[dict_key] #retrieve value based on 'mike':202
#    return dict_value # return the value 202
#
#bowling_scores = {'jeb':123, 'zeb':98, 'mike':202, 'janice':184}
#sorted_keys = sorted(bowling_scores, key=by_value) # get not needed because
## get returns a value for a key; our function has a 'return' value
## methods work the same way: ( see next summary task )
#
#print(sorted_keys,"\n")
#
#for player in sorted_keys: # 'player' is an item in a list! not a dict!!
#    print("{} scored {}".format(player, bowling_scores[player]))    


# HOW DO WE SORT A STRING BY A PORTION OF THE STRING?
# we split the string and return a portion
# this can be aided by using a multi-target assignment of the list

#WHAT IS A MULTI-TARGET ASSIGNMENT?
# assign vlaue in a list to individual variable names 
# example:   items = line.split()
#            name, revenue, state = line

## SORTING A NUMBERIC STRING BY ITS VALUE
## use item-criteria function to do conversion
#
## easy way to type a list from string
#numbers_from_file = '1 10 3 20 110 1000'.split()
#
#def by_numeric_value(this_string): # item-criteria funciton used
#    return int(this_string)
#
#sorted_numbers = sorted(numbers_from_file, key=by_numeric_value)
#
#print(sorted_numbers)


## SUMMARY TASK: SORT A FILE LINE BY A FIELD WITHIN THE LINE
## good for cvs files; sorts a string of fields by a field within the line
#
#import pprint # allows pretty print of list stdout
#
#def by_third_filed(this_line):
#    # book method
#    #els = this_line.split(',')
#    #return els[2]
#    
#    # alt method: mult-target assignment = more flexability!!
#    id1, fname, lname, city, state, lgnum = this_line.split(',') 
#    return city
#
#lines = open('../script_data/students.txt')
#sorted_lines = sorted(lines, key=by_third_filed)
#pprint.pprint(sorted_lines)


##WHAT IS A CASCADING SORT?
## sort list by multiple criteria by haing furnciton return a 2-element tuple
## AKA: MULTI-CRITERIA SORT
##
## def by_last_first(name)
## given: open file handle THEN
##   name = name.split()
##   fname, lname = name.split()
##   return (lname, fname) 
#
## Example of cascading sort
#def by_last_first(name):
#    fname, lname = name.split()
#    return (lname, fname) # will search by last name then by first
#
#names = ['Zeb Will', 'Deb Will', 'Joe Max', 'Ada Max']
#
#lnamesorted = sorted(names, key=by_last_first)
#print(lnamesorted)

#S6P3:(9:40) DISCUSS SORTING, 'INVISIBILITY' AND CUSTOM FUNCTIONS ?
# the function is dealing with one item (and not each item)
# therefore no loops in the function are needed; looping takes place inside the
# sorted function. INISIBLITY: the cust funciton is is gettting called 
# by sorted() (implict loop)

#S6P3:(19:03) STEPS TO SORTING (CUSTOM)
# 1. what is an item to be sorted?
# 2. what value would you like that item to be sorted by?
# 3. can you write a function that takes one item and returns the 'by' value?

#S6P3:(37:18) THE WAY COMPLEX SORTING WORKS:
# 1. We pass an iterable (list, dict, etc.) as arg to sorted()
# 2. We specify a 'sort function' with the key= parameter
# 3. sorted() sends each item as argument to the function
# 4. the value that coms back from the function is the value
#   by which that item will be sorted

#S7P2:(2:10) QUESTION/STEPS TO COMPLEX SORTING
# 1. what is one item to be sorted?
# ... this will be the arg to your sort function
# 2. what is the value by which that item shoud be sorted?
# ... this will be the return value from your sort function
# 3. can you write a function that takes the one item and returns the value
# by which you'd like it sorted

## SORTING A DICTIONARIES KEYS BY VALUES(EXAMPLE):
#bowling_scores = {'jeb':123, 'zeb':98, 'mike':202, 'janice':184}
## sorted takes a sequence and returns a list
#sorted_keys = sorted(bowling_scores, key=bowling_scores.get)
#
#print(sorted_keys,"\n")
#
#for player in sorted_keys: # 'player' is an item in a list! not a dict!!
#    print("{} scored {}".format(player, bowling_scores[player]))    

# NOTE: USING METHODS AND IN PARTICULAR GET 
# AKA: REFERING TO METHODS IN THE ABSTRACT
# the key value can be a appropriate method call using the dot opeator
# wihtout the parenthesis; as they are called iniside of the sorted function.
# example: key=str.lower  is ok and similar to key=companydict.get
# we are refering to methods lower and get in the abstract; no call made

#S6P3:(24:46) MULTIDIMENSIONAL STRUCURES:
# all accessed w/ looping using indexed subscripts
# THERE ARE 5 TYPES OF MULTIDIMINSIONAL CONTAINERS CASES:
# LIST OF LIST, LIST OF DICTS, DICT OF LIST, DICT OF DICTS, ARBITRARY DIMENSION
#
# SUMMARY STRUCTURE: LIST OF LISTS
# pros: provides a matrix similar to Excel spreadsheet
# ea. item is a list each list represents a row of data


## SUMMARY STRUCTURE: LIST OF DICTS
## ea. key represents a field/attribute/collumn with values being row entities
## pros]: easier navigation by use of named subscripts vs numbered subscripts

## SUMMARY STRUCTURE: DICT OF LISTS
## associates unique keys with a sequence of values
## pros: facilitates calculation of elements max, min, sum, len, etc..
#
## EXAMPLE: looping a complex structure (list of list)
#value_table =   [
#                    ['19260701', 0.09, -0.22, -0.30, 0.009],
#                    ['19260702', 0.44, -0.22, -0.08, 0.009], 
#                    ['19260703', 0.17, -0.26, -0.37, 0.009] 
#                ]
#
#for row in value_table:
#    print("MKtRF for {} is {}".format(row[0], row[1]))


## SUMMARY STRUCTURE: DICT OF DICTS
## unique key with another key/ value pair
## pros: allows convienient access via clear-visually-nexted structure
#
## EXAMPLE: looping a complex structure (dict of dict)
#date_values =   {
#        '19260701': {'MktRF': 0.09,
#                    'SMB': -0.22,
#                    'HML': -0.30,
#                    'RF': 0.009 },
#        '19260702': {'MktRF': 0.44,
#                    'SMB': -0.35,
#                    'HML': -0.08,
#                    'RF': 0.009 },
#}
#
#for this_date in date_values:
#    # book answer
#    print("MKtRF for {} is {}".format(this_date, date_values[this_date]['MktRF']))
#
#    # mechanics is similar to functional notation f o g (x)
#    # dict(dict(key)) => dict[key][key]
#    # we use a double subscript to get in
#    # outer dictionary call is to entire dict; then to the 2nd dict using an 
#    # inner key
#    # this returns the entire dict of dicts as values
#    #print("MKtRF for {} is {}".format(this_date, date_values[this_date]))


# SUMMARY STRUCTURE: ARBITRARY DIMENSIONS
# pros: allows 1 item to have easily accessable, infinitely complex clear-vis
# structure

# SUMMARY TASK: RETRIEVING AN "INNER" ELEMENT VALUE
# Nested subscripts are the usual way to travel "into" a nested 
# structure to obtain a value.  

# SUMMARY TASK: LOOPING THROUGH A COMPLEX STRUCTURE
# Looping through a nested structure often requires 
# an "inner" loop within an "outer" loop

# MULTIDIMENSIONAL STRUCTURES - BUILDING
#Usually, we don't initialize multi-dimensional structures within our code.  
#Sometimes one will come to us, as with dict.items(), which returns a list of 
#tuples.  Database results also come as a list of tuples.
