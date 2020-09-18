'''
本题要求对两个正整数m和n（m≤n）编写程序，计算序列和m​2​​+1/m+(m+1)​2​​+1/(m+1)+⋯+n​2​​+1/n。
输入格式:

输入在一行中给出两个正整数m和n（m≤n），其间以空格分开。
输出格式:

在一行中按照“sum = S”的格式输出部分和的值S，精确到小数点后六位。题目保证计算结果不超过双精度范围。
'''
m,n=input().split()
m=int(m)
n=int(n)
sum=0
tag=True
for i in range(m,n+1):
    sum+=i**2+1/i
print('sum = {0:.6f}'.format(sum))