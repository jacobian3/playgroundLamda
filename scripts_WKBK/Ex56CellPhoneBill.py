#PROGRAM Ex56.py3

#SET tax rate, 911 rate, sales tax, additional minute rate, additional
#SET text message rate, base rate
base_cost = 15
plus_minute_rate = 0.15
plus_text_rate = 0.25
emergency_cost = 0.44
sales_tax_rate = 0.05
max_free = 50
plus_minute_cost = 0
plus_text_cost = 0

#READ number of minutes of converstation and total nubmer of text
minutes_used = int(input("Enter total minutes used: "))
messages_used = int(input("Enter total text messages used: "))

#COMPUTE logic for additonal minutes
#IF minutes used is greater than max free message 
# or IF messages used is greater than max free THEN
if minutes_used > max_free or messages_used > max_free :
    #STORE additional airtime calculation
    #STORE additional messages used
    plus_minute_cost = plus_minute_rate * ( minutes_used - max_free )
    plus_text_cost = plus_text_rate * ( messages_used - max_free )

#COMPUTE the total bill amount
pre_tax_cost = base_cost + \
    plus_minute_cost + \
    plus_text_cost + \
    emergency_cost

sales_tax_cost = pre_tax_cost * sales_tax_rate
total_bill = pre_tax_cost + sales_tax_cost

#WRITE 1. base charge, 2. additional minute charge (if exist) 3. additional
#WRITE txt messages charge (if exist) 4. 911 charge, 5. tax 6. Total bill
#WRITE 7. Display to 2 decimal points
print("Base cost is", base_cost)

if plus_minute_cost != 0 :
    print("Additional minute charge is: %s" % plus_minute_cost )
if plus_text_cost != 0 :
    print("Additional message charge is: %s" % plus_text_rate )
    
print("911 charge is: ", emergency_cost)
print("The sales tax is: ", sales_tax_cost)
print("*" * 25)
print("The total bill is: $%.2f" % total_bill)
#END
