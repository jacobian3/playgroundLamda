personal_info = "595-33-9193:68:Columbus, OH"

mylist = personal_info.split(':')

print("""SS#: {}
Age: {}
Residence: {}""".format(mylist[0], mylist[1], mylist[2]))

print("\nSS#: {}\nAge: {}\nResidence: {}".format(mylist[0], mylist[1], mylist[2]))
