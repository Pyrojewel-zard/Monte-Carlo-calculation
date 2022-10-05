# -*- coding:utf-8 -*-
# 蒙特卡洛+自适应迭代
# 不懂想法是不是对的，不过我的想法是，上一次的迭代结果和这一次的迭代结果之间，进行差值比较，如果差值小于设定精度，就停止迭代,并输出结果,第一版应进行不画图只计算
import numpy as np
import matplotlib.pyplot as plt
import math

cal_e=1e-5  #设定精度
cal_n=40    #初次迭代点数

def f(x):   #被积函数
    return x**2+np.cos(x)   