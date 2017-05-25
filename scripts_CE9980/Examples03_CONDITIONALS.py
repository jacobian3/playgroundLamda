## EXAMPLE OF WHILE LOOP PROCESS
#cc = 0  # 1st initialize counter
#
#while cc < 5: # 2nd if test is true, enter block
#    print(cc)
#    # 3rd increment cc; when we get to end of block, jump back to while
#    # test
#    cc += 1 

## 'IF' STATEMENT
#aa = input('please enter a positve integer: ')
#int_aa = int(aa)
#
#if int_aa < 0:  # test: is this a True statement?
#
#    print('error: input invalid')
#    exit(1)
#
#d_int_aa = int_aa * 2
#print('Your value doubled is ' + str(d_int_aa))


## EX. 1.7
#new_int1 = 2 # assignment
#new_int2 = 4
#float_object = 5.1
#
#total = new_int1 + new_int2 + float_object # sum of variables
#print(total) # type returns a type object
#print(type(total))

## EXAMPLE: OF THOUGHT PROCESS FOR WHILE TRUE INFINITE LOOP STRUCTURE
#counter = 0 # initialize counter for WHILE True loop
#while True: # infinite loop breaks when correct input standard in
#    max_count = input('Enter an int: ')
#    if max_count.isdigit(): # checks if the string value is numerical
#        break # 'T' continues to conversion of string to int
#    print('sorry, try again') # WRITE msg to user and jump back to test
#
#max_count = int(max_count)
#
#while counter < max_count:
#    print(counter)
#    counter = counter + 1

## EXAMPLE: SUMMARY ALGORITHM
#COUNT = 0
#TOTAL = 0
#
#fh = open('./script_data/FF_abbreviated.txt')
#for line in fh:
#    line = line.rstrip()
#    myline = float(line.split()[1])
#    print(myline)
#    COUNT += 1
#    TOTAL += myline
#
#print('There are:{} items. They total:{}.'\
#        'Their avg:{}'.format(COUNT, TOTAL, TOTAL / COUNT))
