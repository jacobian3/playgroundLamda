from sys import argv
#this takes files and unpacks them into the program

script, text_file = argv

fhand = open(text_file)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1
print("There were", count, "subject lines in %s." % text_file)
