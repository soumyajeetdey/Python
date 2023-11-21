'''
write a program to display the below information

Total no. of males  : xxxx
Total no. of females: xx

'''
try:
    with open ('adult.csv','r') as fr, open ('backup.csv','w') as fw:
        for line in fr:
            line = line.replace('United-States','USA')
            fw.write(line)
except Exception as err:
    print(err)