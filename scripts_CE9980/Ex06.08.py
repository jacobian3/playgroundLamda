# given
line_list = [
    'the value on this line is 3',        
    'the value on this line is 1',        
    'the value on this line is 4',        
    'the value on this line is 2',        
]

def last_number(line):
    return line.split()[-1]

# sorted returns a list (iterable)
for line in sorted(line_list, key = last_number):
    print(line)


