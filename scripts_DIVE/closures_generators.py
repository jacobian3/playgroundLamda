# closure to make functions to get multiple multiplication functions
#  using closures.
def multiplier_of(n): 		# takes arg as global
    def multiplier(number):	# multiplies the param var by new num. 
        return number*n
    return multiplier

multiplywith5 = multiplier_of(5) # assigns a function with a prev. assigned var
print(multiplywith5(9)) 		# uses the assignment to take a new arg

multiplywith4 = multiplier_of(4)
print(multiplywith4(9))
