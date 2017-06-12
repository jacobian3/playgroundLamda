import os

file_name =  '../script_data/student_db.txt' 

file_size = os.path.getsize(file_name)

print("{}: {} bytes".format(file_name, file_size))

