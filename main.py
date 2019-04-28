import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
from geometry import *
# from B_distribution import *
from module import *
from push import *

#np.set_printoptions(threshold=np.inf)

# theta=np.arange(-np.pi,np.pi,0.01)
# phi=np.arange(0,2*np.pi,0.01)
# X=np.outer(R0+r0*np.cos(theta),np.cos(phi))
# Y=np.outer(R0+r0*np.cos(theta),np.sin(phi))
# Z=np.sqrt(np.abs(-np.abs(np.sqrt(X**2+Y**2)-R0)**2+r0**2))

# ax=Axes3D(fig)
# ax.plot_wireframe(X,Y,Z,rstride=30,cstride=30)
# ax.plot_wireframe(X,Y,-Z,rstride=30,cstride=30)
# plt.xlim((-3,3))
# plt.ylim((-3,3))
# ax.set_zlim3d(-2,2) 
# plt.show()


# def q(rr):
    # #rr=r(x,y,z)
    # return 0.1+rr**2

# def R(x,y,z):
    # return np.sqrt(x**2+y**2)

# def r(x,y,z):
    # return np.sqrt(np.abs((np.sqrt(x**2+y**2)-R0)**2+z**2))

# def Bt(RR):
    # return B0*R0/RR

# def Bp(rr,RR):
    # return Bt(RR)*rr/(q(rr)*R0)

# def B_distribution(x,y,z):
    # RR=R(x,y,z)
    # rr=r(x,y,z)
    # # print(rr)
    # Btn=Bt(RR)
    # Bpn=Bp(rr,RR)
    # Bx=-Btn*(y/RR)-Bpn*(z/rr)*(x/RR)
    # By=Btn*(x/RR)-Bpn*(z/rr)*(y/RR)
    # Bz=Bpn*(RR-R0)/rr
    # return Bx,By,Bz
    


# def line_data3d(x0,y0,z0,step):
    # linex=[x0]
    # liney=[y0]           #给定初始点
    # linez=[z0]
    # # print(linex)
    # i=0
    # step=1/step
    # while i<=100000:      #判断是否超出绘图范围
        # i=i+1
        # Bx,By,Bz=B_distribution(linex[-1],liney[-1],linez[-1])            #获取磁感应强度
        # # print(Bx,By)
        # linex.append(linex[-1]+step*Bx/np.sqrt(Bx**2+By**2+Bz**2))       #计算下一个点的位置
        # liney.append(liney[-1]+step*By/np.sqrt(Bx**2+By**2+Bz**2))
        # linez.append(linez[-1]+step*Bz/np.sqrt(Bx**2+By**2+Bz**2))
        # #print(linex[i],liney[i])
    # #print(linex,liney,linez)
    # return linex,liney,linez

# def line_plot3d(coord,step,method=0):
    # fig = plt.figure()
    # ax = fig.gca(projection='3d')
    # if method==0:
        # for p in coord:
            # linex, liney,linez=line_data3d(*p,step)
            # ax.plot(linex,liney,linez,'r')
            # ax.plot(linex[:9],liney[:9],linez[:9],'xb')
            # # ax.plot_wireframe(X,Y,Z,rstride=30,cstride=30)
            # # ax.plot_wireframe(X,Y,-Z,rstride=30,cstride=30)
            # # plt.xlim((-3,3))
            # # plt.ylim((-3,3))
           # #  ax.set_zlim3d(-2,2)
            # geometry()
            # ax.legend()
        # plt.show()
    # if method==1:
        # for p in coord:
            # linex, liney,linez=praline_data(*p,step)
            # ax.plot3d(linex,liney,linez,'r')
            # ax.legend()
        # plt.show()
    # return


# line_plot3d([[2.2,0.4,0.1]],1000)
# xn,yn,zn,E=leapfrog(x0,y0,z0,vx0,vy0,vz0)
# u2=boris(x0,y0,z0,vx0,vy0,vz0)
u2=rungekutta4(x0,y0,z0,vx0,vy0,vz0)
u=oden(x0,y0,z0,vx0,vy0,vz0)
t=dt*np.array(range(nt))
u1=np.array([(vx0/q_m)*np.sin(q_m*B0*t),2*y0+(vx0/q_m)*np.cos(q_m*B0*t),z0+vz0*t])
# u=rungekutta4(x0,y0,z0,vx0,vy0,vz0)
# xn,yn,zn,E=rungekutta2(x0,y0,z0,vx0,vy0,vz0)
# print(xn,yn,zn)
# print(len(xn))
# trace,t=oden(x0,y0,z0,vx0,vy0,vz0)
fig=plt.figure()
# E=np.sqrt(u[:,3]**2+u[:,4]**2+u[:,5]**2)
# E1=np.sqrt(u2[:,3]**2+u2[:,4]**2+u2[:,5]**2)
E1=np.sqrt(u2[:,3]**2+u2[:,4]**2+u2[:,5]**2)
global ax
# dd=u[:-1,0]-u1[0]
ddd=u2[:-1,0]-u[:,0]
# ddd=u2[:-1,0]-u1[0]
# du=u2[:-1,0]-u1[0]
# ddd=du[1:]-du[:-1]
# d=np.sqrt(dd[:,0]**2+dd[:,1]**2+dd[:,2]**2)
# d=dd
ax = fig.gca(projection='3d')

# ax.plot(u[:,0],u[:,1],u[:,2],'r')
# ax.plot(u1[:,0],u1[:,1],u1[:,2],'b')
# ax.plot(u1[0],u1[1],u1[2])
# ax.plot(trace[:,0],trace[:,1],trace[:,2],'r')
geometry(ax)
plt.show()
# plt.plot(d)
plt.plot(ddd)
plt.show()
plt.subplot(121)
# plt.plot(trace[:,0],trace[:,1])
# plt.plot(u[:,0],u[:,1])
plt.plot(u1[0],u1[1])
plt.plot(u2[:,0],u2[:,1])
plt.subplot(122)
# plt.plot(E)
plt.plot(E1)
plt.show()


