##Searching through a file
##first example: get rid of whitespace
#fhand = open('mbox.txt')
#for line in fhand:
#    line = line.rstrip()
#    if line.startswith("From:"):
#        print(line)




##Searching through a file
##second example: skip uniteresting lines
#fhand = open('mbox.txt')
#count = 0
#for line in fhand:
#    line = line.rstrip()
#    if not line.startswith('From:'):
#        continue
#    #process interesting lines
#    count += 1 #counts interesting items
#    print(line)
#    print(count)

##Searching through a file
## example: find

#fhand = open('mbox.txt')
#for line in fhand:
#    line = line.rstrip()
#    if line.find('@uct.ac.za') == -1 :
#        continue
#    print(line)
