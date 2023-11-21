book = {"C1":10, "C2":20, "C3": 30}

#display keys
print(book.keys())
#display values
print(book.values())
#display key value pairs
print(book.items())
book['C4'] = 40
book['C5'] = 50
print(book)

newbook ={'c6':60,'c7':70}

#method 1
finalbook = {**book,**newbook}

#method 2
book.update(newbook)
print(newbook)