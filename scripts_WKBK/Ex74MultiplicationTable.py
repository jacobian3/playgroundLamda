#PROGRAM Ex74MultiplicationTable 
#MY INITIAL SOLUTION

#COMPUTE the top row of number from 1 to 10
#FOR i in the range of 1 to 11 DO
print("    ", end ="") #!importan:this displays the 4spaces w/o moving down!
for r_label in range(1,11):
    #WRITE i as a label
    print("%4d" % r_label, end="")
#ENDFOR
print() #start at next row

#COMPUTE the left column of numbers from 1 to 10
#FOR i in the range of 1 to 11 DO
for c_label in range(1,11):
    print("%4d" % c_label, end="") #formater here is important to align decimal
    #FOR i in the range of 1 to 11 DO
    for t_value in range(1,11):
        print("%4d" % (t_value * c_label), end="")
    #ENDFOR
    print()
#ENDFOR
#END


#PROGRAM Ex74MultiplicationTable 
#Book's solution walkthrough and insigt into problem

#Display mult table
#setting the table constants in this way allows you future ability to 
#expand the table
MIN = 1
MAX = 10

#Display the top row
#the initial space is 4 characters; this is important b/c the formatter
#in the print statement places consistent 4 spaces after print
#this keeps the uniformity of the characters to facilitate table creation
#"MAX + 1" -> range end is up-to and not including the value
print("    ", end ="") 
for i in range(MIN, MAX + 1): 
    # end="" prevents print carriage return
    # "%4d" formatter guarantees 4 spaces
    print("%4d" % i, end="") 
print() #this print stops the line for continuing to the right

#Display table
#first 'for' is for the initial row value
for i in range(MIN, MAX + 1):
    print("%4d" % i, end="")
    #second 'for' is for each consecutive mult i.e., 1 x 1..1 x 8
    for j in range(MIN, MAX + 1):
        print("%4d" % (i * j), end="")
    print()
#END
