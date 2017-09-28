import re

### ANCHORS AND BOUNDARY
#
### Example: ending @21:55
#text = '.txthello.jpg'
#print(bool( re.search(r'\.txt$', text) )) # False
#
### Example: beginning @22:00
#text = '.txthello.jpg'
#print(bool( re.search(r'^\.txt', text) )) # True; \ is for file paths
#
### Example: somewhere in the string
#text = 'oh, hey there'
#print(bool( re.search(r'hey', text) )) # True
#
### Example: somwhere in the string
#text = 'oh, hey there'
#print(bool( re.search(r'^hey$', text) )) # False; space chrs are chrs also!!
# 
### Example: somwhere in the string
# will only match with 'hey'
#text = ' hey  '
#print(bool( re.search(r'^hey$', text) )) # False; space chrs are chrs also!!

## ex. @25:50
#print(bool
#( re.search(r'hey', 'ggg heyxxx') )) # True; b/c no anchor 

## CHARACTER CLASSES
# see notes
## BUILT-IN CHARACTER CLASS: DIGITS
## BUILT-IN CHARACTER CLASS: "WORD" CHARACTERS
## BUILT-IN CHARACTER CLASS: space CHARACTERS
## 

# example
#print(bool( re.search(r'^\d$', '55') )) # False ; anchors only eval 1chr!

# example
# getting a match object lets us know that we matched
# is looking for a-digit chr followed by another digit chr
#print( re.search(r'^\d\d$', '55') ) # True 

# example
#print( re.search(r'\d', 'hello yess ok 5') ) # True 

# example: Match to the wrong thing. It stops looking for a match after it 
# locates the first match. and then evals: True; b/c no anchor!!
#print( re.search(r'\d', 'hello yess ok 57') ) # True ;

#  * you must account for EVERY chr!!!
