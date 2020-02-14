import math
from graphics import *
import time
import matplotlib.pyplot as plt
import numpy as np
import plotting_functions

i,p,primes=10**2,[2],[0,1]

if(i>=2):
	for s in range(3,i+1):
		b,m=0,0
		while (b==0 and p[m]<=math.sqrt(s)):
			if s%p[m]==0:
				b=1
			m=m+1
		if b==0:
			primes.append(1)
			p.append(s)
		else:
			primes.append(0)
primes=np.array(primes)
primes=primes.reshape(math.ceil(math.sqrt(i)),math.ceil(math.sqrt(i)))
plt.imshow(primes, cmap='terrain', interpolation='nearest')
plt.show()
