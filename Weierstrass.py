import numpy as np
import matplotlib.pyplot as plt
import math
import random as rand

b=5
a=0.3
m=300

text=8000
x_min=0
x_max=math.pi*2
y=[]
X=[]
for x in range(0,int((x_max-x_min)*text)):
	y.append(0)
	X.append(x/text)
	for n in range(0,m):
		y[x]+=(a**n)*math.cos((b**n)*x/text)

plt.plot(X,y)
plt.show()
