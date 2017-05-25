from sys import argv

usage = 'Usage: {} [int1] [int2]'

try:
    arg0 = argv[0]
    arg1 = argv[1]
    arg2 = argv[2]
except IndexError:
    exit(usage.format(arg0))
    

try:
    this_sum = int(arg1) + int(arg2)
except ValueError:
    exit(usage.format(arg0))

print("{} + {} = {}".format(arg1, arg2, this_sum))
