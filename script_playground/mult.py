#TOC
# TODO: do colomn headings
# TODO: do row headings
# TODO: calculate the product of each row and coulumn heading
#
#SET range for table
END = 15
START = 1

#WRITE columns
print("    ", end="")
for column in range(START, END + 1):
	print("%4d" % column, end= "")
print("")

#WRITE row head
for row in range(START,END + 1):
    print("%4d" % row, end = "")
    #CALCULATE and WRITE row and column products
    for column in range(START, END + 1):
        print("%4d" % (row * column), end = "")
    print()
