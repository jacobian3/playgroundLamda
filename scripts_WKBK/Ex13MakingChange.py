#PROGRAM Ex13MakingChange:
#SET denomination conversion factors
# this is really read "200 cents per toonie"
#therfore cent_per_toonie = 200 would have been a better convention
# because there are not 200 toonies
toonies = 200
loonies = 100
quarters = 25
dimes = 10
nickels = 5
pennies = 1

#READ the amount of money in cents from the user
cents_available = int(input("Enter total amount of change in cents:\n"))

#COMPUTE denomination form largest to smallest
Toonies = cents_available // toonies

cents_available = cents_available % toonies

Loonies = cents_available // loonies
cents_available = cents_available % loonies

Quarters = cents_available // quarters
cents_available = cents_available % quarters

Dimes = cents_available // dimes
cents_available = cents_available % dimes

Nickels = cents_available // nickels
cents_available = cents_available % nickels

Pennies = cents_available // pennies
cents_available = cents_available % pennies

#WRITE the amount of money in pennies, nickels, dimes, quarter, loonies, toonie
#NOTE the method used to split the string, that contains formatters!!!
print("The total change is:\n")
print("%s Toonies, %s Loonies, %s Quarters, %s Dimes, %s Nickels, and " \
    "%s Pennies" % (Toonies, Loonies, Quarters, Dimes, Nickels, Pennies))
#END

