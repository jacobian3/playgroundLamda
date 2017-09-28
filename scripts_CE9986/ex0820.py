import re

"""regex: if it ends in .jpg or .JPG """

# given 
match_strings = [
    'hello world 00',
    'goodbye world    ',
    ' 23 bonjour',
    'wilkommen23  ',
    'aloha',
    '99',
    '88557799',
    'Que 3 Tal!',
    'myfile.jpg',
    'yourfile.JPG'
]

count = 0

for item in match_strings:
    if re.search(r'[.](jpg|JPG)$', item): # eval 1 consec. chr at a time!
        count += 1
        print(item)

print('count: ',count)
