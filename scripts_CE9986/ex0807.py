"""regex: if it consists only of non-digits """
import re

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
    if re.search(r'^\D+$', item):
        count += 1
        print(item)

print('count: ',count)
