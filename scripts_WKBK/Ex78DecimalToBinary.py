#PROGRAM Ex78DecimalToBinary 
#convert decimal(base 10) to binary(base 2) 
result = ""

#READ decimal number from user as integer
base_10 = int(input("Enter decimal number: "))
q = base_10 

#COMPUTE using division algorithm provided 
#REPEAT
while True:
    r = q % 2 #the 2: this is the same as new_base = 2
    result += str(r) #so as to not change the value of 'r' per cycle
    #the 2: this is the same as new_base = 2
    q = q // 2 #??later try q //= 2
    if q == 0:
        break
#UNTIL

#WRITE result in binary representation
print("The result is %s." % result)
#END
