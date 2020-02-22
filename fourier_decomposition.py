import math
import numpy as np
import matplotlib.pyplot as plt

#defining initial variables
text=10000
a=2*np.pi
ext=10

print("Current Settings:\n the number of grid segments per unit distance is: {}\n the current region of the x is: {}, {}\n and the number of fourier components calculated is {} \n".format(text,-a,a,ext))

#calling variables
alpha,beta=[],[]
X=np.linspace(-a,a, num=2*a*text, endpoint=1)
G=0*X

#defining the function (any function can be defined here)
F=X**2+5*X+1-0.2*X**3

#Finding each of the fouerier components
#treating the zeroth fourier component differently from all the others
C=np.cos(0*X)
alpha.append(0)
beta.append(np.sum(C*F)/(2*a*text))
#then calculating all other fourier components in the standard manner
for i in range(1,ext):
    S=np.sin(i*X*(np.pi/a))
    C=np.cos(i*X*(np.pi/a))
    alpha.append(np.sum(S*F)/(a*text))
    beta.append(np.sum(C*F)/(a*text))
alpha=np.array(alpha)
beta=np.array(beta)
print(alpha,beta)
for i in range(0,ext):
    G+=alpha[i]*np.sin(i*X*(np.pi/a))+beta[i]*np.cos(i*X*(np.pi/a))
plt.plot(X,F,alpha=1)
plt.plot(X,G,alpha=0.5)
plt.show()
