#PROGRAM Ex09CompoundInterestLoop:

#SET interest rate at 4% per year
apr = .04

#READ deposit amount
principal = float(raw_input("Enter the principal amount:\n"))

#WHILE counter is less than or equal to 3 DO
i = 1
while i < 4:
    #CALCULATE interest earned and paid by year end
    #CALCULATE add to principal at end of year
    interest_earned = apr * principal
    principal += interest_earned
    i += 1
    #WRITE savings account amount after 1, 2, and 3 years (rnd@2decimal)
    print "interest in year %s is: $%.2f" % (i, principal)
#ENDWHILE
#END Ex09CompoundInterestLoop
