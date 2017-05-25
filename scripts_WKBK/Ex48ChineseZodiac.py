#program Ex48.py3

#READ year born from the user
year = int(input("Enter the year to find Zodiac year?:\n"))

# Create a circle/cycle of size B
# Start with 0 and move around it in A steps
# the landing spot is the solution
# this is calculated A mod B == ?; repeat for every element of the cycle's list
# year mod 12 == B; at each animal calculate the mod and test the condition
# trasitively if 2000 % 12 == 8 is True, since 2000 is asociated with "Dragon"
# we can establish that anytime the year % 12 the animal is a dragon
#IF cycle is 12 and we move in 1 year steps through the cycle THEN

if year % 12 == 8 :
    #SET zodiac
    zodiac = 'Dragon'
elif year % 12 == 9 :
    #SET zodiac
    zodiac = 'Snake'
elif year % 12 == 10 :
    #SET zodiac
    zodiac = 'Horse'
elif year % 12 == 11 :
    #SET zodiac
    zodiac = 'Sheep'
elif year % 12 == 0 :
    #SET zodiac
    zodiac = 'Monkey'
elif year % 12 == 1 :
    #SET zodiac
    zodiac = 'Rooster'
elif year % 12 == 2 :
    #SET zodiac
    zodiac = 'Dog'
elif year % 12 == 3 :
    #SET zodiac
    zodiac = 'Pig'
elif year % 12 == 4 :
    #SET zodiac
    zodiac = 'Rat'
elif year % 12 == 5 :
    #SET zodiac
    zodiac = 'Ox'
elif year % 12 == 6 :
    #SET zodiac
    zodiac = 'Tiger'
elif year % 12 == 7 :
    #SET zodiac
    zodiac = 'Hare'

#WRITE zodiac animal
print("%d is the year of the %s." % (year, zodiac))
#end
