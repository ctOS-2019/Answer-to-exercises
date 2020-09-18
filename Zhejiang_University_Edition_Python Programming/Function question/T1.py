'''
给定两个均不超过9的正整数a和n，要求编写函数fn(a,n) 求a+aa+aaa++⋯+aa⋯aa(n个a）之和，fn须返回的是数列和

/* 请在这里填写答案 */
a,b=input().split()
s=fn(int(a),int(b))
print(s)
'''


def fn(a, b):
    sum = 0
    c = 0
    for i in range(b):
        c += 1
        num = ''
        for d in range(c):
            num += str(a)
        sum += int(num)
    return sum
