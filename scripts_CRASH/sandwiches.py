# @ param items is a list of arbitrary wants on a sandwich
def sandwhich(*items):
    """ show the items on a sandwhich """
    print("\nThis sandwhich has " + str( len(items) ) + " item(s): ")
    for item in items:
        print(" - " + item)

def main():
    sandwhich("ranch", "cucumbers", "apple slices")
    sandwhich("hamburger", "lettuce")
    sandwhich("bacon")

if __name__ == "__main__":
    main()
