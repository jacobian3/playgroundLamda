#PROGRAM Ex59.py3

#READ string from user with license plate; seperate sting into components
license_plate = input("Enter license plate ID: ")

#COMPUTE 
#IF license starts with 3 uppercase letters and ends with 3 numbers THEN
if len(license_plate) == 6 and \
    license_plate[0].istitle() == True and \
    license_plate[1].istitle() == True and \
    license_plate[2].istitle() == True and \
    license_plate[3].isdigit() == True and \
    license_plate[4].isdigit() == True and \
    license_plate[5].isdigit() == True : 

    #SET license type to old
    license_type = 'old'

#IF license starts with 4 numbers and ends with 3 uppercase letters THEN
elif len(license_plate) == 7 and \
    license_plate[0].isdigit() == True and \
    license_plate[1].isdigit() == True and \
    license_plate[2].isdigit() == True and \
    license_plate[3].isdigit() == True and \
    license_plate[4].istitle() == True and \
    license_plate[5].istitle() == True and \
    license_plate[6].istitle() == True :

    #SET license type to new
    license_type = 'new'

#ELSE
else:
    #SET license to invalid
    license_type = 'invalid'

#WRITE to user type of license plate
print("%s is %s" % (license_plate, license_type))
#END
