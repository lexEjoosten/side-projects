#this program was created to investigate some of the properties of elliptic curves, it loops through some different values for constants in the eliptic curve function in order to understand its properties

import math
import matplotlib.pyplot as plt


text=100
de=100
a_min=4
a_max=10
b=10
c=10
for e in range(a_min*de,a_max*de):
    X,Y1,Y2=[],[],[]
    a=e/de
    for i in range(-10*text,text*10):
        x=i/text
        if x**3+a*x**2+b*x+c>=0:
            X.append(x)
            Y1.append(math.sqrt(x**3+a*x**2+b*x+c))
            Y2.append(-math.sqrt(x**3+a*x**2+b*x+c))
    if e%10==0:
        plt.clf()
        plt.plot(X,Y1)
        plt.plot(X,Y2)
        plt.draw()
        plt.pause(0.005)
        print(a,end='\n')
