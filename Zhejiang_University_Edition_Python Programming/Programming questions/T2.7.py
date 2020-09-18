'''
读入2个正整数A和B，1<=A<=9, 1<=B<=10,产生数字AA...A,一共B个A
输入格式:

在一行中输入A和B。
输出格式:

在一行中输出整数AA...A,一共B个A
'''

before=input()
after=""
for i in before:
    if i == " ":
        continue
    else:
        after+=i
list1=after.split(",")
a=list1[0]
b=int(list1[1])
sum=""
for i in range(b):
    sum+=a
print(int(sum))