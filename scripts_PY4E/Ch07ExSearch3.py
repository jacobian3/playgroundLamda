##EXAMPLE: using continue to speed up selection 
#Rh = open('mbox-short.txt')
#count = 0
#for line in fh:
#    line = line.rstrip()
#    #Skip 'unitersting line'
#    if not line.startswith('From:'):
#        count += 1 #only counting 'unintersting' files
#        continue
#    #PROCESS 'interesting' lines
#    print(line) # only prints 'interesting' files
#print('count: ', count)

# EXAMPLE: example of using list comprehension to do the same 
# this only prints lines containing the word from
handle = open('mbox-short.txt')
line = [ print(line.strip()) for line in handle if line.startswith('From:')] 

## EXAMPLE: list comprehension to break apart 
#handle = open('mbox-short.txt')

