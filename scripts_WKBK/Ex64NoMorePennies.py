#PROGRAM Ex64.py3
#THIS PROGRAM DOESNT WORK

#SET conversion factors
cash2pennies = 100
total_cost = 0
#elements = []

#READ pay type
#pay_type = input("Enter pay type as '0':CASH or '1':CREDIT/DEBIT: ")

#WRITE sentinel value to user
print("Obtain total by leaving price blank")
#READ price from user 
price_cash = float(input("Enter cash amount in dollars: "))

#WHILE sentinel isn't blank DO
while price_cash != " " :
    #COMPUTE conversion of price cash into pennies
    price_pennies = price_cash * cash2pennies
    #COMPUTE remaining change
    remaining_change = price_pennies % 5 
    #IF
    if remaining_change < 2.5 :
        rounded_change += rounddwn(remaining_change)
    #ELSE
    else:
        rounded_change += roundup(remaining_change)
        #ENDIF
    #ENDIF
    total_cost = total_cost + price_cash
    price_cash = float(input("Enter cash amount in dollars: "))
#ENDWHILE

#WRITE total cost of all items
#WRITE amount cash due
print("The total cost of all items is: $%.2f" % total_cost)
print("The cash due to customer is $%.2f" % rounded_change)
#END
