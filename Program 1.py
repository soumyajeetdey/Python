# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 09:39:27 2023

@author: E439585
"""
# This is single line comment

'''
Multi line comment
'''
print (10,20,30,40)
name = 'python programming'
print (name)
print ("I Love", name)

#stine start:stop:incremental value
print(name[0])
print(name[1])
print (name[0:18:2])
print(name[:])
print(name[::])
print(name[-1])
print(name[-2])
print(name[-4:-1])
print(name[::-1])

print(name.capitalize())
print(name.title())
print(name.center(40))
print(name.center(40,"*"))
print(name.find('ram')) # index position if present
                        # -1 if not present
print(name.split(" ")) #converting string to list
print(name.format('python','C'))
print(name.replace("python","Java"))

bname = "  python "
print(len(bname))
print(len(bname.strip()))
print(len(bname.lstrip()))
print(len(bname.rstrip()))

data = ["unix","programming"] #converting list to string
print(":".join(data))

