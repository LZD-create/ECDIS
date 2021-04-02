#WGS84坐标系
from math import tan,sin,pi,log,cos


def D2R(phi):                       #角度转换弧度
    return phi/180*pi
a=6378137.000                       #长轴
b=6356752.314                       #短轴
e=((a**2-b**2)/a**2)**0.5           #第一偏心率
print("e=",e)
phi=D2R(38)                             #纬度
lamda=D2R(120)                         #经度
phi_0=D2R(38)                            #基准纬度
lamda_0=D2R(0)                           #中央经线
print("phi=",phi)
print("lamda=",lamda)
print("phi_0=",phi_0)
print('lamda_0=',lamda_0)
print('lamda-lamda_0=',lamda-lamda_0)



def r_base(phi_0):                  #基准纬度圈半径r0
    return a*cos(phi_0)/(1-e**2*sin(phi_0)**2)**0.5

r0=r_base(phi_0)

def Q(phi):                         #等量纬度
    A=tan(pi/4+phi/2)
    B=((1-e*sin(phi))/(1+e*sin(phi)))**e**0.5
    return log(A*B)

q=Q(phi)

def Mercator(lamda,lamda_0):
    x=r0*q
    print("r0=",r0)
    print("q=",q)
    y=r0*(lamda-lamda_0)
    print("lamda-lamda_0=",lamda-lamda_0)
    return x,y


x,y=Mercator(lamda,lamda_0)
print("x=",x,"y=",y)





