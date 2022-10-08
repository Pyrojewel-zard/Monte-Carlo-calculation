import numpy as np
import matplotlib.pyplot as plt
import time
# 梯形法
def trapezoid_partition(f, a, b, n, m):
    h = (b - a) / m
    s = 0
    for i in range(m):
        s += trapezoid(f, a + i * h, a + (i + 1) * h, n)
    return s

## 梯形法
def trapezoid(f, a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return s * h

## 辛普森法
def simpson(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n - 1, 2):
        s += 2 * f(a + i * h)
    return s * h / 3

## 高斯积分
def gauss(f, a, b, n):
    if n == 1:
        x = [0]
        w = [2]
    elif n == 2:
        x = [-1 / np.sqrt(3), 1 / np.sqrt(3)]
        w = [1, 1]
    elif n == 3:
        x = [-np.sqrt(3 / 5), 0, np.sqrt(3 / 5)]
        w = [5 / 9, 8 / 9, 5 / 9]
    elif n == 4:
        x = [-np.sqrt((3 + 2 * np.sqrt(6 / 5)) / 7), -np.sqrt((3 - 2 * np.sqrt(6 / 5)) / 7), np.sqrt((3 - 2 * np.sqrt(6 / 5)) / 7), np.sqrt((3 + 2 * np.sqrt(6 / 5)) / 7)]
        w = [(18 - np.sqrt(30)) / 36, (18 + np.sqrt(30)) / 36, (18 + np.sqrt(30)) / 36, (18 - np.sqrt(30)) / 36]
    elif n == 5:
        x = [-np.sqrt(5 + 2 * np.sqrt(10 / 7)) / 3, -np.sqrt(5 - 2 * np.sqrt(10 / 7)) / 3, 0, np.sqrt(5 - 2 * np.sqrt(10 / 7)) / 3, np.sqrt(5 + 2 * np.sqrt(10 / 7)) / 3]
        w = [(322 - 13 * np.sqrt(70)) / 900, (322 + 13 * np.sqrt(70)) / 900, 128 / 225, (322 + 13 * np.sqrt(70)) / 900, (322 - 13 * np.sqrt(70)) / 900]
    s = 0
    for i in range(n):
        s += w[i] * f((b + a) / 2 + (b - a) / 2 * x[i])
    return s * (b - a) / 2

## 分区间高斯积分算法
def gauss_partition(f, a, b, n, m):
    h = (b - a) / m
    s = 0
    for i in range(m):
        s += gauss(f, a + i * h, a + (i + 1) * h, n)
    return s
class integration():    #这个类是用来计算积分的
    def __init__(self, f, a, b, n, m):
        self.f = f
        self.a = a
        self.b = b
        self.n = n
        self.m = m
    def accumulate(self):#这个函数是用来计算积分的
        pass
class trapezoidal(integration):
    def accumulate(self):
        return trapezoid(self.f, self.a, self.b, self.n)

class simpson_(integration):
    def accumulate(self):
        return simpson(self.f, self.a, self.b, self.n)

class gauss_(integration):
    def accumulate(self):
        return gauss(self.f, self.a, self.b, self.n)

class gauss_partition_(integration):
    def accumulate(self):
        return gauss_partition(self.f, self.a, self.b, self.n, self.m)


if __name__ == "__main__":

    def fun(x):
        return 1/(1+x**2)

    tol=1e-6
    

### 梯形法具体迭代过程
    n1=10
    res1=trapezoidal(fun,0,1,n1,0)
    while np.abs(res1.accumulate() - np.arctan(1))>tol:
        n1+=1
        res1=trapezoidal(fun,0,1,n1,0)
    print("梯形法计算结果：", res1.accumulate())
    print("梯形法计算节点",n1)
    time1=time.perf_counter()
    s1=trapezoidal(fun,0,1,n1,0)
    res = s1.accumulate()
    time2=time.perf_counter()
    print("梯形法计算用时",time2-time1)
    print("梯形法误差", np.abs(res - np.arctan(1)))


### 辛普森法具体迭代过程
    n2=1
    res2=simpson_(fun,0,1,n2,0)
    while np.abs(res2.accumulate() - np.arctan(1))>tol:
        n2+=1
        res2=simpson_(fun,0,1,n2,0)
    print("辛普森法计算结果：", res2.accumulate())
    print("辛普森法计算节点",n2)
    time3=time.perf_counter()
    s2=simpson_(fun,0,1,n2,0)
    res = s2.accumulate()
    time4=time.perf_counter()
    print("辛普森法计算用时",time4-time3)
    print("辛普森法误差", np.abs(res - np.arctan(1)))


    n3=1
    res3=gauss_(fun,0,1,n3,0)
    while np.abs(res3.accumulate() - np.arctan(1))>tol:
        n3+=1
        res3=gauss_(fun,0,1,n3,0)
    print("高斯积分计算结果：", res3.accumulate())
    print("高斯积分计算节点",n3)
    time5=time.perf_counter()
    s3=gauss_(fun,0,1,n3,0)
    res = s3.accumulate()
    time6=time.perf_counter()
    print("高斯积分计算用时",time6-time5)
    print("高斯积分误差", np.abs(res - np.arctan(1)))


    n4=1
    res4=gauss_partition_(fun,0,1,n4,20)
    while np.abs(res4.accumulate() - np.arctan(1))>tol:
        n4+=1
        res4=gauss_partition_(fun,0,1,n4,20)
    print("分区高斯积分计算结果：", res4.accumulate())
    print("分区高斯积分计算节点",n4)
    time7=time.perf_counter()
    s4=gauss_partition_(fun,0,1,n4,20)
    res = s4.accumulate()
    time8=time.perf_counter()
    print("分区高斯积分计算用时",time8-time7)
    print("分区高斯积分误差", np.abs(res - np.arctan(1)))
