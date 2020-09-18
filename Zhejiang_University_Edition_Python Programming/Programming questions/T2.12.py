'''
本题要求编写程序，根据输入的三角形的三条边a、b、c，计算并输出面积和周长。注意：在一个三角形中， 任意两边之和大于第三边。三角形面积计算公式：area=√​s(s−a)(s−b)(s−c)​​​，其中s=(a+b+c)/2。
输入格式：

输入为3个正整数，分别代表三角形的3条边a、b、c。
输出格式：

如果输入的边能构成一个三角形，则在一行内，按照

area = 面积; perimeter = 周长

的格式输出，保留两位小数。否则，输出

These sides do not correspond to a valid triangle
'''
list = []
for i in input().split(' '):
    list.append(int(i))
list.sort()
a, b, c = list
if a + b > c:
    s = (a + b + c) / 2
    len = a + b + c
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print('area = {0:.2f}; perimeter = {1:.2f}'.format(area, len))
else:
    print('These sides do not correspond to a valid triangle')