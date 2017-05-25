#PROGRAM Ex32.py3
#READ 3 integers from user
integer1 = int(input("Enter 1st integer:\n"))
integer2 = int(input("Enter 2nd integer:\n"))
integer3 = int(input("Enter 3rd integer:\n"))

#COMPUTE min then max then middle integer
minimum_number = min(integer1, integer2, integer3)
print(minimum_number)
maximum_number = max(integer1, integer2, integer3)
print(maximum_number)
middle_number = integer1 + \
                integer2 + \
                integer3 - \
                maximum_number - \
                minimum_number

#WRITE 3 integers sorted smallest to largest
print("The smallest number is: %s" % minimum_number)
print("The middle number is: %s" % middle_number)
print("The largest number is: %s" % maximum_number)
#END
