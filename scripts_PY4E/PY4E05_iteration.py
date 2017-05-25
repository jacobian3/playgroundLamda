#exampleList = [1, 5, 6, 1, 6, 7, 8, 9, 345, 53, 5]
#
#for eachNumber in exampleList:
#    print(eachNumber)


##PT4E_iteration

##Summing a loop
#zork = 0 # initialize the varible for summation
#print('Before', zork) #print init var
#for thing in [9, 41, 12, 3, 74, 15]: #init 'thing' an iterate list values
#    zork = zork + thing #check Zork and add thing list item to zork as sum
#    print(zork, thing) #print new zork val. and curent thing value b4 next cy.
#print('After', zork)

##Avg in the loop
#count = 0
#sum1 = 0
#
#values = [9, 41, 12, 3, 74, 15]
#print('Before', count, sum1)
#for value in values:
#    count += 1
#    sum1 += value
#    print('count:',count,'val:', value,'sum:', sum1)
#print("After", count, sum1, sum1 / count )

##Filtering in a loop
#print('Before') # entry point
#for value in values : #for each value the list of values, init:value to list
#    if value > 20: # print only numbers greater than 20
#        print('Large number', value) #nums > 20
#print('After')# exit point

##while loop example
#n = 5 # initialize iteration variable
#while n > 0: #evaluate the condition;if F exit the body of the loop
#    print(n) # k
#    n = n - 1 # will cycle for 5 iterations for countdown to zero
#print('Blastoff!')

##Infinite loop example
#n = 10
#while True:
#    print(n, end = " ")
#    n = n - 1 #iteration variable to count to infinity; no mechanism escape
#print('Done')

##break example
#while True:
#    line = input('> ')
#    if line == 'done':
#        break
#    print(line)
#print("Done")

##continue example
#while True:
#    line = input('> ')
#    if line[0] == '#':
#        continue
#    if line == 'done':
#        break
#    print(line)
#print('Done!')


##definite loops
#friends = ['Joseph', 'Glenn', 'Sally'] #list 
#for friend in friends: #loop through list and init var to loop elements
#    print('Happy New Year:', friend)
#print('Done!')
