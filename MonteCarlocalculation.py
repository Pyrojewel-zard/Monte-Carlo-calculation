# -*- coding:utf-8 -*-
# 蒙特卡洛+自适应迭代
# 不懂想法是不是对的，不过我的想法是，上一次的迭代结果和这一次的迭代结果之间，进行差值比较，如果差值小于设定精度，就停止迭代,并输出结果,第一版应进行不画图只计算
# f(x)=x^2+cos(x),
# 积分上下限:a=-3,b=2
import numpy as np
import matplotlib.pyplot as plt
import math

cal_e=1e-5  #设定精度
cal_n=40    #初次迭代点数

def f(x):   #被积函数
    return x**2+np.cos(x+2)

def ff(x):  #积分上下限归一化,积分结果*area-1再*5
    b=3
    a=-2
    xx=5*x-2
    return f(xx)+1
   
def MonteCarlo(n):  #蒙特卡洛计算单次迭代,n为点数
    x=np.arange(0,1,1/n)
    y=ff(x)
    plt.plot(x,y,'r.')
    x_list=np.random.uniform(0,1,n)
    y_list=np.random.uniform
    


if __name__ == '__main__':
    N=cal_n #迭代点数
    M=MonteCarlo(N)
    n=1
    print("初次迭代结果为：",M-5)
    while True:
        N*=2
        n+=1
        M1=MonteCarlo(N)
        print("迭代次数为：",n,"迭代结果为：",M1)
        if abs(M1-M)<cal_e:
            print("精度满足，迭代结束")
            break
        else:
            M=M1
    print("最终结果为：",M1)
