# -*- coding:utf-8 -*-
# 蒙特卡洛+自适应迭代
# 不懂想法是不是对的，不过我的想法是，上一次的迭代结果和这一次的迭代结果之间，进行差值比较，如果差值小于设定精度，就停止迭代,并输出结果,第一版应进行不画图只计算
# f(x)=x^2+cos(x),
# 积分上下限:a=-3,b=2
import numpy as np
import matplotlib.pyplot as plt
import docx

cal_e=1e-5  #设定精度
cal_n=40    #初次迭代点数

def f(x):   #被积函数
    return x**2+np.cos(x+2)

def ff(x):  #积分上下限归一化,积分结果*area-1再*5
    b=3
    a=-2
    xx=(b-a)*x+a
    return f(xx)+1
   
def MonteCarlo(n):  #蒙特卡洛计算单次迭代,n为点数
    x=np.arange(0,1,1/n)
    y=ff(x)
    x_list = np.random.random((1, n)) * 1
    y_list = np.random.random((1, n)) * 11
    yy_list = ff(x_list)
    list = (yy_list-y_list)
    num = 0
    # print(len(x))
    for i in range(len(x)):
        if list[0, i]>0:
            num +=1
    return num/n
    
def createTable(doc,table):
    
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = '迭代次数'
    hdr_cells[1].text = '迭代点数'
    hdr_cells[2].text = '迭代结果'
    hdr_cells[3].text = '积分结果'
    return doc,table

def add_Data_to_Table(doc,table,data):
    cal=20
    for i in range(data.size):
        cal*=2
        row_cells = table.add_row().cells
        row_cells[0].text = str(i+1)
        row_cells[1].text = str(cal)
        row_cells[2].text = str(data[i])
        row_cells[3].text = str((data[i]*11-1)*5)
    doc.save('MonteCarlo.docx')
    return doc,table

def plot_convergence(M_equal):
    x=np.arange(0,M_equal.size,1)
    plt.plot(x,M_equal,'r')
    plt.savefig('./test2.jpg')
    plt.show()

if __name__ == '__main__':
    M_equal=np.array([])
    N=cal_n #迭代点数
    M1=MonteCarlo(N)
    M2=MonteCarlo(N)
    M_equ=(M1+M2)/2
    n=1
    print("初次迭代结果为：",M_equ)
    if abs(M1-M2)<cal_e:
        print("精度满足，迭代结束，结果为：",M_equ)
    while True:
        N*=2
        n+=1
        M1=MonteCarlo(N)
        M_equ=(M_equ+M1)/2
        M_equal=np.append(M_equal,M_equ)
        print("迭代次数为：",n,"迭代结果为：",M_equ)
        if abs(M1-M_equ)<cal_e:
            print("精度满足，迭代结束")
            break
    print("最终结果为：",M_equ)
    doc = docx.Document()
    table = doc.add_table(rows=1, cols=4,style="Table Grid")
    createTable(doc,table)
    add_Data_to_Table(doc,table,M_equal)
    plot_convergence(M_equal)

