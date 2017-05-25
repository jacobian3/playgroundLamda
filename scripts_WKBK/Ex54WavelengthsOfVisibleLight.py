#PROGRAM Ex54.py3

#READ wavelength from user as float
wavelength = float(input("Enter wavelength of light as decimal: "))

#COMPUTE 
#IF wavelength is in range of Red THEN
if wavelength >= 751 :
    #SET color to Invaild
    color = "Invalid"
#IF wavelength is in range of Red THEN
elif wavelength >= 620 :
    #SET color to Red
    color = "Red"
#IF wavelength is in range of Orange THEN
elif wavelength >= 590 :
    #SET color to Orange
    color = "Orange"
#IF wavelength is in range of Yellow THEN
elif wavelength >= 570 :
    #SET color to Yellow
    color = "Yellow"
#IF wavelength is in range of Green THEN
elif wavelength >= 495 :
    #SET color to Green
    color = "Green"
#IF wavelength is in range of Blue THEN
elif wavelength >= 450 :
    #SET color to Blue
    color = "Blue"
#IF wavelength is in range of violent THEN
elif wavelength >= 380 :
    #SET color to violet
    color = "Violet"
#ELSE wavelength is outside of range THEN
else:
    #SET color to outside of range
    color = "Invalid"
#ENDIF

if color == "Invalid" :
    #WRITE color or error if outside of range
    print("Color is outside of range.")
else:
    print("Color is %s." % color)
#ENDIF
#END
