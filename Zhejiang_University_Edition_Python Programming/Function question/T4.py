'''
本题要求实现一个计算Fibonacci数的简单函数，并利用其实现另一个函数,输出两正整数m和n（0<m<n≤100000）之间的所有Fibonacci数的数目。 所谓Fibonacci数列就是满足任一项数字是前两项的和（最开始两项均定义为1）的数列,fib(0)=fib(1)=1。其中函数fib(n)须返回第n项Fibonacci数；函数PrintFN(m,n)用列表返回[m, n]中的所有Fibonacci数。
函数接口定义：

在这里描述函数接口。例如：
fib(n),返回fib(n)的值
PrintFN(m,n)，用列表返回[m, n]中的所有Fibonacci数。

裁判测试程序样例：

在这里给出函数被调用进行测试的例子。例如：
/* 请在这里填写答案 */

m,n,i=input().split()
n=int(n)
m=int(m)
i=int(i)
b=fib(i)
print("fib({0}) = {1}".format(i,b))
fiblist=PrintFN(m,n)
print(len(fiblist))
'''


def fib(i):
    if i == 0 or i == 1:
        return 1
    else:
        return fib(i - 1) + fib(i - 2)


# 一个简单的递归函数

def PrintFN(m, n):
    a = 0
    list = []
    while True:
        fiba = fib(a)
        if fiba > n:
            return list
        if fiba >= m:
            list.append(fiba)
        a += 1


m, n, i = input().split()
n = int(n)
m = int(m)
i = int(i)
b = fib(i)
print("fib({0}) = {1}".format(i, b))
fiblist = PrintFN(m, n)
print(len(fiblist))
