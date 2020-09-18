'''
给定两个均不超过9的正整数a和n，要求编写程序求a+aa+aaa++⋯+aa⋯a（n个a）之和。
输入格式：

输入在一行中给出不超过9的正整数a和n。
输出格式：

在一行中按照“s = 对应的和”的格式输出。
'''

list1=input().split(" ")
a=list1[0]
n=int(list1[1])
s=0
for i in range(n):
    num=""
    for y in range(i+1):
        num+=a
    s+=int(num)
print("s = {0}".format(s))