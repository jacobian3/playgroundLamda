# rename of tumbr files
import os

#change directory to directory containing files
os.chdir("/Users/jacobian3/Desktop/untitled_folder")

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    first, second, third = file_name.split("_")
    new_name = '{}-{}{}'.format(second, first, file_ext)
    os.rename(f, new_name)
