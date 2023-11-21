""" ###############################################################################

write a program to display all the keys and values

expected output :
name       : John Smith
sku        : 20223
name       : Jane Smith
address    : 123 Maple Street
city       : Pretendville
state      : NY
zip        : 12345
name       : John Smith
address    : 123 Maple Street
city       : Pretendville
state      : NY
zip        : 12345


############################################################################### """

data = {
  "name"   : "John Smith",
  "sku"    : "20223",
  "price"  : 23.95,
  "shipTo" : { "name" : "Jane Smith",
               "address" : "123 Maple Street",
               "city" : "Pretendville",
               "state" : "NY",
               "zip"   : "12345" },
  "billTo" : { "name" : "John Smith",
               "address" : "123 Maple Street",
               "city" : "Pretendville",
               "state" : "NY",
               "zip"   : "12345" }
}

