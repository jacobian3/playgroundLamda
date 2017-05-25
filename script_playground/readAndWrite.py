import os

os.chdir("/Users/jacobian3/version-control/tabula_rasa/text_files")

#This is a context manager; used to autoclose after open
#will also autoclose after exception
with open('boston.txt','r') as fh:
    SIZE_TO_READ = 10 # #of chars to read in at a time

    fh_contents = fh.read(SIZE_TO_READ) #will read whole file in sm chunks

    while len(fh_contents) > 0: #fh_contents is shrinking ea. iteration
        print(fh_contents, end="*") # '*' is printed so as to see effect
        fh_contents = fh.read(SIZE_TO_READ) # reduces fh_contents
