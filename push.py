import numpy as np
from B_distribution import *
from E_distribution import *
#from module import *
from scipy.integrate import odeint

def leapfrog(x0,y0,z0,vx0,vy0,vz0):
    x=[x0-0.5*vx0*dt,x0+0.5*vx0*dt]  #x_leapfrog[n]=x[n-0.5]
    y=[y0-0.5*vy0*dt,y0+0.5*vy0*dt]
    z=[z0-0.5*vz0*dt,z0+0.5*vz0*dt]
    xt=[x0]
    yt=[y0]
    zt=[z0]
    vx=[vx0]                          #v_leapfrog[n]=v[n]
    vy=[vy0]
    vz=[vz0]
    for i in range(nt):
        i=i+1
        Bx,By,Bz=B_distribution(xt[i-1],yt[i-1],zt[i-1])
        # print(Bx,By,Bz)
        x.append(x[i]+dt*vx[i-1])
        y.append(y[i]+dt*vy[i-1])
        z.append(z[i]+dt*vz[i-1])
        xt.append(x[i]+0.5*dt*vx[i-1])
        yt.append(y[i]+0.5*dt*vy[i-1])
        zt.append(z[i]+0.5*dt*vz[i-1])
        vx.append(vx[i-1]+q_m*dt*(vy[i-1]*Bz-vz[i-1]*By))
        vy.append(vy[i-1]+q_m*dt*(vz[i-1]*Bx-vx[i-1]*Bz))
        vz.append(vz[i-1]+q_m*dt*(vx[i-1]*By-vy[i-1]*Bx))
    # print(vx)
    E=np.sqrt(np.array(vx)**2+np.array(vy)**2+np.array(vz)**2)
    return xt,yt,zt,E

def euler1(x0,y0,z0,vx0,vy0,vz0):
    xt=[x0]
    yt=[y0]
    zt=[z0]
    vx=[vx0]                          
    vy=[vy0]
    vz=[vz0]
    for i in range(nt):
        i=i+1
        Bx,By,Bz=B_distribution(xt[i-1],yt[i-1],zt[i-1])
        # print(Bx,By,Bz)
        x.append(x[i]+dt*vx[i-1])
        y.append(y[i]+dt*vy[i-1])
        z.append(z[i]+dt*vz[i-1])
        vx.append(vx[i-1]+q_m*dt*(vy[i-1]*Bz-vz[i-1]*By))
        vy.append(vy[i-1]+q_m*dt*(vz[i-1]*Bx-vx[i-1]*Bz))
        vz.append(vz[i-1]+q_m*dt*(vx[i-1]*By-vy[i-1]*Bx))
    # print(vx)
    E=np.sqrt(np.array(vx)**2+np.array(vy)**2+np.array(vz)**2)
    return xt,yt,zt,E

def equation(init,t):  # formulation
    x,y,z,vx,vy,vz=init
    def BB():
        Bx,By,Bz=B_distribution(x,y,z)
        return [vx,vy,vz,q_m*(vy*Bz-vz*By),q_m*(vz*Bx-vx*Bz),q_m*(vx*By-vy*Bx)]
    return BB()
        
def equationE(init,t):
    x,y,z,vx,vy,vz=init
    def BE():
        Bx,By,Bz=B_distribution(x,y,z)
        Ex,Ey,Ez=E_distribution(x,y,z)
        return [vx,vy,vz,q_m*(Ex+vy*Bz-vz*By),q_m*(Ey+vz*Bx-vx*Bz),q_m*(Ez+vx*By-vy*Bx)]
    return BE()
def oden(x0,y0,z0,vx0,vy0,vz0):
    t=dt*np.array(range(nt))
    if magnetic==0:
        trace=odeint(equation,[x0,y0,z0,vx0,vy0,vz0],t)
    elif magnetic==1:
        trace=odeint(equationE,[x0,y0,z0,vx0,vy0,vz0],t)
    return trace

def boris(x0,y0,z0,vx0,vy0,vz0):
    # xt=np.array([x0])
    # yt=np.array([y0])
    # zt=np.array([z0])
    # vx=np.array([vx0])
    # vy=np.array([vy0])
   #  vz=np.array([vz0])
    u=np.zeros((nt+1,6))
    u[0]=[x0,y0,z0,vx0,vy0,vz0]
    I=np.eye(3)
    for i in range(nt):
        i=i+1
        xn=np.array([u[i-1,0],u[i-1,1],u[i-1,2]])
        Bx,By,Bz=B_distribution(u[i-1,0],u[i-1,1],u[i-1,2])
        Omega=0.5*q_m*dt*np.array([[0,-Bz,By],[Bz,0,-Bx],[-By,Bx,0]])
        vn=np.array([u[i-1,3],u[i-1,4],u[i-1,5]])
        vn1=np.dot(np.dot(np.linalg.inv(I+Omega),I-Omega),vn)
        # print(vn1)
        # vx=np.append(vx,vn1[0,0])
        # vy=np.append(vy,vn1[1,0])
        # vz=np.append(vz,vn1[2,0])
        # xt=np.append(xt,xt[i-1]+dt*vx[i])
        # yt=np.append(yt,yt[i-1]+dt*vy[i])
        # zt=np.append(zt,zt[i-1]+dt*vz[i])
        # E=np.sqrt(vx**2+vy**2+vz**2)
        # u[i]=np.concatenate((xn+dt*(vn+vn1)/2,vn1))
        u[i]=np.concatenate((xn+dt*vn1,vn1))

    return u

# def rungekutta4(x0,y0,z0,vx0,vy0,vz0):
    # # xt=np.array([x0])
    # # yt=np.array([y0])
    # # zt=np.array([z0])
    # # vx=np.array([vx0])
    # # vy=np.array([vy0])
   # #  vz=np.array([vz0])
    # r=np.zeros((nt+1,6))
    # r[0]=[x0,y0,z0,vx0,vy0,vz0]
    # for i in range(nt):
        # i=i+1
        # Bx,By,Bz=B_distribution(xt[i-1],yt[i-1],zt[i-1])
        # Omega=q_m*dt*np.array([[0,Bz,-By],[-Bz,0,Bx],[By,-Bx,0]])
        # vn=np.array([[vx[i-1]],[vy[i-1]],[vz[i-1]]])
        # kv1=np.dot(Omega,vn)
        # kv2=np.dot(Omega,vn+0.5*kv1)
        # kv3=np.dot(Omega,vn+0.5*kv2)
        # # print(kv3)
        # kv4=np.dot(Omega,vn+kv3)
        # vn1=vn+(kv1+2*kv2+2*kv3+kv4)/6
        # # print(vn1)
        # vx=np.append(vx,vn1[0,0])
        # vy=np.append(vy,vn1[1,0])
        # vz=np.append(vz,vn1[2,0])
        # xt=np.append(xt,xt[i-1]+dt*1e-11*vx[i-1])
        # yt=np.append(yt,yt[i-1]+dt*1e-11*vy[i-1])
        # zt=np.append(zt,zt[i-1]+dt*1e-11*vz[i-1])
        
        # E=np.sqrt(vx**2+vy**2+vz**2)
    # return xt,yt,zt,E

def rungekutta4(x0,y0,z0,vx0,vy0,vz0):
    # xt=np.array([x0])
    # yt=np.array([y0])
    # zt=np.array([z0])
    # vx=np.array([vx0])
    # vy=np.array([vy0])
   #  vz=np.array([vz0])
    u=np.zeros((nt+1,6))
    u[0]=[x0,y0,z0,vx0,vy0,vz0]
    for i in range(nt):
        i=i+1
        xn=np.array([u[i-1,0],u[i-1,1],u[i-1,2]])
        Bx,By,Bz=B_distribution(u[i-1,0],u[i-1,1],u[i-1,2])
        Omega=q_m*dt*np.array([[0,Bz,-By],[-Bz,0,Bx],[By,-Bx,0]])
        vn=np.array([u[i-1,3],u[i-1,4],u[i-1,5]])
        kv1=np.dot(Omega,vn)
        kv2=np.dot(Omega,vn+0.5*kv1)
        kv3=np.dot(Omega,vn+0.5*kv2)
        # print(kv3)
        kv4=np.dot(Omega,vn+kv3)
        vn1=vn+(kv1+2*kv2+2*kv3+kv4)/6
        # print(vn1)
        # xn=xn.reshape((3,1))
        # u[i]=np.hstack((xn+dt*(vn+vn1)/2,vn1))
        u[i]=np.hstack((xn+dt*vn,vn1))
        # E=np.sqrt(vx**2+vy**2+vz**2)
    return u
def rungekutta2(x0,y0,z0,vx0,vy0,vz0):
    xt=np.array([x0])
    yt=np.array([y0])
    zt=np.array([z0])
    vx=np.array([vx0])
    vy=np.array([vy0])
    vz=np.array([vz0])
    for i in range(nt):
        i=i+1
        Bx,By,Bz=B_distribution(xt[i-1],yt[i-1],zt[i-1])
        Omega=q_m*dt*np.array([[0,Bz,-By],[-Bz,0,Bx],[By,-Bx,0]])
        xt=np.append(xt,xt[i-1]+dt*vx[i-1])
        yt=np.append(yt,yt[i-1]+dt*vy[i-1])
        zt=np.append(zt,zt[i-1]+dt*vz[i-1])
        Bx1,By1,Bz1=B_distribution(xt[i],yt[i],zt[i])
        Omega1=q_m*dt*np.array([[0,Bz1-By1],[-Bz1,0,Bx1],[By1,-Bx1,0]])
        vn=np.array([[vx[i-1]],[vy[i-1]],[vz[i-1]]])
        kv1=dt*q_m*np.dot(Omega,vn)
        kv2=dt*q_m*np.dot(Omega1,vn+kv1)
#         kv3=dt*q_m*np.dot(Omega,vn+0.5*kv2)
        # # print(kv3)
        # kv4=dt*q_m*np.dot(Omega,vn+kv3)
        vn1=vn+(kv1+kv2)/2
        # print(vn1)
        vx=np.append(vx,vn1[0,0])
        vy=np.append(vy,vn1[1,0])
        vz=np.append(vz,vn1[2,0])
        E=np.sqrt(vx**2+vy**2+vz**2)
    return xt,yt,zt,E










    
    
