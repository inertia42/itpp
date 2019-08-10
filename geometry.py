import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from module import *
from B_distribution import *

def line_data3d(x0,y0,z0,step):
    linex=[x0]
    liney=[y0]           #给定初始点
    linez=[z0]
    # print(linex)
    i=0
    step=1/step
    while i<=20000:      #判断是否超出绘图范围
        i=i+1
        Bx,By,Bz=tokamak(linex[-1],liney[-1],linez[-1])            #获取磁感应强度
        # print(Bx,By)
        linex.append(linex[-1]+step*Bx/np.sqrt(Bx**2+By**2+Bz**2))       #计算下一个点的位置
        liney.append(liney[-1]+step*By/np.sqrt(Bx**2+By**2+Bz**2))
        linez.append(linez[-1]+step*Bz/np.sqrt(Bx**2+By**2+Bz**2))
        #print(linex[i],liney[i])
    #print(linex,liney,linez)
    return linex,liney,linez

def line_plot3d(coord,step,method=0):
    fig = plt.figure()
    # global ax
    ax = fig.gca(projection='3d')
    if method==0:
        for p in coord:
            linex, liney,linez=line_data3d(*p,step)
            ax.plot(linex,liney,linez,'r')
            ax.plot(linex[:9],liney[:9],linez[:9],'xb')
            # ax.plot_wireframe(X,Y,Z,rstride=40,cstride=40)
            # ax.plot_wireframe(X,Y,-Z,rstride=40,cstride=40)
            # plt.xlim((-3,3))
            # plt.ylim((-3,3))
           #  ax.set_zlim3d(-2,2)
            # ax.legend()
        plt.show()
    if method==1:
        for p in coord:
            linex, liney,linez=praline_data(*p,step)
            ax.plot3d(linex,liney,linez,'r')
            ax.legend()
        plt.show()
    return



def geometry(ax):
    theta=np.arange(-np.pi,np.pi,0.01)
    phi=np.arange(0,2*np.pi,0.01)
    X=np.outer(R0+r0*np.cos(theta),np.cos(phi))
    Y=np.outer(R0+r0*np.cos(theta),np.sin(phi))
    Z=np.sqrt(np.abs(-np.abs(np.sqrt(X**2+Y**2)-R0)**2+r0**2))

    ax.plot_wireframe(X,Y,Z,rstride=40,cstride=40,linewidth=1)
    ax.plot_wireframe(X,Y,-Z,rstride=40,cstride=40,linewidth=1)
    plt.xlim((-3,3))
    plt.ylim((-3,3))
    ax.set_zlim3d(-2,2)




