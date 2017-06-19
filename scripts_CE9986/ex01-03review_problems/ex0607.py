def my_element_modifier(arg):
    lower_arg = arg.lower()
    print('sorting element "{}" by "{}"'.format(arg, lower_arg))
    return lower_arg

sorted_list = sorted('e c D B a'.split(), key=my_element_modifier)

print(sorted_list)
