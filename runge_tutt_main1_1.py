import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate


def func(x, u):
    f = (np.log(x + 1) / (x ** 2 + 1)) * u ** 2 + u - u ** 3 * np.sin(10 * x)
    return f


def rk_4(x0, v0, h):
    x = x0 + h
    k1 = func(x0, v0)
    k2 = func(x0 + h / 2, v0 + h / 2 * k1)
    k3 = func(x0 + h / 2, v0 + h / 2 * k2)
    k4 = func(x0 + h, v0 + h * k3)
    v = v0 + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return x, v


h = 0.01
x0 = 0
u0 = 0.2
N = 100
b = 5

List = [[x0, u0]]


def RK_Method_Without_ce_main_1(N,x0,u0,h):
    listx = []
    list = []
    for i in range(N):
        list.append(u0)
        listx.append(x0)
        x0 = rk_4(x0,u0, h)[0]
        u0 = rk_4(x0,u0, h)[1]
    return listx, list

def RK_Method_halfhope_Without_ce_main_1(N,x0,u0,h):
    listx = []
    list = []
    for i in range(2*N):
        list.append(u0)
        listx.append(x0)
        x0 = rk_4(x0,u0, h/2)[0]
        u0 = rk_4(x0,u0, h/2)[1]
    return listx, list


plt.axis([0,5,0,10])
plt.plot(RK_Method_Without_ce_main_1(10000, 0, 0.2, 0.001)[0],RK_Method_Without_ce_main_1(10000, 0, 0.2, 0.001)[1])
#plt.show()