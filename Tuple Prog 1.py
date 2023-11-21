atup = (12,23,34,45,56,67,78,89)
# atup[0] = 100 - this will throuw error
print(atup)

#typecasting - converting from one object to another object
alist = list(atup)
alist[0] = 100
atup = tuple(alist)
print(atup)

btup = ("java",2,32.35,"unix")