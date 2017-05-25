citydict = {}
citylist = 'Boston,Chicago,New York,Boston,Chicago,Boston'.split(',')

for city in citylist:
    if city not in citydict:
        citydict[city] = 0
    citydict[city] += 1

print(citydict)
