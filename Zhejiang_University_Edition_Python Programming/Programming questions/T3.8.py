'''
输入一个字符串，对该字符串进行逆序，输出逆序后的字符串。
输入格式：

输入在一行中给出一个不超过80个字符长度的、以回车结束的非空字符串。
输出格式：

在一行中输出逆序后的字符串。
'''
source = input()
output = ''
for i in source:
    output = i + output
print(output)
# 只要反向加字符串就可以了
