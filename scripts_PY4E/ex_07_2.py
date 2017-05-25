##fn = input("Enter the desired file name: ")
#fn = 'mbox.txt'
#
#try:
#    fh = open(fn)
#except:
#    print("%s isn't a valid file." % fn)
#    exit()
#
#count = 0
#total = 0
## taken from a stackOverflow answer and refactored
#for lx in fh:
#    if lx.startswith("X-DSPAM-Confidence:"):
#        colpos = lx.find(':')
#        print("colpos:",colpos)
#        spam = lx[colpos+1:] # this is incorrect;change: +1 -> +2
#        print("spamb4:",spam)
#        spam = spam.lstrip()
#        spam = float(spam)
#        print("spamAfter:",spam)
#        count += 1
#        print("count:",count)
#        total += spam
#        print("total",total)
#
#print("total count: ",count)
#print("total spam: ",total)
#        
#print("Average is: ", total / count)


#PROGRAM: understanding extraction techniques

fn = 'mbox.txt'

try:
    fh = open(fn)
except:
    print("%s isn't a valid file." % fn)
    exit()

for lx in fh:
    lx = lx.strip() # ok to place before selectioni statement
    if lx.startswith("X-DSPAM-Confidence:"):
        print(lx)
        colpos = lx.find(':') # give position of ':' => 18
        print("colpos:",colpos)
        spam = lx[colpos+2:] # 2 space rt fr. ':' is the '0' til EOL
        print("spamb4:",spam)

