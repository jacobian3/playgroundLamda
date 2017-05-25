#PROGRAM Tax&Tip :

#SET local tax rate to 8% 
#SET tip  
tax_rate = .08
tip_rate = .18

#READ meal amount
meal_amount = float(raw_input("Enter meal amount:\n"))

#COMPUTE tax amount as 8% of meal amount
#COMPUTE tip amount as 18% of meal amount w/o the tax
#COMPUTE grand total is meal amount + tax amount + timp amount (@2 place)
tax_amount = meal_amount * tax_rate
tip_amount = meal_amount * tip_rate
grand_total = tax_amount + tip_amount + meal_amount

#WRITE tip
print "The total amount of tip is $%.2f" % tip_amount
#WRITE tax
print "The total amount of tax is $%.2f" % tax_amount
#WRITE grand total
print "The grand total is $%.2f" % grand_total
#END Tax&Tax
