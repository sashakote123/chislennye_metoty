import numpy as np
import matplotlib.pyplot as plt
import math

u0 = 1
u0_2 = 1

err = u0_2 - u0
S = err / 15
e = 0.1

h = 0.1

x1 = np.linspace(0, 1)

u = u0 * math.e ** (3 * x1)

x = 0
x_2 = 0


def func_k1(x, u0, h):
    return 3 * u0


def func_k2(x, u0, h):
    return 3 * (u0 + h / 2 * func_k1(x, u0, h))


def func_k3(x, u0, h):
    return 3 * (u0 + h / 2 * func_k2(x, u0, h))


def func_k4(x, u0, h):
    return 3 * (u0 + h * func_k3(x, u0, h))


def func_RK(x, u0, h):
    return u0 + h / 6 * (func_k1(x, u0, h) + 2 * func_k2(x, u0, h) + 2 * func_k3(x, u0, h) + func_k4(x, u0, h))


def RK_Method_Without_ce(N, x, u0, h):
    listx = []
    list = []
    for i in range(N):
        list.append(u0)
        listx.append(x)
        u0 = func_RK(x, u0, h)
        x = x + h
    return listx, list


def RK_Method_halfhope_Without_ce(N, x, u0, h):
    list = []
    for i in range(N):
        list.append(u0)
        u0 = func_RK(x, u0, h / 2)
        x = x + h / 2
        u0 = func_RK(x, u0, h / 2)
        x = x + h / 2
    return x, list


def RK_Method_With_ce(N, x, x_2, u0, u0_2, e, h):
    list = []
    list.append(u0)
    #for i in range(N):
    for i in range(N):
        tmp_x = x
        tmp_x_2 = x_2
        tmp_u0 = u0
        tmp_u0_2 = u0_2
        u0 = func_RK(x, u0, h)
        x = x + h
        u0_2 = func_RK(x, u0_2, h / 2)
        x_2 = x_2 + h / 2
        u0_2 = func_RK(x, u0_2, h / 2)
        x_2 = x_2 + h / 2
        S = (u0_2 - u0)/15
        if abs(S) <= e and abs(S) >= e/32:
            list.append(u0)
            continue
        if abs(S) < e/32:
            h = 2*h
            list.append(u0)
            continue
        if abs(S) > e:
            u0 = tmp_u0
            u0_2 = tmp_u0_2
            x = tmp_x
            x_2 = tmp_x_2
            h = h/2
            continue

    return x, list


#print(RK_Method_With_ce(1000,x,x_2,u0,u0_2,e,h)[0],'\n',RK_Method_With_ce(10000,x,x_2,u0,u0_2,e,h)[0], RK_Method_With_ce(1000,x,x_2,u0,u0_2,e,h)[0] - RK_Method_With_ce(10000,x,x_2,u0,u0_2,e,h)[0])

#print(RK_Method_Without_ce(100, x, u0, h)[1])

x = np.linspace(0, round(RK_Method_halfhope_Without_ce(100, x, u0, h)[0]), round(RK_Method_halfhope_Without_ce(100, x, u0, h)[0]*int(1/h)))
plt.plot(RK_Method_halfhope_Without_ce(100,x,u0,h)[0], RK_Method_Without_ce(100, x, u0, h)[1], 'r')
plt.plot(RK_Method_halfhope_Without_ce(100, x, u0, h)[0], RK_Method_halfhope_Without_ce(100, x, u0, h)[1], 'y')

#plt.plot(x1, u, 'g')

#plt.show()
