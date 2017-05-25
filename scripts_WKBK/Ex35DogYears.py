#PROGRAM Ex35"".py3

#SET dog years
#SET dog years > 2  factor
young_dog = 10.5
old_dog = 2 * 10.5

#REPEAT
while True:
    #READ years of age from user
    years_of_age = int(input("Enter dog's age as integer: "))
#UNTIL !positve number
    if years_of_age > 0:
        break

#IF dog's years is less or equal to 2 THEN
if years_of_age <= 2:
    #CALCULATE dogs age
    dogs_age = years_of_age * young_dog
    #WRITE the dogs age
    print("The dog's age is: ", dogs_age)
#ELSE
else:
    #CALCLULATE older dogs age
    dogs_age = old_dog + ( years_of_age - 2 ) * 4
    #WRITE the dogs age
    print("The dog's age is: ", dogs_age)
#END
