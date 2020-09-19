'''
第6章函数-3 使用函数统计指定数字的个数 (20分)

本题要求实现一个统计整数中指定数字的个数的简单函数。

CountDigit(number,digit )

其中number是整数，digit为[1, 9]区间内的整数。函数CountDigit应返回number中digit出现的次数。
函数接口定义：

在这里描述函数接口。例如：
CountDigit(number,digit ),返回digit出现的次数

裁判测试程序样例：


/* 请在这里填写答案 */

number,digit=input().split()
number=int(number)
digit=int(digit)
count=CountDigit(number,digit )
print("Number of digit 2 in "+str(number)+":",count)
'''
def CountDigit(number,digit):
    count = 0
    number=str(number)
    digit=str(digit)
    for i in number:
        if digit == i:
            count += 1
    return count
# 这int又str回来，有点浪费计算资源
number,digit=input().split()
number=int(number)
digit=int(digit)
count=CountDigit(number,digit )
print("Number of digit 2 in "+str(number)+":",count)