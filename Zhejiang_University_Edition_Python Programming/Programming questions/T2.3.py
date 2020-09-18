'''
为了提倡居民节约用电，某省电力公司执行“阶梯电价”，安装一户一表的居民用户电价分为两个“阶梯”：月用电量50千瓦时（含50千瓦时）以内的，电价为0.53元/千瓦时；超过50千瓦时的，超出部分的用电量，电价上调0.05元/千瓦时。请编写程序计算电费。
输入格式:

输入在一行中给出某用户的月用电量（单位：千瓦时）。
输出格式:

在一行中输出该用户应支付的电费（元），结果保留两位小数，格式如：“cost = 应付电费值”；若用电量小于0，则输出"Invalid Value!"。
'''

value=int(input())
if value<=50 and value>=0:
    cost = value*0.53
elif value>50:
    cost = 50*0.53+(value-50)*(0.53+0.05)
else:
    cost = False
if cost:
    print("cost = {0:.2f}".format(cost))
else:
    print("Invalid Value!") 