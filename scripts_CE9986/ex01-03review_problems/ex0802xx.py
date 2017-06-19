import sys

try:
    num1 = sys.argv[1]
    num2 = sys.argv[2]

except IndexError:
    exit("One or three strings is missing")

try:
    ans = int(num1) + int(num2)
except ValueError:
    exit("An envalid argument was entered")

print("{} + {} = {}".format(num1, num2, ans) )
