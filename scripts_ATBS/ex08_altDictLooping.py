favorite_languages = dict(zip('jen sarah edward phil'.split(),
    'python c ruby python'.split()))

my_friends = ['bob','sue', 'phil','sarah'] 
for name in favorite_languages:
    print(name.title())

    if name in my_friends:
        print("\tHi " + name.title() + 
                ", I see your favorite language is " + 
                favorite_languages[name].title() + "!")
    else:
        print("\tHi " + name.title() + ", please take our poll!")

