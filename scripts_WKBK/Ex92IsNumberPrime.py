## 
# Determine if a number entered is prime.
#

## Determine using
# @param n the integer to test
# @return True if the number is prime,False otherweise
# 1 isn't prime. By definition it must be divisible only by 1 and itself as two
# distinct numbers(not 1 & self: i.e., 2 can only be divided by 1 and 2)
def isPrime(n):
    if n <= 1:
        return False
    
    #Check for number from 2 up to but not including n to see if it divides
    #evenly into n
    #the assumption below is that all numbers are divisible by self and 1
    #therefore, the only check is for divisibiliy by all numbers from 2 up to 
    # but not including the number itself.
    # 'for' iteration checks all of these value. IF the condition is TRUE 
    # returning FALSE means that it can't be prime
    for i in range(2, n):
        # determines even or odd n value
        # if even result isn't prime -> False
        if n % i == 0:
            return False #return acts as in same way as a break(escapes loop)
    return True #otherwise True

#ENTERFUNCTION main
def main():
    value = int(input("Enter an integer: "))
    if isPrime(value):
        print(value, "is prime.")
    else:
        print(value, "isn't prime.")
#ENDFUNCTION

#CALL the main function, if the file isn't imported
if __name__ == '__main__':
    main()
