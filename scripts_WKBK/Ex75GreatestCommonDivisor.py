#PROGRAM Ex75GreatestCommonDivisor 
#READ two pos integer from user
n = int(input("Enter 1st positve integer: "))
m = int(input("Enter 2nd positve integer: "))

#IF n is smaller THEN
if n < m:
    #SET d
    d = n 
#ELSE
else:
    #SET d
    d = m 
#ENDIF

#WHILE do doesn't divide m or d doesn't evenly divide n DO
while m % d != 0 or n % d != 0:
    d -= 1
#ENDWHILE

#WRITE d as the greatest common divisor of n and m
print("The greatest common divisor of %s and %s is %s." % (n,m,d))
#END
