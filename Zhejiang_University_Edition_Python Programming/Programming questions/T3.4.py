'''
本题要求编写程序，从给定字符串中查找某指定的字符。
输入格式：

输入的第一行是一个待查找的字符。第二行是一个以回车结束的非空字符串（不超过80个字符）。
输出格式：

如果找到，在一行内按照格式“index = 下标”输出该字符在字符串中所对应的最大下标（下标从0开始）；否则输出"Not Found"。
'''
key = input()
target = input()
m = -1
for i in range(len(target)):
    if key == target[i:i + len(key)]:
        m = i
if m != -1:
    print('index = {0}'.format(m))
else:
    print('Not Found')
# 噢，实际上该代码还支持字符串查找
