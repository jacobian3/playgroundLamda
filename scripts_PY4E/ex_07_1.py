#PROGRAM: ex_07.1
fname = input("Enter the file name: ")

fhand = open(fname)
for line in fhand:
    cap_line = line.upper() 
    print(cap_line.rstrip())
    
