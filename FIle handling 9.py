# write a program to read movies.csv and display all the different genres line by line.

import csv

movies = set()
movieslist = []
with open('movies.csv',encoding='utf-8') as fobj:
    reader = csv.reader(fobj)
    for line in reader:
        genre= line[2]
        output= genre.split("|")
        movieslist.extend(output)
    for movie in set(movieslist):
        print(movie)