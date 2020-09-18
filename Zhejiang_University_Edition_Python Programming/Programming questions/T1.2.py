'''
在同一行依次输入三个值a,b,c，用空格分开，输出 b*b-4*a*c的值
输入格式:

在一行中输入三个数。
输出格式:

在一行中输出公式值。
'''

source=input()
alllist=source.split(" ")
a=int(alllist[0])
b=int(alllist[1])
c=int(alllist[2])
print(b*b-4*a*c)