# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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

print(RK_Method_Without_ce_main_1(100, x0, u0, h)[0])
print(RK_Method_Without_ce_main_1(100, x0, u0, h)[1])


'''''
def RK_Method_Without_ce_main_1(N,x0,u0,h):
    i = 1
    while (i < N) & (List[-1][0] < b):
        x, v = rk_4(List[-1][0], List[-1][1], h)
        List.append([x, v])
        i += 1

    row_names = ["xi", "vi"]
    #print(tabulate(List, headers=row_names, tablefmt="fancy_grid", showindex="always"))

    x_list = []
    y_list = []


    j = 1
    while j != i:
        x_list.append(List[j][0])
        y_list.append(List[j][1])
        j += 1

    #print(len(x_list))
    #print(len(y_list))
    return x_list, y_list
print((RK_Method_Without_ce_main_1(100, x0, u0, h)[0]))
print((RK_Method_Without_ce_main_1(100, x0, u0, h)[1]))
'''''

plt.plot(RK_Method_Without_ce_main_1(500, x0, u0, h)[0],RK_Method_Without_ce_main_1(500, x0, u0, h)[1])
plt.axis([0, 5, 0, 10])
#plt.show()