# write a program to read adult.csv and display workclass and occupation colums only

import csv

with open('adult.csv','r') as fobj:
    reader = csv.reader(fobj)
    for line in reader:
        print("workclass :",line[1])
        print("occupation :",line[6])