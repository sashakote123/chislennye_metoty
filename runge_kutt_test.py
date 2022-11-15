import numpy as np
import matplotlib.pyplot as plt
import math


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
    x_list = []
    y_list = []
    for i in range(N):
        y_list.append(u0)
        x_list.append(x)
        u0 = func_RK(x, u0, h)
        x = x + h
    return x_list, y_list


def RK_Method_halfhope_Without_ce(N, x, u0, h):
    x_list = []
    list = []
    for i in range(N):
        list.append(u0)
        x_list.append(x)
        u0 = func_RK(x, u0, h / 2)
        x = x + h / 2
        u0 = func_RK(x, u0, h / 2)
        x = x + h / 2
    return x_list, list


def RK_Method_With_ce(N, X0, U0, h, eps):
    b = 5
    i = 1
    c1 = 0
    c2 = 0
    List = [[X0, U0, 0, 0, h, c1, c2]]
    while (i < N):
        y1 = func_RK(List[-1][0], List[-1][1], h)
        x1 = List[-1][0] + h

        y2 = func_RK(List[-1][0], List[-1][1], h / 2)
        x2 = List[-1][0] + h / 2
        y2 = func_RK(x2, y2, h / 2)
        x2 = x2 + h / 2

        s = (y2 - y1) / (2 ** 4 - 1)
        if (eps / (2 ** 5) <= abs(s)) and (abs(s) <= eps):
            List.append([x1, y1, y1 - y2, s, h, c1, c1])
        else:
            if (abs(s) < eps / (2 ** 5)):
                c2 += 1
                h = 2 * h
                List.append([X0, U0, U0 - y2, s, h, c1, c1])
            else:
                h = h / 2
                c1 += 1
        i += 1

    x_list = []
    y_list = []
    h_list = []
    y1y2_list = []
    S_list = []
    c1_list = []
    c2_list = []

    j = 0
    while j != len(List):
        x_list.append(List[j][0])
        y_list.append(List[j][1])
        h_list.append(List[j][4])
        y1y2_list.append(List[j][2])
        S_list.append(List[j][3])
        c1_list.append(List[j][5])
        c2_list.append(List[j][6])
        j += 1

    return x_list, y_list, h_list, y1y2_list, S_list, c1_list, c2_list


