charlist = 'F e c a B D'.split()

#def up_case(char):  #alt method to test understanding
#    return char.lower()
#
#s_list = sorted(charlist, key = up_case)

# str.lower is an actual method call; not an abstraction
s_list = sorted(charlist, key = str.lower)


print(s_list)
