'''
本题目要求计算下列分段函数f(x)的值：

输入格式:

输入在一行中给出实数x。
输出格式:

在一行中按“f(x) = result”的格式输出，其中x与result都保留一位小数。
'''

x=float(input())
if x==0:
    print("f(0.0) = 0.0")
else:
    print("f({0:.1f}) = {1:.1f}".format(x,1/x))