#traditional way
# fobj acts like pointer or cursor
fobj = open('adult.csv','r')

for line in fobj:
    print(line.strip())
    
fobj.close()

# Python way
# context manager
# Advantage: file gets closed automatically

with open('adult.csv','r') as fobj:
    for line in fobj:
        print(line.strip())

# open(r'C:\Users\E439585\OneDrive - Honeywell\Desktop\Python programs)
# open(C:/Users/E439585/OneDrive - Honeywell/Desktop/Python programs)
'''
with open ('C:\\Users\\E439585\\OneDrive - Honeywell\\Desktop\\Python programs','r'):
    for line in fobj:
        print(line.strip())
'''
    
# file write operation
with open('language.txt','w') as fw:
    fw.write('python\n')
    fw.write('unix\n')
    
with open('numbers.txt','w') as fobj:
    for val in range(1,11):
        fobj.write(str(val)+ "\n")
        
