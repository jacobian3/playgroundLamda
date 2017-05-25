#PROGRAM Ex67py3

totals_as_added = []

#SET senior_cost
#SET child_cost
#SET sm_child_cost
#SET adult_cost
senior_cost = 18.00
child_cost = 14.00
baby_cost = 0.00
adult_cost = 23.00

#SET limits
#NOTE problem in book doesn't account for children between 2 and 3
#intention is to place under child_limit
baby_limit = 2
child_limit = 12
adult_limit = 64

#SET the total of all admissions cost
total = 0

#SET sentinel to space
sentinel = ""

#READ group
#PROCESS
#NOTE for blank to fininsh problems 1st read before entry into loop as string
# 2nd change from str to number, in order to do calcs
# 3rd read another time to check for sentinel value
line = input("Enter the age of the guest (blank to finish)")
#WHILE not sentinel value THEN
while line != sentinel:
    #STORE line string as age var
    age = int(line)

    #COMPUTE selection logic for age limits
    #IF age < baby_limit THEN
    if age <= baby_limit:
        #SET total
        total += baby_cost
        print("current age: ", age, "therfore:" )
        totals_as_added.append(baby_cost)
    #IF age < child limit THEN
    elif age <= child_limit:
        #SET total
        total += child_cost
        print("current age: ", age, "therfore:" )
        totals_as_added.append(child_cost)
    #IF age < adult limit THEN
    elif age <= adult_limit:
        #SET total 
        total += adult_cost
        print("current age: ", age, "therfore:" )
        totals_as_added.append(adult_cost)
    #ELSE age is senior 
    else:
        #SET total 
        total += senior_cost
        print("current age: ", age, "therfore:" )
        totals_as_added.append(senior_cost)
    #ENDIF

    #DEBUG create a list of all ages given
    #allows me to set the set of entries as they accumulate
    print(totals_as_added)

    #READ line and test for sentinel value
    line = input("Enter the age of the guest (blank to finish)")
#ENDWHILE

#WRITE admission cost of the group
print("list of cost: ", totals_as_added)
print("The sum of the list: ", sum(totals_as_added))
print("The admission cost is $%.2f." % total)
#END
