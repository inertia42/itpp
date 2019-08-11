global R0,r0,B0

R0=2 #large radius
r0=0.8 #small radius
B0=3 #magnetic
Ex0=0.05
Ey0=0
Ez0=0

x0=0   #the initial coordinate of x
y0=-0.5  #y
z0=0    #z
vx0=0.04  
# vy0=0.0011
# vz0=0.002
vy0=0.05
vz0=0.05
dt=0.01
nt=2000
q_m=1

B_type=0    #0:Bx,By为零 1:grad_B
E_type=1
magnetic=1   #0:只有电场 1:有电场和磁场
