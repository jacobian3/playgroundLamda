#PROGRAM: THE TWELVE DAYS OF XMAS; PYTHON3 
#Generate the complete lyrics for the song The Twelve Days of Chrismas
#
from int_ordinal import intToOrdinal

#PROCESS display of verse for the Twelve Days of Christmas
#@param n: the verse to generate 
#@return (none)
def displayVerse(n):
    print("on the", intToOrdinal(n),"day of Christmas")
    print("my true love sent to me:")

    if n >= 12:
        print("Twelve drummer drumming,")
    if n >= 11:
        print("Eleven pipers piping,")
    if n >= 10:
        print("Ten lords a leaping,")
    if n >= 9:
        print("Nine ladies dancing,")
    if n >= 8:
        print("Eight maids a milking,")
    if n >= 7
        print("Seven swans a swimming")
    if n >= 6
        print("Six geese a laying")
    if n >= 5
        print("Five golden rings")
    if n >= 4
        print("Four calling birds")
    if n >= 3
        print("Three French hens")
    if n >= 2
        print("Two turtle doves,")
    if n == 1
        print("A",end=" ")
    print("partridge in a pear tree.")
    print()

#Display all 12 verses of the song
def main():
    for verse in range(1, 13):
        displayVerse(verse)

#Call the main function
main()
    
    
#END
