#method1: importing all the methods
import math

print(math.floor(22.3))
print(math.ceil(43.43))
print(math.log(1))

#method2: importing with alias name
import matplotlib.pyplot as plt
print(plt.pie([20,30,50]))
'''
#method3: import required method only
from math import log,tan
print(log(34.3))
print(tan(3))

#method4: import everything using *
from math import *
print(log(34.3))
print(tan(3))
'''