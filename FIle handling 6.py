# write a program to display the below information

# Total no. of males  : xxxx
# Total no. of females: xx

import csv
import sys

try: # open the file under try block and add exception handling cases
    malecount = 0
    femalecount = 0
    
    with open('adult.csv','r') as fobj:
        reader = csv.reader(fobj)
        #Loop to parse
        for line in reader:
            gender=line[9].strip()
            if gender=='Male':
                malecount+=1
            if gender=='Female':
                femalecount+=1
            
# Minimal exception handling
except Exception as err: # default or base class exception
    print(err)
    print(sys.exc_info())    

else:
       #Print final count
       print("Male count =",malecount)
       print("Female count =",femalecount)