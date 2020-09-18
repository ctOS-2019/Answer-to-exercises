'''
输入一个字符串，再输入两个字符，求这两个字符在字符串中的索引。
输入格式:

第一行输入字符串
第二行输入两个字符，用空格分开。
输出格式:

反向输出字符和索引，即最后一个最先输出。每行一个。
'''
sentence=input()
keyword=[]
for i in input().split():
    keyword.append(i)
for i in keyword[-1::-1]:
    pos=len(sentence)
    for a in sentence[-1::-1]:
        pos-=1
        if a == i:
            print('{0} {1}'.format(pos,i))