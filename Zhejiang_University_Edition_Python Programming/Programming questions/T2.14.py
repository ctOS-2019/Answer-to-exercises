'''
给定两个整数A和B，输出从A到B的所有整数以及这些数的和。
输入格式：

输入在一行中给出2个整数A和B，其中−100≤A≤B≤100，其间以空格分隔。
输出格式：

首先顺序输出从A到B的所有整数，每5个数字占一行，每个数字占5个字符宽度，向右对齐。最后在一行中按Sum = X的格式输出全部数字的和X。
'''
list=[]
for i in input().split():
    list.append(int(i))
A,B=list
jump=0
sum=0
for i in range(A,B+1):
    jump+=1
    if jump!=5:
        print('{0:>5d}'.format(i),end='')
    else:
        jump=0
        print('{0:>5d}'.format(i))
    sum+=i
if jump != 0:
    print()
    print('Sum = {0}'.format(sum))
else:
    print('Sum = {0}'.format(sum))