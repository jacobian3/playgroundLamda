import os

file_name = 'test_count_number_of_words.txt'

fh = open(file_name).readlines()

line_capture = []
[line_capture.append(line.rstrip()) for line in fh if len(line) > 16]

print(line_capture)
