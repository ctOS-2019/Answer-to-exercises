'''
本题要求提取一个字符串中的所有数字字符（'0'……'9'），将其转换为一个整数输出。
输入格式：

输入在一行中给出一个不超过80个字符且以回车结束的字符串。
输出格式：

在一行中输出转换后的整数。题目保证输出不超过长整型范围。
'''

source = input()
str_num = ''
for i in source:
    try:
        int(i)
    except:
        pass
    else:
        str_num += i
print(int(str_num))

# 我也不知道为什么最后一步要加个int
