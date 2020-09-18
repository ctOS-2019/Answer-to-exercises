'''
本题要求将输入的任意3个整数从小到大输出。
输入格式:

输入在一行中给出3个整数，其间以空格分隔。
输出格式:

在一行中将3个整数从小到大输出，其间以“->”相连。
'''
list1=input().split(" ")
list3=[]
for i in list1:
    list3.append(int(i))
list1=list3
list2=[]
while list1:
    MIN=list1[0]
    for i in list1:
        if i < MIN:
            MIN=i
    list2.append(str(MIN))
    list1.remove(MIN)
out="->".join(list2)
print(out)