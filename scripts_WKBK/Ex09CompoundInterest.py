#PROGRAM Ex09CompoundInterest:
#SET interest rate at 4% per year
#SET year values
apr = .04

#READ deposit amount
principal = float(raw_input("Enter the principal amount:\n"))

#CALCULATE intereste earned and paid by year end
#CALCULATE add to balance of sav_account at end of year
#CALCULATE for year 2 and 3 balance also
interest_amount1 = apr * principal 
sav_bal1 = principal + interest_amount1
interest_amount2 = apr * sav_bal1 
sav_bal2 = sav_bal1 + interest_amount2
interest_amount3 = apr * sav_bal2
sav_bal3 = sav_bal2 + interest_amount3

#WRITE savings account amount after 1, 2, and 3 years (rnd@2decimal)
print "interest in year 1 is: $%.2f" % interest_amount1
print "The saving balance in year one is: $%.2f" % sav_bal1
print "interest in year 2 is: $%.2f" % interest_amount2
print "The saving balance in year two is: $%.2f" % sav_bal2
print "interest in year 3 is: $%.2f" % interest_amount3
print "The saving balance in year three is: $%.2f" % sav_bal3
#END Ex09CompoundInterest
