# 变量

age = 13
name = "john"
print(name)

# 字符串切片
msg = "Hello, World!"
print(msg[2:5])  # llo

# 列表
mylist = []
mylist.append(1)
mylist.append(2)
for item in mylist:
    print(item)  # 打印输出 1,2

# 判断
num = 200
if num > 0:
    print("num is greater than 0")
else:
    print("num is less than 0")

# 循环
for item in range(6):
    if item == 3:
        break
    print(item)
else:
    print("Finally finished!")


# 函数
def my_function():
    print("来自函数的你好")


my_function()

# 文件处理
with open("C:/TEST.txt", "r", encoding="utf-8") as file:
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
website = "Quick Reference"
print(f"Hello, {website}")

# 数据类型

# 字符串
hello = "Hello World"
multi_string = """Multiline Strings
Lorem ipsum dolor sit amet,
consectetur adipiscing elit """
print(multi_string)

# 数值
x = 1  # 整数
y = 2.8  # 浮点小数
z = 1j  # 复数
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>

# 布尔值
my_bool = True
my_bool1 = False
print(bool(0))  # => False
print(bool(1))  # => True

# 列表
list1 = [1, 2, 3]
list2 = ["apple", "cherry", "orange"]
print(list1)
print(list2)

# 元组：类似列表，但自身不可变
my_tuple = (1, 2, 3)
my_tuple1 = tuple((1, 2, 3))
print(my_tuple)
print(my_tuple1)

# 集合：类似列表, 但里面的元素是无序而不重复的
set1 = {1, 2, 3}
set2 = set((4, 5, 6))
print(set1)
print(set2)

# 字典：键-值对。像JSON那种对象
empty_dict = {}
a = {"one": "字典1", "two": "字典2", "three": "字典3"}
print(a["one"])
print(a.keys())
print(a.values())
a.update({"four": "字典4"})
print(a.keys())

# 类型转换
# x = int(1)       # 得到 1
# y = int(2.8)     # 得到 2
# z = int("3")     # 得到 3

# 转换为字符串
x = str("s1")  # 得到 "s1"
y = str(2)  # 得到 "2"
z = str(3.0)  # 得到 "3.0"
print(x, y, z)

# ----- 字符串
hello = "Hello, World"
print(hello[1])  # 获取第二个字符 e
print(hello[-1])  # 获取倒数第一个字符 d

# 获取长度 len() 函数返回字符串的长度
print(len(hello))  # 12

# 重复多次
s = "===+"
n = 3
print(s * n)  # ===+===+===+

# 存在性判断 判断 "spam" 这个字符串是否在其它字符串里
s = "spam"
isSpam = s in "I saw spamalot!"
isNot = s not in "I saw not!"
print(isSpam)  # True
print(isNot)  # True

# 字符串拼接 可以使用加号进行拼接
s = "spam"
t = "egg"
print(s + t)  # spamegg

# 切割字符串
s = "mybacon"
print(s[2:5])  # bac
print(s[0:2])  # my
print(s[:2])  # my
print(s[2:])  # bacon
print(s[-5:-1])  # baco
print(s[::5])  # 步长 mo

# 插入分隔符拼接
str1 = "-".join(["John", "Peter", "Vicky"])
print(str1)  # John-Peter-Vicky

# 头尾判断
isStart = "hello".startswith("h")
isStart1 = "hello".startswith("e")
print(isStart)  # True
print(isStart1)  # False
isEnd = "hello".endswith("o")
print(isEnd)  # True

# 循环
for char in "foo":
    print(char)

# f-字符串（Python 3.6+）
website = "Reference"
print(f"HELLO, {website}")  # "Hello, Reference"

num = 10
print(f"{num} + 10 = {num + 10}")  # '10 + 10 = 20'

# 填充对齐
# 使用空格填充到指定长度
print(f'{"TEST":10}')
# 向左填充
print(f'{"TEST":*>10}')
# 向右填充
print(f'{"TEST":*<10}')
# 居中填充
print(f'{"TEST":*^10}')  # '***test***'
# 使用数字填充
print(f"{12345:0>10}")  # '0000012345'

# 负数
print(f"{-12345:0=10}")  # -000012345

import math

print(f"{math.pi:.2f}")  # '3.14'

# 分组选项
print(f"{100000:,.2f}")  # 100,000.00

# 百分比
print(f"{0.25:.0%}")  # 25%

# 科学计数法
print(f"{345600000000:e}")  # 3.456000e+11

# 列表
li1 = []
li2 = list((1, 2, 3))
li3 = list(range(1, 11))
print(li1)  # []
print(li2)  # [1, 2, 3]
print(li3)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 生成
list = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(list)  # [2, 4, 6, 8, 10]
list1 = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(list1)  # 1, 9, 25, 49, 81]

# 添加元素
li = []
li.append(1)
print(li)  # [1]
li.append(2)
li.append(3)
print(li)  # [1, 2, 3]

# 删除
li = [1, 2, 3, 4]
li.pop()
print(li)  # [1, 2, 3]
del li[0]
print(li)  # [2, 3]
li.remove(2)
print(li)  # [3]

# 列表边界
li = [1, 2, 3, 4]
print(li[0])
print(li[-1])
# print(li[4])  # # IndexError: list index out of range

# 连接
odd = [1, 2, 3, 4]
odd.extend([5, 6, 7])
print(odd)  # [1, 2, 3, 4, 5, 6, 7]

# 搜索
nums = [40, 36, 89, 2, 36, 100, 7, -20.5, -999]
num1 = nums.index(2)  # 返回元素 2 第一次出现的索引
print(num1)  # 3
num2 = nums.index(100, 3, 7)  # 搜索3-7之间的元素
print(num2)  # 5
num3 = nums.index(7, 4)  # 搜索4之后的元素
print(num3)  # 6

# 排序
li = [3, 1, 3, 2, 5]
li.sort()
print(li)  # [1, 2, 3, 3, 5]

# 反转
li.reverse()
print(li)  # [5, 3, 3, 2, 1]

# 计数
li = [3, 1, 3, 2, 5]
linum = li.count(3)
print(linum)  # 2

# 重复
li = ["re"] * 3
print(li)  # ['re', 're', 're']

# 切片
a = ["spam", "egg", "bacon", "tomato", "ham", "lobster"]
a1 = a[2:5]
print(a1)  # ['bacon', 'tomato', 'ham']
a2 = a[-5:-2]
print(a2)  # ['egg', 'bacon', 'tomato']

# 省略索引
a = ["spam", "egg", "bacon", "tomato", "ham", "lobster"]
a1 = a[:4]
print(a1)  # ['spam', 'egg', 'bacon', 'tomato']
a2 = a[2:]
print(a2)  # ['bacon', 'tomato', 'ham', 'lobster']

# 间隔索引
# 切片语法：list[start:end:step]
# start=0：从索引0开始。
# end=6：到索引6结束（不包含6，实际到索引5）。
# step=2：每隔1个元素取一次（步长2）。
a = ["spam", "egg", "bacon", "tomato", "ham", "lobster"]
a1 = a[0:6:2]
print(a1)  # ['spam', 'bacon', 'ham']
a2 = a[6:0:-2]
print(a2)  # ['lobster','tomato','egg']

# ---------判断
number = int(2)
if number > 0:
    print("数字大于0")
else:
    print("数字大于0")

# if-else-if
number = int(0)
if number < 0:
    print("您输入了一个负数。")
elif number == 0:
    print("您输入了一个 0 。")
else:
    print("您输入了一个正数。")

# 三目运算 条件是放在中间
scope = int(10)
line = 60
tip = "及格" if scope >= line else "不及格"
print(tip)  # 不及格

# ----- 循环
primes = [
    2,
    3,
    5,
]
for num in primes:
    print(num)

# 带索引
animals = ["dog", "cat", "mouse"]
for i, val in enumerate(animals):
    print(i, val)
# 0 dog
# 1 cat
# 2 mouse

# while 循环
x = 0
while x < 3:
    print(x)
    x += 1
# 0
# 1
# 2


# 跳出循环
x = 0
for index in range(10):
    x = index * 10
    if index == 5:
        break
    print(x)
# 0
# 10
# 20
# 30
# 40


# 跳过一轮循环
for index in range(6, 9):
    x = index * 10
    if index == 5:
        continue
    print(x)
# 60
# 70
# 80


# 范围循环
for i in range(3):
    print(i)

for i in range(4, 8):
    print("范围" + str(i))
# 4
# 5
# 6
# 7


# 使用zip()
name = ["Pete", "John", "Elizabeth"]
age = [6, 23, 44]
for n, a in zip(name, age):
    print(f"{n} is {a} years old")
# Pete is 6 years old
# John is 23 years old
# Elizabeth is 44 years old

# 列表生成式
# [表达式 for 变量 in 可迭代对象 if 条件]
result = [x ** 2 for x in range(10) if x % 2 == 0]
print(result)  # [0, 4, 16, 36, 64]


# -----------函数
def hello_world():
    print("hello world")


hello_world()


# 关键字参数
def keyword_args(**kwargs):
    return kwargs


arg = keyword_args(big="foot", loch="ness")
print(arg)  # {'big': 'foot', 'loch': 'ness'}


#  返回
def add(x, y):
    print(f"{x} + {y} = {x + y}")  # 1 + 2 = 3
    return x + y


num = add(1, 2)
print(num)  # 3


# 返回多个
def swap(x, y):
    return y, x


x = 1
y = 2
x, y = swap(x, y)
print(x)  # 2
print(y)  # 1


# 位置参数 功能是将传入的所有位置参数打包成元组返回
def varargs(*args):
    return args


args = varargs(1, 2, 3)
print(args)  # 元组(1,2,3)


# 默认值
def add(x, y=10):
    return x + y


num = add(5)
print(num)  # 15

# 匿名函数
func = (lambda x: x > 2)(3)
print(func)  # True

num = (lambda x, y: x ** 2 + y ** 2)(2, 1)
print(num)  # 5

# ----------- 解包: 是将一个 序列 内的多个元素依次重新分配到有限个容器的过程，这只发生在 变量赋值、参数传递 和 生成式生成 过程中。

# 等量解包
ip, port = "127.0.0.1", 80
print(ip)  # "127.0.0.1"
print(port)  # 80
ip, port = ("127.0.0.1", 8080)
print(ip)  # "127.0.0.1"
print(port)  # 80

# 适量解包： _ 也是一个单一变量，不允许解包多个元素，因此变量与值必须一一对应。
ip, _, port = "127.0.0.1:80".rpartition(":")
print(ip)  # "127.0.0.1"
print(port)  # 80

# 过量解包：这里的 * 就是收集序列在解包过程中多出来的元素， 只能有一个，与向函数传递位置参数时的 * 别无二致。
major, minor, *parts = "3.10.2.beta".split(".")
print(major)  # -> "3"
print(minor)  # -> "10"
print(parts)  # -> ["2", "beta"]

# 解包取左边
major, minor, *_ = "3.10.2.beta".split(".")
print(major)  # 3
print(minor)  # 10

# 解包取两边
major, *_, level = "3.10.2.beta".split(".")
print(major)  # 3
print(level)  # beta

# 解包去右边
*_, major, level = "3.10.2.beta".split(".")
print(major)  # 2
print(level)  # beta

# 解包集合
a, b, *_ = {3, 2, 1}
print(a)  # -> 1
print(b)  # -> 2
print(_)  # -> [3]

# 解包迭代器
a, b, *_ = range(3)
print(a)  # -> 0
print(b)  # -> 1
print(_)  # -> [2]

# 解包字典
a, b, *_ = dict(a=1, b=2, c=3)
print(a)  # a
print(_)  # ["c"]
a, b, *_ = dict(a=1, b=2, c=3).values()
print(a)  # 1
print(_)  # [3]

# 生成式中的解包：仅在列表／元组生成式中可以使用多个 *
chars = (*"abc", *"def", "g", "h")
print(chars)  # ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

digits = [*range(3), *"abc"]
print(digits)  # [0, 1, 2, 'a', 'b', 'c']

# 仅在字典生成式中可以使用多个 **
part = {"小明": 11, "小鹏": 12}
summary = {"小郑": 13, **part}
print(summary)  # {'小郑': 13, '小明': 11, '小鹏': 12}

# 迭代中解包
students = [
    ("小明", 18),
    ("小亮", 22),
]

for k, v in students:
    print(k, v)

students = [
    (0, ("小明", 18)),
    (1, ("小亮", 22)),
]

for i, (k, v) in students:
    print(i)  # -> 0、1
    print(k)  # -> "小明"、"小亮"
    print(v)  # -> 18、22


# 函数中的解包
def version(major, minor, *parts):
    print("major", major)  # major 3
    print("minor", minor)  # minor 10
    print("parts", parts)  # parts ('2', 'beta', '0')


version("3", "10", "2", "beta", "0")


def version():
    parts = "3.10.2.beta.0".split(".")
    return *parts, "x64"


print(version())  # ('3', '10', '2', 'beta', '0', 'x64')

# ---------- 模块
# 导入模块
import math

print(math.sqrt(16))  # 4.0

# 从一个模块导入
from math import ceil, floor

print(ceil(3.7))  # 4
print(floor(3.7))  # 3

# 导入一个模块的全部

# 给模块起别名
import math as m

# math.sqrt(16) == m.sqrt(16)
print(math.sqrt(16))  # True
print(m.sqrt(16))  # True

# 浏览模块的函数和属性
import math

dir(math)

# --------- 文件处理
# 逐行
with open("C:/TEST.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line)

# 带行号
file = open("C:/TEST.txt", "r", encoding="utf-8")
for i, line in enumerate(file, start=1):
    print("Number %s: %s" % (i, line))

# 写入字符串
contents = {"a": 12, "b": 13}
with open("C:/TEST.txt", "w+") as file:
    file.write(str(contents))

# 读取字符串
with open("C:/TEST.txt", "r+") as file:
    contents = file.read()
print(contents)

# 写入一对象
# contents = {"a": 12, "b": 13}
# with open("C:/TEST.txt", "w+") as file:
#     file.write(json.dumps(contents))
#
# # 读取对象
# with open("C:/TEST.txt", "r+") as file:
#     contents = json.load(file)
# print(contents)

# 删除文件
# import os
#
# os.remove("C:/TEST.txt")

# 检查和删除
import os

if os.path.exists("C:/TEST1.txt"):
    os.remove("C:/TEST1.txt")
else:
    print("The file does not exist")


# 删除文件夹
# import os
#
# os.rmdir("C:/test")


# ---------- 类和继承
# 定义
class MyClass:
    pass


my = MyClass()  # 类的实例化


# 构造函数
class Animal:
    def __init__(self, voice):
        self.voice = voice


cat = Animal("Meow")
print(cat.voice)  # => Meow

dog = Animal("Woof")
print(dog.voice)  # => Woof


# 方法
class Dog:
    def bark(self):
        print("ha-ha")


charlie = Dog()
charlie.bark()  # ha-ha


# 类变量
class MyClass:
    class_variable = "a class variable"


print(MyClass.class_variable)  # a class variable
x = MyClass()

print(x.class_variable)  # a class variable


# super函数
class ParentClass:
    def print_test(self):
        print("Parent Method")


class ChildClass(ParentClass):
    def print_test(self):
        print("Child Method")
        # 调用父级的 print_test()
        super().print_test()


child_child = ChildClass()
child_child.print_test()


# repr方法
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return self.name + " is " + str(self.age)


john = Employee("john", 18)
print(john)  # john is 18


# 多态性
class ParentClass:
    def print_test(self):
        print("A")


class ChildClass(ParentClass):
    def print_test(self):
        print("B")


OBJ_A = ParentClass()
OBJ_B = ChildClass()

OBJ_A.print_test()
OBJ_B.print_test()


# 重写
class ParentClass:
    def print_test(self):
        print("Parent")


class ChildClass(ParentClass):
    def print_test(self):
        print("Child")


child_int = ChildClass()
child_int.print_test()  # Child


# 继承
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    def sound(self):
        print("WOOF")


YOKI = Dog("yoki", 12)
print(YOKI.name)  # yoki
print(YOKI.age)  # 12
YOKI.sound()


# 用户定义的异常
class CustomError(Exception):
    pass


# --------- 数据类型
# 自定义类创建
from typing import Any


class Object:
    def __new__(cls, *args, **kwargs) -> "self":
        # new 和 init 声明的参数必须一致
        # 或者用 *args 和 **kwargs 进行兼容
        return object.__new__(cls)

    def __init__(self, *args, **kwargs):
        # 初始化方法没有返回值，也不能返回值。
        pass

    def __call__(self, *args, **kwargs) -> Any:
        pass


# 依次调用了 new 和 init，所以如果
# 手动调用 new，那么别忘了调用 init
obj = Object()

# 触发 __call__ 方法，要给什么参数取决于声明
obj()

# 上下文管理器
# from typing import Any
#
#
# class Object:
#     def __enter__(self) -> Optional[Any]:
#         # with 语句会将返回值绑定到 as 子句中的变量，如果有的话。
#         return
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         # 若 with 内没有发生异常，则三个参数都是 None 。
#         # 不应该重新引发传入的异常，这是调用者的责任。
#         pass
#
#
# with Object() as alias:
#     # 进入 with 之前调用 obj.__enter__() 并得到 alias（如果有返回的话）
#     pass
# # 离开 with 后调用 obj.__exit__() ，不管是正常结束还是因异常抛出而离开。
#
# # 当需要获取 Object 的对象时可以这样写
# obj = Object()
# with obj as alias:
#     pass

# 类型标注
string: str = "ha"
times: int = 3
print(string * 3)  # hahaha

# 错误的类型标注不会影响正常运行，也不会报错
result: str = 1 + 2
print(result)


# 参数
def say(name: str, start: str = "hi"):
    return start + "," + name


print(say("ngger"))  # hi,ngger


# 位置参数
def clac_summary(*args: int):
    return sum(args)


print(clac_summary(3, 1, 2))


# 关键字参数
def calc_sum(**kwargs: int):
    return sum(kwargs.values())


print(calc_sum(a=1, b=2))  # => 3


# 属性
class Employee:
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.graduated: bool = False


# 返回值
def say_hello(name) -> str:
    return f"Hello, {name}"


var = "python"
print(say_hello(var))  # Hello, python

# 多种可能的返回值
from typing import Union


def resp200(meaningful) -> Union[int, str]:
    return "ok" if meaningful else "200"


print(resp200(20))  # ok


# 返回多个值
def resp200() -> (int, str):
    return 200, "ok"


# 多种可能的返回值
def resp200(meaningful) -> Union[int, str]:
    return "ok" if meaningful else "200"


print(resp200(123))  # ok


# 标注自己
class Employee:
    name: str
    age: int

    def set_name(self, name) -> "employee":
        self.name = name
        return self


# 标注自己 3.11+
from typing import Self


class Emlpyee:
    name: str
    age: int

    def set_name(self: Self, name) -> Self:
        self.name = name
        return self


# 标注一个值为类型的参数
from typing import TypeVar, Type

T = TypeVar("T")


# "mapper" 的值是一个像 int、str、MyClass 这样的类型
# "default" 是一个 T 类型的值，比如 314、"string"、MyClass()
# 函数的返回值也是一个 T 类型的值
def converter(raw, mapper: Type[T], default: T) -> T:
    try:
        return mapper(raw)
    except:
        return default


raw: str = input("请输入一个证书")
result: int = converter(raw, mapper=int, default=0)

# 这是单行注释
""" 可以写多行字符串
    使用三个"，并且经常使用
    作为文档。
"""


# 生成器
def double_numbers(iterable):
    for i in iterable:
        yield i + i


# 要列出的生成器
values = (-x for x in [1, 2, 3, 4, 5])
gen_to_list = list(values)
print(gen_to_list)

# 处理异常
try:
    # 使用“raise”来引发错误
    raise IndexError("这是一个索引错误")
except IndexError as e:
    pass  # pass只是一个空操作。 通常你会在这里做恢复。
except (TypeError, NameError):
    pass  # 如果需要，可以一起处理多个异常。
else:  # try/except 块的可选子句。 必须遵循除块之外的所有内容
    print("All good!")  # 仅当 try 中的代码未引发异常时运行
finally:  # 在所有情况下执行
    print("我们可以在这里清理资源")
