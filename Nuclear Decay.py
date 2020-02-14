import numpy as np
import matplotlib.pyplot as plt
import math
import random as rand
import matplotlib.animation as anim

n=50
M_0=np.zeros((n, n),dtype="int")
print(M_0)

Y=[]
def Numerical(M,d,n,number,Y):
	M=np.reshape(M,n**2)
	for i in range(0,len(M)):
		yp=Y[M[i]]
		yp[number]+=1
		Y[M[i]]=yp
		for oui in range(0,len(d)-1):
			e=rand.random()
			if e<d[int(M[i])]:
				M[i]+=1
	M=np.reshape(M,(n,n))
	return M,Y

d=[0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0] #decay probabilities after each timestep
t_max=1000
x=np.linspace(0, t_max, num=t_max, endpoint=True)
M=M_0
plt.ion()
fig = plt.figure()
for i in range(0,len(d)):
	Y.append([])

for s in range(0,t_max):
	for i in range(0,len(d)):
		Y[i].append(0)
	M,Y=Numerical(M,d,n,s,Y)
	print(s)
	if s%10==0:
		ax = fig.add_subplot(111)
		ax.matshow(M)
		plt.draw()
		plt.pause(0.01)

for i in range(0,len(d)):
	plt.plot(x,Y[i])
plt.show()

print(input("Press Enter to Exit"))
