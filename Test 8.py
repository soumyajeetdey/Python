# write a program to display each Unique item and the no.of times it is repeated

lang  = ["spark","spark","spark","java","unix","unix","python","python","C","C","C","C"]

for val in set(lang):
    print(val , lang.count(val))