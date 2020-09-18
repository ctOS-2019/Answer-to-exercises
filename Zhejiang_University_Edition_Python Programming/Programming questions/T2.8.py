'''
输入一个整数和进制，转换成十进制输出
输入格式:

在一行输入整数和进制
输出格式:

在一行十进制输出结果
'''
source=input().split(",")
out=int(source[0],int(source[1]))
print(out)