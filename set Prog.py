aset = {10,20,20,30,30,30}
bset = {30,30,30,40,40,50,50}

print(aset)
print(bset)

#unique items
print(aset.union(bset))

#common items
print(aset.intersection(bset))

# A - B
print(aset.difference(bset))

# A is subset of B
print(aset.issubset(bset))

aset.add(30) # no change to set
print(aset)

aset.add(90) # new item get added
print(aset)