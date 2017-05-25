#Program using demonstrates the use of os module
import os

os.chdir("/Users/jacobian3/version-control/tabula_rasa")

for dirpath, dirname, filename in os.walk(os.getcwd()):
    print("Current Path:", dirpath)
    print("Current Directory:", dirname)
    print("Current file:", filename)

