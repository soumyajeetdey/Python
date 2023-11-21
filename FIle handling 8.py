'''
write a program to read supermarket_sales.csv and display the output based on the below conditions

city is yangon
customer type is Normal
payment method is Cash
Gender is Female
'''

import csv
import sys

count = 0

try:
    with open('supermarket_sales.csv','r') as fobj:
        #converting file object to csv object
        reader = csv.reader(fobj)
        #process
        for line in reader:
            if line[2].strip() == 'Yangon' and line[3].strip() == 'Normal'  and     \
            line[4].strip() == 'Female' and line[12].strip() == 'Cash' :
                print(line)
                count +=1
                
# Minimal exception handling
except Exception as err: # default or base class exception
    print(err)
    print(sys.exc_info())    

else:
       #Print final count
       print("Total count =",count)