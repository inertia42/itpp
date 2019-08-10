import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
from geometry import *
# from B_distribution import *
from module import *
from push import *

# line_plot3d([[2.2,0.4,0.1]],1000)
# xn,yn,zn,E=leapfrog(x0,y0,z0,vx0,vy0,vz0)
# u2=boris(x0,y0,z0,vx0,vy0,vz0)
# u1=rungekutta4(x0,y0,z0,vx0,vy0,vz0)
u1=oden(x0,y0,z0,vx0,vy0,vz0)
t=dt*np.array(range(nt))
# u1=np.array([(vx0/q_m)*np.sin(q_m*B0*t),2*y0+(vx0/q_m)*np.cos(q_m*B0*t),z0+vz0*t])
# u=rungekutta4(x0,y0,z0,vx0,vy0,vz0)
# xn,yn,zn,E=rungekutta2(x0,y0,z0,vx0,vy0,vz0)
# print(xn,yn,zn)
# print(len(xn))
# trace,t=oden(x0,y0,z0,vx0,vy0,vz0)
fig=plt.figure()
# E=np.sqrt(u[:,3]**2+u[:,4]**2+u[:,5]**2)
# E1=np.sqrt(u2[:,3]**2+u2[:,4]**2+u2[:,5]**2)
# E1=np.sqrt(u2[:,3]**2+u2[:,4]**2+u2[:,5]**2)
global ax
# dd=u[:-1,0]-u1[0]
# ddd=u2[:-1,0]-u[:,0]
# ddd=u2[:-1,0]-u1[0]
# du=u2[:-1,0]-u1[0]
# ddd=du[1:]-du[:-1]
# d=np.sqrt(dd[:,0]**2+dd[:,1]**2+dd[:,2]**2)
# d=dd
ax = fig.gca(projection='3d')

# ax.plot(u[:,0],u[:,1],u[:,2],'r')
# ax.plot(u1[:,0],u1[:,1],u1[:,2],'b')
ax.plot(u1[:,0],u1[:,1],u1[:,2])
# ax.plot(trace[:,0],trace[:,1],trace[:,2],'r')
plt.show()
# # plt.plot(d)
# plt.plot(ddd)
# plt.show()
# plt.subplot(121)
# # plt.plot(trace[:,0],trace[:,1])
# # plt.plot(u[:,0],u[:,1])
# plt.plot(u1[0],u1[1])
# plt.plot(u2[:,0],u2[:,1])
# plt.subplot(122)
# # plt.plot(E)
# plt.plot(E1)
# plt.show()


