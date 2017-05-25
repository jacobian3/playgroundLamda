# PROGRAM Example3.2UsingTryExcept:
try:
    #READ hours from user
    #EXCEPTION
        #WHEN hours not an integer
            # print request 
    hrs = int(raw_input("Hours?: "))
    #READ rate from user
    #EXCEPTION 
        #WHEN rate is not an integer
            # print request 
    rate = int(raw_input("Rate?: "))
    #IF hours is less than constant then
    if hrs > 40: 
        #COMPUTE overtime hours
        #COMPUTE pay
        overtime_hours = hrs - 40
        pay = rate * (40 + overtime_hours * 1.5)
        #WRITE pay amount
        print pay
    #ELSE
    else:
        #COMPUTE pay amount
        #WRITE pay amount
        pay = rate * hrs
        print pay 
    #END-IF
except:
	print 'Please enter a numeric input' 
#END
