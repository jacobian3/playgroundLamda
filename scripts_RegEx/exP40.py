import re
import os

"""regex: Fix varied-spacing between lines"""

DATA_FILE_PATH = '../script_data'

filename = 'letter_varied_spacing.txt'

file_path = os.path.join(DATA_FILE_PATH, filename)

fh = open(file_path).read()

replacement_char = '\n'

# find occourance
if re.search(r'\n\n', fh):
    re.sub(r'\n\n', replacement_char, fh)



# substituttion
new_string =  re.sub(r'\n\n', replacement_char, match_string)

print(new_string)
