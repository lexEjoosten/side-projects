import matplotlib.pyplot as plt
z,y=[],[]
phi=1.618033988749894848204586834
delta=0.01
xmin=-10
xmax=10
detail=100000
for x in range (xmin*detail,xmax*detail):
	n=x/detail
	p=0
	while(n>(phi+delta) or n<(phi-delta)):
		if(n!=0.0):
			n=1+1/n
		else:
			n=0.0001
		p+=1
	n=x/detail
	z.append(p)
	y.append(n)
plt.plot(y,z)
plt.scatter([phi],[0])
plt.show()