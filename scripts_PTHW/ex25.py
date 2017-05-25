# Exercise 25: Even More Practice
# we call a function on stuff named split; '.' gives command w/ parammeter
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words) # internal function that sorts

def print_first_word(words):
    """Prints the first word after popping it off."""
    # we call on word function 'pop' to take the first word
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    # we call on word function 'pop' to take the last word
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returs the sorted words."""
    # alt: could be written as: sort_words(break_words(sentence))
    words = break_words(sentence) # 1st: uses function to break words up
    return sort_words(words) # 2nd: uses another function to sort the assignment

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence) # breaks the word up
    print_first_word(words) # function takes first word 
    print_last_word(words) # function takes last word

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence) # split sentence n2 words then sorts them
    print_first_word(words) #pops first word on local var only
    print_last_word(words) # pops second word on local var only
