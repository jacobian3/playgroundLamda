#PROGRAM Ex33.py3
#SET bread_ea 3.49
bread_ea = 3.49
disc_bread_each = bread_ea * .40

#READ number of loaves of day old bread purchased
number_of_loaves = int(input("Enter number of loaves purchased:\n"))

#CALCULATE
total_price = number_of_loaves * disc_bread_each  

#WRITE reg price of bread
print("The regular price of bread is    $%5.2f" % bread_ea)
#WRITE the discount b/c it's a day old
print("The discounted price of bread is $%5.2f" % disc_bread_each) 
#WRITE all prices at 2 decimal precision
#WRITE decimal places alligned, when reasonable
#WRITE the total price
print("The total price of bread is      $%5.2f" % total_price)
#END
