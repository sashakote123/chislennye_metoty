import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate


def func(x, u):
    f = (np.log(x + 1) / (x ** 2 + 1)) * u**2 + u - u**3 * np.sin(10 * x)
    return f


def rk_4(xk, vk, hk):
    x = xk + hk
    k1 = func(xk, vk)
    k2 = func(xk + hk / 2, vk + hk / 2 * k1)
    k3 = func(xk + hk / 2, vk + hk / 2 * k2)
    k4 = func(xk + hk, vk + hk * k3)
    v = vk + hk / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return x, v


eps = 1e-12
h = 0.0001
x0 = 0
u0 = 0.1
N = 10000
b = 5
c1 = 0
c2 = 0
max_e = 0
max_h = h
max_h_x = 0
min_h = h
min_h_x = 0
i = 1
List = [[x0, u0, 0, 0, 0, h, c1, c2]]

while (i < N) and (List[-1][0] < b):
    x1, v1 = rk_4(List[-1][0], List[-1][1], h)
    x2, v2 = rk_4(List[-1][0], List[-1][1], h/2)
    x2, v2 = rk_4(x2, v2, h/2)
    v3 = v1 - v2
    S = (v2 - v1)/(2**4-1)
    e = S * 2**4
    if max_e < abs(e):
        max_e = abs(e)

    if (eps/(2**5) <= abs(S)) and (abs(S) <= eps):
        List.append([x1, v1, v2, v3, e, h, c1, c2])
    else:
        if (abs(S)) < (eps/(2**5)):
            c2 += 1
            h = 2 * h
            if max_h < h:
                max_h = h
                max_h_x = x1
            List.append([x1, v1, v2, v3, e, h, c1, c2])
        else:
            h = h/2
            if min_h > h:
                min_h = h
                min_h_x = x1
            c1 += 1
    i += 1

row_names = ["xi", "vi", "v2i", "vi - v2i", "ОЛП", "hi", "c1", "c2"]
print(tabulate(List, headers=row_names, tablefmt="fancy_grid", showindex="always"))
print("n =", len(List))
print("b-xn =", b-List[-1][0])
print("max ОЛП =", max_e)
print("count c1 =", List[-1][6])
print("count c2 =", List[-1][7])
print("max hi =", max_h, "при x =", max_h_x)
print("min hi =", min_h, "при x =", min_h_x)

x_list = []
y_list = []
j = 0
while j != len(List):
    x_list.append(List[j][0])
    y_list.append(List[j][1])
    j += 1

plt.plot(x_list, y_list, "b")
plt.axis([0, 5, 0, 10])
#plt.show()