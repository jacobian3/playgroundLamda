# Exercise 33: While Loops
print " What number is your minimum?"
minimum = int(raw_input("< "))
print " What number is your maximum?"
maximum = int(raw_input("< "))

def show_add_next(begin_num, max_num):
    # this function adds numbers to a list
    i = begin_num
    max_num += 1
    numbers = []

    while i < max_num:
        print "At the top i is %d" % i
        numbers.append(i)

        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


    print "The numbers: "

    for num in numbers:
        print num

    print numbers

show_add_next(minimum, maximum)
