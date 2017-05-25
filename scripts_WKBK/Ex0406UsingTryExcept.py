#PROGRAM Example04.06UsingTryExcept.;py

def compute_pay(hours, rate):
    #COMPUTE
    #IF hours is less than constant then
    if hours > 40: 
        #COMPUTE overtime hours
        #COMPUTE pay
        overtime_hours = hours - 40
        pay = rate * (40 + overtime_hours * 1.5)
        #WRITE pay amount
        print pay
    #ELSE
    else:
        #COMPUTE pay amount
        #WRITE pay amount
        pay = rate * hours
        print pay 
    #END-IF

def read_data():
    #READ hours from user
    #EXCEPTION
        #WHEN hours not an integer
            # print request 
    hours = int(raw_input("Hours?: "))
    #READ rate from user
    #EXCEPTION 
        #WHEN rate is not an integer
            # print request 
    rate = int(raw_input("Rate?: "))
    return rate, hours

rate, hours = read_data()   
#try:
compute_pay(hours, rate)    
#except:
#	print 'Please enter a numeric input' 
#    read_data()
#    compute_pay(hours, pay)

#END
