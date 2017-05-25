i = 1
numbers = []

while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        # div test
        print "FizzBuzz: because", i,"is div by 3 and 5."
        numbers.append(i)
        
    elif i % 3 == 0:
        # div test
        print "Fizz: because", i,"is div by 3."
        #numbers.append(i)

    elif i % 5 == 0:
        # div test
        print "Buzz: because", i,"is div by 5."
        #numbers.append(i)

    else:
        # div test
        print "%r is not divisibile by 3 or 5." % i

    i += 1
    print "number at bottom is: %r" % i
    print "\n"
print numbers
