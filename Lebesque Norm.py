#Lebesque Norm Simulator.
import numpy as np
import matplotlib.pyplot as plt
import plotting_functions
import random
import math

xmax=1000
print(0)
for N in range(1,400):
    n=N/100
    X=np.linspace(0,1,xmax*2, endpoint=True)
    Y=(1-X**n)**(1/n)
    plt.clf()
    plt.plot(X,Y,'k')
    plt.plot(X,-Y,'k')
    plt.plot(-X,Y,'k')
    plt.plot(-X,-Y,'k')
    plt.draw()
    plt.pause(0.01)
