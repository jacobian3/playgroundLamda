string = "I am happy or sad or angry or mad or generous or stingy."
print("use: {}\n".format(string))
uin = input("please enter a sub-string to replace: ")

wrdnum = string.replace(uin, "x")

print(wrdnum)
