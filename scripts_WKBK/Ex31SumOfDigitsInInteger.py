#PROGRAM Ex31.py3
#READ 4 number integer from user
number = int(input("Enter a 4 digit number:\n"))

#COMPUTE seperate each digit and place into a list
string = str(number)
digit = list(string)
number_sum =    int(digit[0]) + \
                int(digit[1]) + \
                int(digit[2]) + \
                int(digit[3])

#WRITE the sum of each of the respective 4 digits
print("The sum of the digits in number is %s" % number_sum)
#END
