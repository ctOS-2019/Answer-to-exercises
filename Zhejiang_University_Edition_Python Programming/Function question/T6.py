'''
缩写词是由一个短语中每个单词的第一个字母组成，均为大写。例如，CPU是短语“central processing unit”的缩写。
函数接口定义：

acronym(phrase);
phrase是短语参数，返回短语的缩写词

裁判测试程序样例：


/* 请在这里填写答案 */

phrase=input()
print(acronym(phrase))
输入样例：

central  processing  unit

输出样例：

CPU
'''

def acronym(phrase):
    output=''
    for i in phrase.split():
        first_str=i[0]
        if first_str.isupper():
            output+=first_str
        else:
            output+=first_str.upper()
    return output

phrase=input()
print(acronym(phrase))