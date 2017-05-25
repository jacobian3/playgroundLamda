dupvals = [1, 3, 1, 1, 2, 3, 2, 1, 3]

uval = set()

for element in dupvals:
    uval.add(element) # the set will discard all duplicates

print(uval)
