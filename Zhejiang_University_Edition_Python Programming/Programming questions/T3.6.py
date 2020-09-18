'''
本题要求统计一个整型序列中出现次数最多的整数及其出现次数。
输入格式：

输入在一行中给出序列中整数个数N（0<N≤1000），以及N个整数。数字间以空格分隔。
输出格式：

在一行中输出出现次数最多的整数及其出现次数，数字间以空格分隔。题目保证这样的数字是唯一的。
'''
dict = {}
list = input().split()
for i in list[1:]:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
for key, value in dict.items():
    if value == max(dict.values()):
        print(key, value)
        break
# 并不是很理解提供的<项数>有什么用，也许是拿来写更简便代码的
