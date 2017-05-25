# Exercise 29: What If
from sys import argv
script, people, cats, dogs = argv # allows entry from standard input
#people = 20
#cats = 30
#dogs = 15

people = int(people)
cats = int(cats)
dogs = int(dogs)

if people < cats:
    print "Too many cats! The world is doomed!"
    print "people: %r are < cats: %r" % (people, cats)

if people > cats:
    print "Not many cats! The world is saved!"
    print "people: %r are > cats: %r" % (people, cats)

if people < dogs:
    print "The world is drooled on!"
    print "people: %r are < dogs: %r" % (people, dogs)

if people > dogs:
    print "the world is dry!"
    print "people: %r are > dogs: %r" % (people, dogs)


dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."
    print "people: %r are >= dogs: %r" % (people, dogs)

if people <= dogs:
    print "People are less than or equal to dogs."
    print "people: %r are <= : %r" % (people, dogs)


if people == dogs:
    print "People are dogs."
    print "people: %r are == : %r" % (people, dogs)
