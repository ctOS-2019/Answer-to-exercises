'''
输入一个以#结束的字符串，本题要求滤去所有的非十六进制字符（不分大小写），组成一个新的表示十六进制数字的字符串，然后将其转换为十进制数后输出。如果在第一个十六进制字符之前存在字符“-”，则代表该数是负数。
输入格式：

输入在一行中给出一个以#结束的非空字符串。
输出格式：

在一行中输出转换后的十进制数。题目保证输出在长整型范围内。
'''
source=input()
sortstr=''
first = True
flag = False
for i in range(len(source)):
    if '0'<=source[i]<='9' or 'a'<=source[i]<='f' or 'A'<=source[i]<='F':
        sortstr += source[i]
        if first and i > 0:
            first=False
            for i in source[:i]:
                if i == '-':
                    flag=True
try:
    output = str(int('0x{0}'.format(sortstr), 16))
    if flag:
        print('-' + output)
    else:
        print(output)
except:
    print(0)