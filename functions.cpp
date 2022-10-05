#include<stdio.h>
#include<stdlib.h>
extern "C"{
//梯形法
double trapezoid(double a, double b, int n)
{
    double (*f)(double x) = [](double x) {return 1 / (1 + x * x); };
    double h = (b - a) / n;
    double s = 0.5 * (f(a) + f(b));
    for (int i = 1; i < n; i++)
    {
        s += f(a + i * h);
    }
    return s * h;
}
//辛普森法
double simpson(double a, double b, int n)
{
    double (*f)(double x) = [](double x) {return 1 / (1 + x * x); };
    double h = (b - a) / n;
    double s = f(a) + f(b);
    for (int i = 1; i < n; i += 2)
    {
        s += 4 * f(a + i * h);
    }
    for (int i = 2; i < n - 1; i += 2)
    {
        s += 2 * f(a + i * h);
    }
    return s * h / 3;
}
//一维高斯积分
double gauss(double a, double b, int n)
{
    double (*f)(double x) = [](double x) {return 1 / (1 + x * x); };
    double x[5] = { 0.9061798459, 0.5384693101, 0, -0.5384693101, -0.9061798459 };
    double w[5] = { 0.2369268851, 0.4786286705, 0.5688888889, 0.4786286705, 0.2369268851 };
    double s = 0;
    for (int i = 0; i < n; i++)
    {
        s += w[i] * f((b - a) * x[i] / 2 + (a + b) / 2);
    }
    return s * (b - a) / 2;
}

//一维分区间高斯积分
double gauss2(double a, double b, int n)
{
    double (*f)(double x) = [](double x) {return 1 / (1 + x * x); };
    double x[5] = { 0.9061798459, 0.5384693101, 0, -0.5384693101, -0.9061798459 };
    double w[5] = { 0.2369268851, 0.4786286705, 0.5688888889, 0.4786286705, 0.2369268851 };
    double s = 0;
    double h = (b - a) / n;
    for (int i = 0; i < n; i++)
    {
        double a1 = a + i * h;
        double b1 = a + (i + 1) * h;
        for (int j = 0; j < 5; j++)
        {
            s += w[j] * f((b1 - a1) * x[j] / 2 + (a1 + b1) / 2);
        }
    }
    return s * h / 2;

}
}
int main(){
    printf("高斯法积分结果为：%lf", gauss2(0, 1, 5));
    return 0;
}
//g++ -o libpycallcpp.dll -shared -fPIC functions.cpp