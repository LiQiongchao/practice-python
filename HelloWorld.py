#!/use/bin/python3
import sys
from sys import argv,path

x = "hello world"; sys.stdout.write(x + "\n");
'''
多行注释
'''
"""
多行注释
"""
name = "job";
print("hello " + name)

# * 2 表示会输出再次
print("I'm a boy.\n" * 2)

a = b = c = 2
d = a + \
    b + \
    c
print("d value is:" + str(d))

# 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
firstName = """DiveIsGood"""
lastName = "Mike"

print(firstName)
# 截取到倒数第二个
print(firstName[0:-1])
print(firstName[4:8])
print(firstName[4:])
# 输出 D v
print(firstName[0:4:2])

# 字符前面加r不会转义
print("hello \n bob")
print(r"hello \n bob")

# 不换行输出
print("hello, we are ", end="-> ")
print("brother", end="")

# from sys import argv,path 从某模块导入函数
print("path:", path)



