# write a program to read adult.csv aand display distinct workclasses

import csv
import sys

try: # open the file under try block and add exception handling cases
    workset = set()
    with open('adult.csv','r') as fobj:
        reader = csv.reader(fobj)
        #Loop to parse
        for line in reader:
            workclass = line[1]
            workset.add(workclass)
            
# Minimal exception handling
except Exception as err: # default or base class exception
    print(err)
    print(sys.exc_info())    

else:
       #loop to diplay
       for work in workset:
           print(work)