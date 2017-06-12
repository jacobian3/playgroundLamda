line_list = [
   'the value on this line is 3',
   'the value on this line is 1',
   'the value on this line is 4',
   'the value on this line is 2',
]

def by_number(line):
    num = int(line[-1])
    return num

sorted_list = sorted(line_list, key=by_number)

for line in sorted_list:
    print(line)
