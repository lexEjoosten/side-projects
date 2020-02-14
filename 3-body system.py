from graphics import *
import time
import matplotlib.pyplot as plt
from math import *
import cmath
import Border
import random
import ctypes  # An included library with Python install.

#system functions
def force_function(R,dt_force_function,circle_size):
	variability_constant=15
	g=1*10**7
	delta_velocity=(dt_force_function*g)/((max(R,circle_size)**2))
	return delta_velocity
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
#Mbox('Your title', 'Your text', 1)

#System Variables:
circle_size=5
x,y=1800,800
dt=1/10000
vfactor=1000
factor=0
crazyfactor=1
di=40
alpha=20000
pos1=complex(0.7*x,0.5*y)
pos2=complex(0.5*x,0.7*y)
pos3=complex(0.5*x,0.5*y)
pos1_l=pos1
pos2_l=pos2
pos3_l=pos3
vel1=complex(factor*random.random()-0.5*factor,factor*random.random()-0.5*factor)
vel2=complex(factor*random.random()-0.5*factor,factor*random.random()-0.5*factor)
vel3=complex(factor*random.random()-0.5*factor,factor*random.random()-0.5*factor)


win = GraphWin("3-body System", x, y)
pt1=Point(pos1.real, pos1.imag)
pt2=Point(pos2.real, pos2.imag)
pt3=Point(pos3.real, pos3.imag)
cir1 = Circle(pt1, circle_size)
cir1.setFill("blue")
cir1.draw(win)
cir2 = Circle(pt2, circle_size)
cir2.setFill("red")
cir2.draw(win)
cir3 = Circle(pt3, circle_size)
cir3.setFill("green")
cir3.draw(win)

print(0)
#Looping Functions
t1=time.time()
t2=0
for i in range(0,int(alpha/dt)):
	R12,phi12=cmath.polar(pos1-pos2)
	R23,phi23=cmath.polar(pos2-pos3)
	R31,phi31=cmath.polar(pos3-pos1)
	dv12=force_function(R12,dt,circle_size)
	dv23=force_function(R23,dt,circle_size)
	dv31=force_function(R31,dt,circle_size)
	dvel12=cmath.rect(-dv12,phi12)
	dvel23=cmath.rect(-dv23,phi23)
	dvel31=cmath.rect(-dv31,phi31)
	vel1=crazyfactor*vel1+(dvel12-dvel31)
	vel2=crazyfactor*vel2+(dvel23-dvel12)
	vel3=crazyfactor*vel3+(dvel31-dvel23)
	pos1+=vel1*dt
	pos2+=vel2*dt
	pos3+=vel3*dt
	if(i%di==0):
		dpos1=pos1-pos1_l
		dpos2=pos2-pos2_l
		dpos3=pos3-pos3_l
		if True==False:
			pt=Point(pos1.real,pos1.imag)
			pt.setFill("blue")
			pt.draw(win)
			pt=Point(pos2.real,pos2.imag)
			pt.setFill("red")
			pt.draw(win)
			pt=Point(pos3.real,pos3.imag)
			pt.setFill("green")
			pt.draw(win)
		cir1.move(dpos1.real, dpos1.imag)
		cir2.move(dpos2.real, dpos2.imag)
		cir3.move(dpos3.real, dpos3.imag)
		pos1_l=pos1
		pos2_l=pos2
		pos3_l=pos3
		time.sleep(dt)
		t2=time.time()
		print(round(di/((t2-t1)*alpha),4),end='\r')
		t1=t2
	vel1,pos1=Border.bounce(vel1,pos1,x,y,dt)
	vel2,pos2=Border.bounce(vel2,pos2,x,y,dt)
	vel3,pos3=Border.bounce(vel3,pos3,x,y,dt)
