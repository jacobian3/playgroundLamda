def binary_search( theValues, item ):
    low = 0
    high = len(theValues) - 1

    # WHILE not found the element, keep looking
    while low <= high:
        # COMPUTE check for middle element
        mid = ( low + high ) / 2
        guess = theValues[mid]
        
        #found the item
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9] # test list

print binary_search(my_list, 3) # => 1
print binary_search(my_list, -1) # => None
