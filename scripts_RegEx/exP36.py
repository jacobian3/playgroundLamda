import re

"""regex: Fix double-spacing """
## ??? this requires wrting to a file; review how to do this b/4 continuing

# GIVEN 
match_string = 'The quick brown\n\nfox jumps over the\n\nlazy dog\n\n' 
replacement_char = '\n'

print(match_string,'\n')

new_string =  re.sub(r'\n\n', replacement_char, match_string)

print(new_string)
