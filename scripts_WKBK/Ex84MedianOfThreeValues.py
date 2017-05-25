#Ex84MedianOfThreeValues (python3)
"""compute and display mdiedian of three values. Thsi program contains two
implementations fo the median function that demonstrate different techniques
for computing the median of three values"""

#COMPUTE using IF statements
#@param a the first value
#@param b the second value
#@param c the third value
#@return the median of values a, b, c
#
def median(a, b, c):
    if a < b and b < c or a > b and b > c: # asking:a < b < c or c > b > a
        return b # the middle in both cases
    if b < a and a < c or  b > a and a > c: # c < a < b or c > a > b 
        return a # the middle in both cases
    if c < a and b < c or c > a and b > c: # b < c < a or a < c < b
        return c # the middle in both cases

#COMPUTE the median of the three values using the min and max functions
# and a little bit of arithmetic
#@param a the first value
#@param b the second value
#@param c the third value
#@return the median of values a, b, c
#
def alternateMedian(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c) #sum - min - max is middle#

#Display the median of 3 values entered by the user
def main():
    x = float(input("Enter the first value: "))
    y = float(input("Enter the second value: "))
    z = float(input("Enter the third value: "))

    print("The median value is: ", median(x, y, z))
    print("Using the alternative method, it is:%2f" % alternateMedian(x, y, z))
    
#call the function
main()
#END
