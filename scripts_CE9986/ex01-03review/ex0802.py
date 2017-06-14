import sys

usage = 'Usage: validate_addargs.py [int1] [init]'

try:
    num1 = sys.argv[1]
    num2 = sys.argv[2]
except IndexError:
    exit('UsageIE: validate_addargs.py [int1] [init]')

try:
    ans = int(num1) + int(num2)
except ValueError:
    exit('UsageVE: validate_addargs.py [int1] [init]')


print("{} + {} = {}".format(num1, num2, ans))
