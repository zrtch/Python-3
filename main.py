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