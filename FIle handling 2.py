# Python way
# context manager
# Advantage: file gets closed automatically

with open('adult.csv','r') as fobj:
    for line in fobj:
        print(line.strip())
        print("----------")


# using csv library - need not split each line
import csv
with open('adult.csv','r') as fobj:
    # converting file object to csv object
    reader = csv.reader(fobj)
    for line in reader:
            print(line)
            print("----------")
            