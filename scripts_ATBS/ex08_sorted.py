favorite_languages = dict(zip('jen sarah edward phil'.split(),
    'python c ruby python'.split()))

#for name in sorted(favorite_languages):
#    print(name.title() + ", thank you for taking the poll.")

#for name in sorted(favorite_languages.values()): # loops by values vs. key
#    print(name.title())

#creates set from unique vals 
for name in set(sorted(favorite_languages.values())): 
    print(name.title())
