#PROGRAM Ex61py3

total_value = 0
average = 0
count = 0

#READ value from the user 
print("when complete enter '0' as sentinel value")
int_value = int(input("Provide integer value : "))

#IF sentinel is entered "0"
if int_value == 0 :
    print("use should not enter '0' as first value")
#ELSE
else:
    #WHILE sentinel is true
    while int_value != 0 :
        #COMPUTE average values entered
        #SET sum of values as numperator
        #SET accumulator as denominator to be the total number of values
        total_value = int_value + total_value
        print("total_value:",total_value)
        count = count + 1
        print("count:",count)
        average = total_value / count
        print("average:",average)
        int_value = int(input("Provide integer value : "))
    #ENDWHILE
#ENDIF

#WRITE average of values to user
print("The average of all values is: %s " % average)
#END
