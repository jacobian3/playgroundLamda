#PROGRAM: Ex79MaximumInteger ; insight into process
"""Find the max of 100 random integers, counting the number of times the max
value is updated"""

from random import randrange

NUM_ITEMS = 100 #constants are always uppercase

#Generage the first number and display it
mx_value = randrange(1, NUM_ITEMS + 1) #1st of 100 values
print(mx_value)

#Count of the number of updates
#initialize counter
num_updates = 0 #counters are not uppercase

#For ea. of the remaining numbers
for i in range(1, NUM_ITEMS): #99 loops will be made for the remaining numbers
    #Generate a new random number
    current = randrange(1, NUM_ITEMS + 1) #number selection: between 1 and 100

    #IF the generated number is the largest one we have seen so far
    if current > mx_value:
        #Update the maximum and count the update
        mx_value = current #allows the current value to become the max_value
        num_updates += 1 #counts ea. time current => max_value
        #Display th enumber, noting that an update occurred
        print(current, "<== Update") 
    else:
        #Display the number
        #Q: Why isn't there a count in this case?
        #ANS: In the summary, we are only counting updates.
        print(current)

#Display the summary results
print("The maximum value found was %s." % mx_value)
print("The maximum value was updated", num_updates, "times.")
#END
