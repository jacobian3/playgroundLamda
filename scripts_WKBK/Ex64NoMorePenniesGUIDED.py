#PROGRAM Ex64.py3
# this rework is to help me understand the problem logic

#SET conversion factors
pennies_per_nickel = 5
nickel = .05
elements = []

#SET total of all items, before entry into loop
total = 0.00

#READ the init price from the user
line = input("Enter the price of the item(blank to quit): ")

#WHILE sentinel has not been entered DO 
while line != "" :
    #STORE accumulated total
    #float is entered here to avoid converting line
    #into a float, when testing for a string sentinel value
    total = total + float(line) 
    #store values for debug
    elements.append(float(line)) # list accumulator to debug logic
    otherTotal = sum(elements)
    #READ the price from the user
    line = input("Enter the price of the item(blank to quit): ")
#ENDWHILE

#WRITE total payable to user
print("The sum of amount payable $%.2f." % otherTotal)
print("The exact amount payable is $%.2f." % total)

#COMPUTE the number of pennies that would be left if total was only paid 
# in nickels
rounding_indicator = total * 100 % pennies_per_nickel

#IF '#' of pennies is less than 2.5 pennies round down
#rounding indicator is the number of pennies remaining
#that can't be evenly divided by 5 pennies
if rounding_indicator < pennies_per_nickel / 2:
    #STORE value for total cash as pennies!
    #obtain cash as pennies by div # of pennies by 100
    cash_total = total - rounding_indicator / 100
#ELSE round up
else:
    #STORE cash total 
    # this method rounds up by .05 and then subtracts the remaining cash change
    cash_total = total + nickel - rounding_indicator / 100 
#ENDIF

#WRITE the cash amount payable
print(elements) # shows a list of all entered numbers
print("The cash amout payable is $%.2f." % cash_total)

#END 
