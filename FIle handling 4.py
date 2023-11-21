# write a program to read adult.csv and display workclass and occupation colums only

import csv

try: # open the file under try block and add exception handling cases
    with open('adult.csv','r') as fobj:
        reader = csv.reader(fobj)
        for line in reader:
            print("workclass :",line[1])
            print("occupation :",line[6])
except TypeError as err:
    print("system error :",err)
except ValueError as err:
    print("system error :",err)
except (KeyError,IndexError) as err:
    print(err)
except FileNotFoundError as err:
    print(err)
except Exception as err: # default or base class exception
    print(err)