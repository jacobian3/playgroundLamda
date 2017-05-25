#PROGRAM EX10Arithmetic : 
from math import log10
#READ a as integer from user
a = int(raw_input("Enter an integer:\n"))
#read b as integer from user
b = int(raw_input("Enter an integer:\n"))

#CALCULATE
sums = a + b
dif = a - b
product = a * b
quotient = a / b
remainder = a % b
log = log10(a)
exponent = a**b

#WRITE sums
print "the sum of %s and %s is %s"  % (a, b, sums)
#WRITE dif
print "%s less %s is %s"  % (a, b, dif)
#WRITE product
print "the product of %s and %s is %s" % (a, b, product)
#WRITE quotient
print "the quotient of %s and %s is %s"  % (a, b, quotient)
#WRITE remainder
print "the modulus of %s and %s is %s"  % (a, b, remainder)
#WRITE log
print "the result of log of %s with base 10 is %s"  % (a, log)
#WRITE exponent
print "the result of %s raised to the %s is %s"  % (a, b, exponent)
#END EX10Arithmetic
