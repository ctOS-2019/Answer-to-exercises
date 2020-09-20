'''
本题要求实现一个函数，用下列公式求cos(x)近似值，精确到最后一项的绝对值小于eps（绝对值小于eps的项不要加）：

cos (x) = x^0 / 0! - x^2 / 2! + x^4 / 4! - x^6 / 6! + ?

函数接口定义：funcos(eps,x ),其中用户传入的参数为eps和x；函数funcos应返回用给定公式计算出来，保留小数4位。
函数接口定义：

函数接口:
funcos(eps,x ),返回cos(x)的值。

裁判测试程序样例：

在这里给出函数被调用进行测试的例子。例如：


/* 请在这里填写答案 */

eps=float(input())
x=float(input())
value=funcos(eps,x )
print("cos({0}) = {1:.4f}".format(x,value))
'''


def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result


def funcos(eps, x):
    answer = 0
    tag = 1
    i = 0
    while True:
        step = tag * (x ** i) / factorial(i)
        if abs(step) < eps:
            return answer
        answer += step
        tag = -tag
        i += 2


eps = float(input())
x = float(input())
value = funcos(eps, x)
print("cos({0}) = {1:.4f}".format(x, value))
