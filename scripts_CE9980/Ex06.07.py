def my_element_modifier(arg):
    lower_arg = arg.lower()
    print('sorting element "{}" by value "{}"'.format(arg, lower_arg))
    return lower_arg

# my_element_modifier() is called once for ea. element; 5 times. python sorts
# based on return value
sorted_list = sorted('e c D B a'.split(), key=my_element_modifier)

print(sorted_list)
