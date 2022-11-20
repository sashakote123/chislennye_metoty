from typing import List, Any

import numpy as np
import matplotlib.pyplot as plt
import math
import numpy as np


def function(N, X0, U0, h):
    x = X0
    y = U0
    x_list = []
    y_list = []
    for i in range(N):
        x_list.append(x)
        y_list.append(y)
        x = x + h
        y = U0 * math.exp(3 * x)
    return x_list, y_list


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


def rk_4_test(x, u0, h):
    xs = x + h
    us = u0 + h / 6 * (func_k1(x, u0, h) + 2 * func_k2(x, u0, h) + 2 * func_k3(x, u0, h) + func_k4(x, u0, h))

    return xs, us


def RK_Method_With_ce_test_2(N, X0, U0, h, eps):
    b = 5
    c1 = 0
    c2 = 0
    max_e = 0
    max_h = h
    max_h_x = 0
    min_h = h
    min_h_x = 0
    i = 1
    List = [[X0, U0, 0, 0, 0, h, c1, c2]]

    while (i < N) and (List[-1][0] < b):
        x1, v1 = rk_4_test(List[-1][0], List[-1][1], h)
        x2, v2 = rk_4_test(List[-1][0], List[-1][1], h / 2)
        x2, v2 = rk_4_test(x2, v2, h / 2)
        v3 = v1 - v2
        S = (v2 - v1) / (2 ** 4 - 1)
        e = S * 2 ** 4
        if max_e < abs(e):
            max_e = abs(e)

        if (eps / (2 ** 5) <= abs(S)) and (abs(S) <= eps):
            List.append([x1, v1, v3, S, e, h, c1, c2])
        else:
            if (abs(S)) < (eps / (2 ** 5)):
                c2 += 1
                h = 2 * h
                if max_h < h:
                    max_h = h
                    max_h_x = x1
                List.append([x1, v1, v3, S, e, h, c1, c2])
            else:
                h = h / 2
                if min_h > h:
                    min_h = h
                    min_h_x = x1
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
        h_list.append(List[j][5])
        y1y2_list.append(List[j][2])
        S_list.append(List[j][3])
        c1_list.append(List[j][6])
        c2_list.append(List[j][7])
        j += 1
    return x_list, y_list, h_list, y1y2_list, S_list, c1_list, c2_list


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


def UiVi_without_ce(N, X0, U0, h):
    Ui_list = function(N, 0, U0, h)[1]
    Vi_list = RK_Method_Without_ce(N, X0, U0, h)[1]
    UiVi_list = []
    for i in range(N):
        UiVi_list.append(abs(Ui_list[i] - Vi_list[i]))
    return Ui_list, UiVi_list


def UiVi_with_ce(N, X0, U0, h, eps):
    Vi_list = RK_Method_With_ce_test_2(N, X0, U0, h, eps)[1]
    Xi_list = RK_Method_With_ce_test_2(N, X0, U0, h, eps)[0]
    Ui_list = []
    UiVi_list = []
    for i in range(len(Vi_list)):
        Ui_list.append(U0*math.exp(3 * (Xi_list[i]-X0)))
        UiVi_list.append(abs(Ui_list[i] - Vi_list[i]))
    return Ui_list, UiVi_list


print(UiVi_with_ce(100, 1, 1, 0.01, 0.0001)[0])
print(UiVi_with_ce(100, 1, 1, 0.01, 0.0001)[1])
