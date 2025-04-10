# 变量
age = 13
name = 'john'
print(name)

# 字符串切片
msg = "Hello, World!"
print(msg[2:5]) # llo

# 列表
mylist = []
mylist.append(1)
mylist.append(2)
for item in mylist:
    print(item) # 打印输出 1,2

# 判断
num = 200
if num > 0 :
    print("num is greater than 0")
else:
    print("num is less than 0")

# 循环
for item in range(6):
    if item == 3: break
    print(item)
else:
    print("Finally finished!")


# 函数
def my_function():
    print('来自函数的你好')
my_function()

# 文件处理
with open('C:/TEXT.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line)

# 算术
result = 10 + 30
print(result)

# 加等于
counter = 0
counter += 10
print(counter)

# f-字符串
website = 'Quick Reference'
print(f"Hello, {website}")

# 数据类型

# 字符串
hello = "Hello World"
multi_string = """Multiline Strings
Lorem ipsum dolor sit amet,
consectetur adipiscing elit """
print(multi_string)

# 数值
x = 1    # 整数
y = 2.8  # 浮点小数
z = 1j   # 复数
print(type(x)) # <class 'int'>
print(type(y)) # <class 'float'>
print(type(z)) # <class 'complex'>

# 布尔值
my_bool = True
my_bool1 = False
print(bool(0))  # => False
print(bool(1))  # => True

# 列表
list1 = [1, 2, 3]
list2 = ['apple','cherry','orange']
print(list1)
print(list2)

# 元组：类似列表，但自身不可变
my_tuple = (1, 2, 3)
my_tuple1 = tuple((1,2,3))
print(my_tuple)
print(my_tuple1)

# 集合：类似列表, 但里面的元素是无序而不重复的
set1 = {1, 2, 3}
set2 = set((4,5,6))
print(set1)
print(set2)


# 字典：键-值对。像JSON那种对象
empty_dict = {}
a = {'one':'字典1','two':'字典2','three':'字典3'}
print(a['one'])
print(a.keys())
print(a.values())
a.update({'four':'字典4'})
print(a.keys())

# 类型转换
# x = int(1)       # 得到 1
# y = int(2.8)     # 得到 2
# z = int("3")     # 得到 3

# 转换为字符串
x = str("s1")    # 得到 "s1"
y = str(2)       # 得到 "2"
z = str(3.0)     # 得到 "3.0"
print(x,y,z)


# ----- 字符串
hello = 'Hello, World'
print(hello[1]) # 获取第二个字符 e
print(hello[-1])  # 获取倒数第一个字符 d

# 获取长度 len() 函数返回字符串的长度
print(len(hello)) # 12

# 重复多次
s = '===+'
n = 3
print(s * n) # ===+===+===+

# 存在性判断 判断 "spam" 这个字符串是否在其它字符串里
s = 'spam'
isSpam = s in 'I saw spamalot!'
isNot = s not in 'I saw not!'
print(isSpam) # True
print(isNot) # True

# 字符串拼接 可以使用加号进行拼接
s = 'spam'
t = 'egg'
print(s + t) # spamegg

# 切割字符串
s = 'mybacon'
print(s[2:5]) # bac
print(s[0:2]) # my
print(s[:2]) # my
print(s[2:]) # bacon
print(s[-5:-1]) # baco
print(s[::5]) # 步长 mo

# 插入分隔符拼接
str1 = "-".join(["John", "Peter", "Vicky"])
print(str1) # John-Peter-Vicky

# 头尾判断
isStart = 'hello'.startswith('h')
isStart1 = 'hello'.startswith('e')
print(isStart) # True
print(isStart1) # False
isEnd = 'hello'.endswith('o')
print(isEnd)  # True

# 循环
for char in 'foo':
    print(char)

# f-字符串（Python 3.6+）
website = 'Reference'
print(f"HELLO, {website}") # "Hello, Reference"

num = 10
print(f'{num} + 10 = {num + 10}') # '10 + 10 = 20'

# 填充对齐
# 使用空格填充到指定长度
print(f'{"text":10}')
# 向左填充
print(f'{"text":*>10}')
# 向右填充
print(f'{"text":*<10}')
# 居中填充
print(f'{"text":*^10}') # '***test***'
# 使用数字填充
print(f'{12345:0>10}') # '0000012345'

# 负数
print(f'{-12345:0=10}') # -000012345

import math
print(f'{math.pi:.2f}') # '3.14'

# 分组选项
print(f'{100000:,.2f}') # 100,000.00

# 百分比
print(f'{0.25:.0%}') # 25%

# 科学计数法
print(f'{345600000000:e}') # 3.456000e+11
