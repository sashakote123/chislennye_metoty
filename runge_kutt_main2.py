import math
import matplotlib.pyplot as plt
import numpy as np

class RK:
    def __init__(self, a, u0, dudt0, h=0.0001, control=False, e=0):
        self.a = a
        self.u = u0
        self.dudt = dudt0
        self.h = h
        self.x = 0
        self.c = control
        self.e = e
        self.C1 = 0
        self.C2 = 0
        self.ud2 = 0
        self.s = 0

    def f2(self, x, u1, u2):
        return self.a * math.sqrt(u2 ** 2 + 1)

    def f1(self, x, u1, u2):
        return u2

    def step(self):
        if (self.c):
            self.ctrl()
        else:
            x = self.x
            u = self.u
            dudt = self.dudt
            h = self.h
            k1 = self.f1(x, u, dudt)
            q1 = self.f2(x, u, dudt)
            k2 = self.f1(x + h / 4, u + (h / 4) * k1, dudt + (h / 4) * q1)
            q2 = self.f2(x + h / 4, u + (h / 4) * k1, dudt + (h / 4) * q1)
            k3 = self.f1(x + h / 2, u + (h / 2) * k2, dudt + (h / 2) * q2)
            q3 = self.f2(x + h / 2, u + (h / 2) * k2, dudt + (h / 2) * q2)
            k4 = self.f1(x + h, u + h * (k1 - 2 * k2 + 2 * k3), dudt + h * (q1 - 2 * q2 + 2 * q3))
            q4 = self.f2(x + h, u + h * (k1 - 2 * k2 + 2 * k3), dudt + h * (q1 - 2 * q2 + 2 * q3))
            self.u += (h / 6) * (k1 + 4 * k3 + k4)
            self.dudt += (h / 6) * (q1 + 4 * q3 + q4)
            self.x += h

    def ctrl(self):
        x = self.x
        u = self.u
        dudt = self.dudt
        h = self.h
        k1 = self.f1(x, u, dudt)
        q1 = self.f2(x, u, dudt)
        k2 = self.f1(x + h / 4, u + (h / 4) * k1, dudt + (h / 4) * q1)
        q2 = self.f2(x + h / 4, u + (h / 4) * k1, dudt + (h / 4) * q1)
        k3 = self.f1(x + h / 2, u + (h / 2) * k2, dudt + (h / 2) * q2)
        q3 = self.f2(x + h / 2, u + (h / 2) * k2, dudt + (h / 2) * q2)
        k4 = self.f1(x + h, u + h * (k1 - 2 * k2 + 2 * k3), dudt + h * (q1 - 2 * q2 + 2 * q3))
        q4 = self.f2(x + h, u + h * (k1 - 2 * k2 + 2 * k3), dudt + h * (q1 - 2 * q2 + 2 * q3))
        u1 = u + (h / 6) * (k1 + 4 * k3 + k4)
        dudt1 = dudt + (h / 6) * (q1 + 4 * q3 + q4)
        htmp = h / 2
        k1 = self.f1(x, u, dudt)
        q1 = self.f2(x, u, dudt)
        k2 = self.f1(x + htmp / 4, u + (htmp / 4) * k1, dudt + (htmp / 4) * q1)
        q2 = self.f2(x + htmp / 4, u + (htmp / 4) * k1, dudt + (htmp / 4) * q1)
        k3 = self.f1(x + htmp / 2, u + (htmp / 2) * k2, dudt + (htmp / 2) * q2)
        q3 = self.f2(x + htmp / 2, u + (htmp / 2) * k2, dudt + (htmp / 2) * q2)
        k4 = self.f1(x + htmp, u + htmp * (k1 - 2 * k2 + 2 * k3), dudt + htmp * (q1 - 2 * q2 + 2 * q3))
        q4 = self.f2(x + htmp, u + htmp * (k1 - 2 * k2 + 2 * k3), dudt + htmp * (q1 - 2 * q2 + 2 * q3))
        u2 = u + (htmp / 6) * (k1 + 4 * k3 + k4)
        dudt2 = dudt + (htmp / 6) * (q1 + 4 * q3 + q4)
        k1 = self.f1(x, u2, dudt2)
        q1 = self.f2(x, u2, dudt2)
        k2 = self.f1(x + htmp / 4, u2 + (htmp / 4) * k1, dudt2 + (htmp / 4) * q1)
        q2 = self.f2(x + htmp / 4, u2 + (htmp / 4) * k1, dudt2 + (htmp / 4) * q1)
        k3 = self.f1(x + htmp / 2, u2 + (htmp / 2) * k2, dudt2 + (htmp / 2) * q2)
        q3 = self.f2(x + htmp / 2, u2 + (htmp / 2) * k2, dudt2 + (htmp / 2) * q2)
        k4 = self.f1(x + htmp, u2 + htmp * (k1 - 2 * k2 + 2 * k3), dudt2 + htmp * (q1 - 2 * q2 + 2 * q3))
        q4 = self.f2(x + htmp, u2 + htmp * (k1 - 2 * k2 + 2 * k3), dudt2 + htmp * (q1 - 2 * q2 + 2 * q3))
        self.ud2 = u2 + (htmp / 6) * (k1 + 4 * k3 + k4)
        self.s = abs(u1 - self.ud2) / 15
        e = self.e
        if (self.s > e):
            self.h /= 2
            self.C1 += 1
            self.ctrl()
        else:
            self.x += h
            self.u = u1
            self.dudt = dudt1
            if (self.s < e / 32):
                self.h *= 2
                self.C2 += 1

    def get_data(self):
        return [self.x, self.u, self.ud2, self.u - self.ud2, self.s, self.h, self.C1, self.C2]


# Пример использования



def RK_Method_Without_ce_main_2(N,x0,u0,h):
    cl = RK(x0, u0, 3, h, control=False, e=0.00001)
    listx = []
    list = []
    for i in range(N):
        cl.step()
        s = cl.get_data()
        #print(s[0], '         ', s[1])
        listx.append(s[0])
        list.append(s[1])
        if (s[0] > 5):
            break
    return listx, list

h = 0.001
x0 = 2
u0 = 1
N = 100
b = 5

#print(RK_Method_Without_ce_main_2(1000, x0, u0, h)[0])
#print(RK_Method_Without_ce_main_2(1000, x0, u0, h)[1])
plt.plot(RK_Method_Without_ce_main_2(1000, x0, u0, h)[0], RK_Method_Without_ce_main_2(1000, x0, u0, h)[1])
#plt.show()
