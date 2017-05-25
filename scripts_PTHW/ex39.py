# Exercise 39: Dictionaries, Oh Lovely Dictionaries
# create a mapping of state to abbreviation
# maps the abbreviaitons to their respective states key
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}


# create a basic set of states and some cities in them
# maps the cities to their respective abbrevation key
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
# these will be added in arbitrary locations b/c its a dict
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10 # prints 10 dashes in a row
print "NY State has: ", cities['NY'] # the city name
print "OR State has: ", cities['OR'] # the city name

# print some states
# print a dash and given the states key prints the abbrv.
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
# uses states key to obtain the state value, then uses the state value
# as an argument(key) in the cities dict. to associate with respective 
# city value
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
# cycles throught each set of the dictionary and unpacts them
# into 2vars'
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

#now do both at the same time
# unpacts states into 2 variables and uses a formatter 
# and a key to display the cities dict.
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
# gets a value from states using a key; makes assignment
# if available = True, otherwise false
state = states.get('Texas')

# if not 'Texas' = false then print
if not state:
    print "Sorry, no Texas."

# get a city with a default value
# get provides value for both true and false availablity of cities
# named Texas
city = cities.get('TX', 'Does Not Exist')
print "the city for the state 'TX' is: %s" % city
