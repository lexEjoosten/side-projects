def bounce(vel, pos, x, y,dt):
	x=0.85*x
	posx,posy=pos.real,pos.imag
	if((posx+vel.real*dt)>x or (posx+vel.real*dt)<0):
		vel=complex(-vel.real*0.8,vel.imag)
	if((posy+vel.imag*dt)>y or (posy+vel.imag*dt)<0):
		vel=complex(vel.real,-vel.imag*0.8)
	return vel,pos
def loop(vel, pos, x, y, dt):
	x=0.85*x
	posx,posy=pos.real,pos.imag
	if posx>x:
		posx=posx-x
	if posx<0:
		posx=posx+x
	if posy>y:
		posy=posy-y
	if posy<0:
		posy=posy+y
	pos=complex(posx,posy)
	return vel,pos