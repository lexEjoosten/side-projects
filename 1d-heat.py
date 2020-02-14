import numpy as np
import matplotlib.pyplot as plt
import math
import random as rand
import matplotlib.animation as anim

#constants:
text=100
x_min=0
x_max=10
t_max=10000
dt=0.01
init_random=0.1
heat_constant=101
temp_max=0

#setting up initial conditions:
x=[]    
y=[]
s=float(0)
for i in range(x_min*text,x_max*text):
    x.append(i/text)
    y.append(s)
    s+=init_random*(2*rand.random()-1)/text 
    #y.append(math.sin(10*math.pi*i/(text*10)))
t=0
x.append(float(x_max))
y.append(float(temp_max))



plt.plot(x,y)
plt.show()

for i in range(0,int(t_max/dt)):
    y[0]+=heat_constant*dt*(((y[1]))-y[0])
    for p in range(1,len(x)-1):
        y[p]+=heat_constant*dt*(((y[p-1]+y[p+1])/2)-y[p])
    y[len(x)-1]+=heat_constant*dt*(((y[len(x)-2]))-y[len(x)-1])
    
    if i%50==0:
        plt.clf()
        plt.plot(x,y)
        plt.draw()
        plt.pause(0.0005)
    
    if i%100==0:
        s=0
        for r in range(0,len(x)):
            s+=y[r]
        print(s,y[0])
            

    
    


