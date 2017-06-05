# SUMMARY ALGORITM (STEPS)
# What is the Summary algorithm? How to implement steps?
    # allows parsing of tabular structures

fh = open('F-F_abbreviated.txt') # 1. open and assign file handle

mysum = 0.0 # 2. initialize float value
for line in fh:
    line = line.rstrip() # 3. remove newline
    items = line.split() # 4. remove header information
    mysum = mysum + float(val)
print(mynum)


# COLLECITONS AND ANALYSIS 

#var = [1, 4.3, 6.9, 11, 15]
#
#print('median is {}'.format(var[2]))
#
#print('top 2: {}'.format(var[-2:]))
#
#print('max val is {} '.format(min(var)))
#
#print('max val is {} '.format(max(var)))
#
#print('average is {}'.format(sum(var) / len(var)))
#
#print('sum is {}    '.format(sum(var)))
#
#print('count is {}  '.format(len(var)))


## COLLECTIONS OF VALUES TO DETERMINE MEMBERSHIP
#
#valid_actions = 'run stop search rest'.split() 
#
#u_input = input('please enter an action: ')
#
#if u_input in valid_actions:
#    print('great, I will "{}". '.format(u_input))
#else:
#    print('sorry, action not found')

#  SUMMARY OF CONTAINERS

#var2 = [1, 2, 3, 'a', 'b']
#
#var2.append(4) 
#print(var2)
#
#mylist = var2
#
#sublist = mylist[3]
#print(sublist)

# SUMMARY LOOP A LIST

#myList = [1, 2, 3, 'a', 'b']

#for item in myList:
#    print(item,end=" ")

#mylist = [4, 9, 1.2, -5, 200, 20]
#smyl = sorted(mylist) # sorted method takes an argument list
#print(smyl)


# SUMMARY FOR OBJECT: 'SET'

#myset = () #initialize an empty set

#myset = {'a', 9999, 4.3}
#myset.add(4.3) # can't be assigned b/c it's not unique
#myset.add('a5')
#print(myset)

#print( len(myset) )

#membership test
#if 'a' in myset:
#    print("'a' is in myset\n")
#
#for item in myset:
#    print(item)

## PRACTICAL EXAMPLE 1

#state_list = [] # init empty list
#for line in open('../script_data/student_db.txt'): # open and iterate contents
#
#        elements = line.split(':')
#        state_list.append(elements[3]) # add state name to list of names
#
#chosen_state = input("Enter state ID: ")
#state_freq = state_list.count(chosen_state) #counts instances of list occurance
#print('{} occurs {} times'.format(chosen_state, state_freq))

## PRACTICAL EXAMPLE 2
#
#state_set = set()
#for line in open('../script_data/student_db.txt'):
#    line = line.rstrip()
#    elements = line.split(':')
#    state_set.add(elements[3])
#
#chosen_state = input('enter a state ID:  ')
#
#if chosen_state in state_set:
#    print('that is a valid state')
#else:
#    print('that is not a valid state')

## PRACTICAL EXAMPLE 3

fh = open('../script_data/student_db.txt')
line = fh.readlines()
print(line)

wanted_lines = line[1:]
for element in wanted_lines:
    print(element.rstrip())
