# Python知识点与使用场景指南

## 1. 变量与数据类型

### 1.1 变量定义与使用

```python
age = 13
name = "john"
print(name)  # 输出: john
```

**使用场景：**

- 存储用户信息(姓名、年龄、邮箱等)
- 临时保存计算结果
- 配置程序运行参数

### 1.2 主要数据类型

#### 字符串(String)

```python
hello = "Hello World"
multi_string = """Multiline Strings
Lorem ipsum dolor sit amet,
consectetur adipiscing elit"""
print(multi_string)
```

**使用场景：**

- 处理文本数据
- 用户输入/输出交互
- 存储配置信息
- 日志记录

#### 数值(Number)

```python
x = 1  # 整数
y = 2.8  # 浮点数
z = 1j  # 复数
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>
```

**使用场景：**

- 整数：计数、索引、循环控制
- 浮点数：科学计算、金融计算、数据分析
- 复数：信号处理、电气工程计算

#### 布尔值(Boolean)

```python
my_bool = True
my_bool1 = False
print(bool(0))  # False
print(bool(1))  # True
```

**使用场景：**

- 条件判断
- 状态标记(完成/未完成)
- 权限控制(允许/禁止)

#### 列表(List)

```python
list1 = [1, 2, 3]
list2 = ["apple", "cherry", "orange"]
```

**使用场景：**

- 存储有序数据集合
- 数据处理中的临时存储
- 实现队列和栈结构

#### 元组(Tuple)

```python
my_tuple = (1, 2, 3)
my_tuple1 = tuple((1, 2, 3))
```

**使用场景：**

- 存储不可变数据集合
- 函数返回多个值
- 作为字典的键

#### 集合(Set)

```python
set1 = {1, 2, 3}
set2 = set((4, 5, 6))
```

**使用场景：**

- 去除重复元素
- 集合运算(交集、并集、差集)
- 成员检测

#### 字典(Dictionary)

```python
empty_dict = {}
a = {"one": "字典1", "two": "字典2", "three": "字典3"}
print(a["one"])  # 字典1
print(a.keys())  # dict_keys(['one', 'two', 'three'])
print(a.values())  # dict_values(['字典1', '字典2', '字典3'])
a.update({"four": "字典4"})
print(a.keys())  # dict_keys(['one', 'two', 'three', 'four'])
```

**使用场景：**

- 键值对映射存储
- 配置管理
- JSON数据处理
- 缓存实现

### 1.3 类型转换

```python
# 转为整数
x = int(1)  # 1
y = int(2.8)  # 2
z = int("3")  # 3

# 转为字符串
x = str("s1")  # "s1"
y = str(2)  # "2"
z = str(3.0)  # "3.0"
```

**使用场景：**

- 用户输入处理
- 数据类型不一致时的统一处理
- API接口数据适配

## 2. 字符串操作

### 2.1 字符串索引与切片

```python
msg = "Hello, World!"
print(msg[2:5])  # llo
print(msg[1])  # e
print(msg[-1])  # !
print(len(msg))  # 13
```

**使用场景：**

- 文本分析
- 数据提取
- 字符串解析

### 2.2 字符串方法

#### 字符串拼接

```python
# 使用+拼接
s = "spam"
t = "egg"
print(s + t)  # spamegg

# 使用join拼接
str1 = "-".join(["John", "Peter", "Vicky"])
print(str1)  # John-Peter-Vicky
```

**使用场景：**

- 生成文本报告
- 构建SQL语句
- 格式化输出

#### 判断方法

```python
isStart = "hello".startswith("h")  # True
isEnd = "hello".endswith("o")  # True
isSpam = "spam" in "I saw spamalot!"  # True
```

**使用场景：**

- 文件扩展名判断
- URL前缀检查
- 文本搜索

### 2.3 格式化字符串

```python
# f-字符串(Python 3.6+)
website = "Reference"
print(f"HELLO, {website}")  # "HELLO, Reference"

num = 10
print(f"{num} + 10 = {num + 10}")  # "10 + 10 = 20"

# 填充与对齐
print(f'{"text":*>10}')  # "******text"
print(f'{"text":*<10}')  # "text******"
print(f'{"text":*^10}')  # "***text***"

# 数值格式化
import math

print(f"{math.pi:.2f}")  # "3.14"
print(f"{100000:,.2f}")  # "100,000.00"
print(f"{0.25:.0%}")  # "25%"
print(f"{345600000000:e}")  # "3.456000e+11"
```

**使用场景：**

- 生成报表
- 日志格式化
- 用户界面显示
- 数据可视化时的标签格式化

## 3. 列表操作

### 3.1 列表创建

```python
li1 = []
li2 = list((1, 2, 3))
li3 = list(range(1, 11))

# 列表生成式
list1 = [x ** 2 for x in range(1, 11) if x % 2 == 1]  # [1, 9, 25, 49, 81]
list2 = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # [2, 4, 6, 8, 10]
```

**使用场景：**

- 数据收集
- 元素筛选
- 数据转换

### 3.2 列表元素操作

```python
# 添加元素
li = []
li.append(1)  # [1]
li.extend([2, 3])  # [1, 2, 3]

# 删除元素
li = [1, 2, 3, 4]
li.pop()  # [1, 2, 3]
del li[0]  # [2, 3]
li.remove(2)  # [3]
```

**使用场景：**

- 队列和栈的实现
- 动态数据存储
- 用户输入收集

### 3.3 列表查找与排序

```python
# 查找
nums = [40, 36, 89, 2, 36, 100, 7]
nums.index(2)  # 3
nums.index(100, 3, 7)  # 5
nums.index(7, 4)  # 6
nums.count(36)  # 2

# 排序
li = [3, 1, 3, 2, 5]
li.sort()  # [1, 2, 3, 3, 5]
li.reverse()  # [5, 3, 3, 2, 1]
```

**使用场景：**

- 数据排序
- 搜索算法
- 频率分析

### 3.4 列表切片

```python
a = ["spam", "egg", "bacon", "tomato", "ham", "lobster"]
a[2:5]  # ['bacon', 'tomato', 'ham']
a[:4]  # ['spam', 'egg', 'bacon', 'tomato']
a[2:]  # ['bacon', 'tomato', 'ham', 'lobster']
a[0:6:2]  # ['spam', 'bacon', 'ham']
a[6:0:-2]  # ['lobster', 'tomato', 'egg']
```

**使用场景：**

- 数据分批处理
- 提取特定位置数据
- 实现分页功能

## 4. 条件判断

### 4.1 if-elif-else结构

```python
number = 0
if number < 0:
    print("您输入了一个负数。")
elif number == 0:
    print("您输入了一个0。")
else:
    print("您输入了一个正数。")
```

**使用场景：**

- 用户输入验证
- 业务逻辑判断
- 错误处理

### 4.2 三元运算符

```python
scope = 10
line = 60
tip = "及格" if scope >= line else "不及格"
print(tip)  # 不及格
```

**使用场景：**

- 简单条件赋值
- UI显示逻辑
- 数据格式化

## 5. 循环结构

### 5.1 for循环

```python
# 基本for循环
for num in [2, 3, 5]:
    print(num)

# 带索引的循环
for i, val in enumerate(["dog", "cat", "mouse"]):
    print(i, val)  # 0 dog, 1 cat, 2 mouse

# 范围循环
for i in range(3):
    print(i)  # 0, 1, 2

# 使用zip()
name = ["Pete", "John", "Elizabeth"]
age = [6, 23, 44]
for n, a in zip(name, age):
    print(f"{n} is {a} years old")
```

**使用场景：**

- 批量数据处理
- 遍历集合元素
- 生成序列数据

### 5.2 while循环

```python
x = 0
while x < 3:
    print(x)
    x += 1  # 0, 1, 2
```

**使用场景：**

- 不确定迭代次数的场景
- 条件满足时持续执行
- 等待特定事件发生

### 5.3 循环控制

```python
# break - 跳出循环
for index in range(10):
    x = index * 10
    if index == 5:
        break
    print(x)  # 0, 10, 20, 30, 40

# continue - 跳过当前迭代
for index in range(6, 9):
    x = index * 10
    if index == 7:
        continue
    print(x)  # 60, 80
```

**使用场景：**

- 提前结束不必要的迭代
- 跳过特定条件的处理
- 实现搜索算法

## 6. 函数

### 6.1 函数定义与调用

```python
def hello_world():
    print("hello world")


hello_world()  # hello world
```

**使用场景：**

- 代码复用
- 模块化编程
- API设计

### 6.2 参数类型

#### 普通参数

```python
def add(x, y):
    print(f"{x} + {y} = {x + y}")
    return x + y


num = add(1, 2)  # 1 + 2 = 3
```

**使用场景：**

- 基本函数操作
- 传递必要信息

#### 默认参数

```python
def add(x, y=10):
    return x + y


num = add(5)  # 15
```

**使用场景：**

- 配置默认行为
- 简化常用函数调用
- API设计中提供默认选项

#### 位置参数

```python
def varargs(*args):
    return args


args = varargs(1, 2, 3)  # (1, 2, 3)
```

**使用场景：**

- 处理不定数量的参数
- 实现灵活的函数接口
- 转发参数到其他函数

#### 关键字参数

```python
def keyword_args(**kwargs):
    return kwargs


arg = keyword_args(big="foot", loch="ness")  # {'big': 'foot', 'loch': 'ness'}
```

**使用场景：**

- 处理不定数量的命名参数
- 配置函数
- 构建命令行接口

### 6.3 返回值

```python
# 单一返回值
def add(x, y):
    return x + y


# 多个返回值
def swap(x, y):
    return y, x


x, y = swap(1, 2)  # x=2, y=1
```

**使用场景：**

- 计算结果返回
- 状态信息返回
- 多值处理

### 6.4 匿名函数(Lambda)

```python
func = (lambda x: x > 2)(3)  # True
num = (lambda x, y: x ** 2 + y ** 2)(2, 1)  # 5
```

**使用场景：**

- 简单函数内联定义
- 函数式编程
- 回调函数

## 7. 解包操作

### 7.1 等量解包

```python
ip, port = "127.0.0.1", 80
print(ip)  # "127.0.0.1"
print(port)  # 80

ip, port = ("127.0.0.1", 8080)
print(ip)  # "127.0.0.1"
print(port)  # 8080
```

**使用场景：**

- 多变量赋值
- 元组数据提取
- 函数返回值处理

### 7.2 适量解包

```python
ip, _, port = "127.0.0.1:80".rpartition(":")
print(ip)  # "127.0.0.1"
print(port)  # "80"
```

**使用场景：**

- 忽略不需要的值
- 处理分隔符分割的数据
- 提取特定位置的数据

### 7.3 过量解包

```python
major, minor, *parts = "3.10.2.beta".split(".")
print(major)  # "3"
print(minor)  # "10"
print(parts)  # ["2", "beta"]

# 解包取左边
major, minor, *_ = "3.10.2.beta".split(".")

# 解包取两边
major, *_, level = "3.10.2.beta".split(".")

# 解包取右边
*_, major, level = "3.10.2.beta".split(".")
```

**使用场景：**

- 处理不定长度的序列
- 版本号解析
- 头尾数据提取

### 7.4 集合和迭代器解包

```python
# 解包集合
a, b, *_ = {3, 2, 1}
print(a)  # 1
print(b)  # 2
print(_)  # [3]

# 解包迭代器
a, b, *_ = range(3)
print(a)  # 0
print(b)  # 1
print(_)  # [2]
```

**使用场景：**

- 处理集合数据
- 迭代器数据处理
- 按位置提取数据

### 7.5 字典解包

```python
a, b, *_ = dict(a=1, b=2, c=3)
print(a)  # "a"
print(_)  # ["c"]

a, b, *_ = dict(a=1, b=2, c=3).values()
print(a)  # 1
print(_)  # [3]
```

**使用场景：**

- 字典键值提取
- 配置解析
- JSON数据处理

### 7.6 函数参数解包

```python
def version(major, minor, *parts):
    print("major", major)  # major 3
    print("minor", minor)  # minor 10
    print("parts", parts)  # parts ('2', 'beta', '0')


version("3", "10", "2", "beta", "0")

# 解包为参数
args = ["3", "10", "2"]
version(*args, "beta", "0")  # 相当于version("3", "10", "2", "beta", "0")
```

# Python进阶知识点与使用场景指南

## 1. 模块与包

### 1.1 导入模块

```python
# 导入整个模块
import math

print(math.sqrt(16))  # 4.0

# 从模块导入特定函数
from math import ceil, floor

print(ceil(3.7))  # 4
print(floor(3.7))  # 3

# 给模块起别名
import math as m

print(m.sqrt(16))  # 4.0
```

**使用场景：**

- 复用标准库功能
- 使用第三方库
- 组织大型项目代码
- 简化重复使用的代码路径

### 1.2 查看模块内容

```python
import math

dir(math)  # 列出模块中的所有函数和属性
```

**使用场景：**

- 探索新模块功能
- 调试和开发
- 学习库的API

## 2. 文件处理

### 2.1 文件读取

```python
# 逐行读取
with open("file.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line)

# 带行号读取
file = open("file.txt", "r", encoding="utf-8")
for i, line in enumerate(file, start=1):
    print(f"Line {i}: {line}")
file.close()  # 记得关闭文件

# 读取整个文件内容
with open("file.txt", "r+") as file:
    contents = file.read()
print(contents)
```

**使用场景：**

- 数据提取和处理
- 配置文件读取
- 日志分析
- 文本处理

### 2.2 文件写入

```python
# 写入字符串
contents = {"a": 12, "b": 13}
with open("file.txt", "w+") as file:
    file.write(str(contents))

# 写入JSON对象
import json

contents = {"a": 12, "b": 13}
with open("file.txt", "w+") as file:
    file.write(json.dumps(contents))

# 读取JSON对象
with open("file.txt", "r+") as file:
    contents = json.load(file)
print(contents)
```

**使用场景：**

- 数据持久化
- 配置存储
- 生成报告
- 日志记录

### 2.3 文件和目录操作

```python
import os

# 删除文件
if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("文件不存在")

# 删除目录
os.rmdir("empty_directory")  # 只能删除空目录

# 删除目录及其内容
import shutil

shutil.rmtree("directory_with_contents")

# 创建目录
os.makedirs("new_directory/subdirectory", exist_ok=True)

# 列出目录内容
files = os.listdir("directory")
```

**使用场景：**

- 文件管理
- 临时文件处理
- 批量文件操作
- 数据备份和清理

## 3. 类和面向对象编程

### 3.1 类的定义与实例化

```python
# 简单类定义
class MyClass:
    pass


my = MyClass()  # 实例化类


# 带构造函数的类
class Animal:
    def __init__(self, voice):
        self.voice = voice


cat = Animal("Meow")
print(cat.voice)  # Meow
```

**使用场景：**

- 对象模型设计
- 状态和行为封装
- 模拟现实世界的实体

### 3.2 类的方法与变量

```python
# 实例方法
class Dog:
    def bark(self):
        print("Woof!")


charlie = Dog()
charlie.bark()  # Woof!


# 类变量
class MyClass:
    class_variable = "a class variable"  # 所有实例共享的变量


print(MyClass.class_variable)  # a class variable
x = MyClass()
print(x.class_variable)  # a class variable
```

**使用场景：**

- 定义对象行为
- 维护类级别状态
- 实现设计模式

### 3.3 继承与多态

```python
# 基本继承
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    def sound(self):
        print("WOOF")


yoki = Dog("yoki", 12)
print(yoki.name)  # yoki
print(yoki.age)  # 12
yoki.sound()  # WOOF


# 方法重写
class ParentClass:
    def print_test(self):
        print("Parent")


class ChildClass(ParentClass):
    def print_test(self):
        print("Child")


child = ChildClass()
child.print_test()  # Child


# 使用super()调用父类方法
class ParentClass:
    def print_test(self):
        print("Parent Method")


class ChildClass(ParentClass):
    def print_test(self):
        print("Child Method")
        # 调用父类的print_test()
        super().print_test()


child = ChildClass()
child.print_test()  # 输出: Child Method 然后 Parent Method
```

**使用场景：**

- 代码复用
- 模型层次结构
- 框架设计
- 插件系统

### 3.4 特殊方法

```python
# __repr__方法用于对象的字符串表示
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} is {self.age}"


john = Employee("John", 18)
print(john)  # John is 18


# __new__方法控制对象创建
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


# __call__方法使对象可调用
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor


double = Multiplier(2)
print(double(5))  # 10
```

**使用场景：**

- 自定义对象行为
- 实现设计模式
- 控制对象生命周期

### 3.5 上下文管理器

```python
class DatabaseConnection:
    def __enter__(self):
        print("连接数据库")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("关闭数据库连接")
        # 返回True可以抑制异常传播
        return False

    def query(self, sql):
        print(f"执行查询: {sql}")


# 使用with语句
with DatabaseConnection() as conn:
    conn.query("SELECT * FROM users")
# 自动调用__exit__，即使出现异常
```

**使用场景：**

- 资源管理(文件、网络连接、数据库)
- 事务处理
- 临时状态变更

### 3.6 用户定义异常

```python
class InvalidAgeError(Exception):
    """当年龄值无效时抛出"""
    pass


def set_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError(f"年龄必须在0-150之间，收到的值是: {age}")
    return age


try:
    set_age(-5)
except InvalidAgeError as e:
    print(f"错误: {e}")
```

**使用场景：**

- 业务规则验证
- 自定义错误处理
- API设计

## 4. 类型标注

### 4.1 基本类型标注

```python
# 变量类型标注
name: str = "Python"
age: int = 30
is_active: bool = True


# 函数参数和返回值标注
def greet(name: str, times: int = 1) -> str:
    return f"Hello, {name}!" * times


message = greet("Python")
```

**使用场景：**

- 提高代码可读性
- 辅助IDE代码补全
- 静态类型检查

### 4.2 复杂类型标注

```python
from typing import List, Dict, Tuple, Union, Optional

# 列表类型
names: List[str] = ["Alice", "Bob", "Charlie"]

# 字典类型
user_ages: Dict[str, int] = {"Alice": 25, "Bob": 30}

# 元组类型
point: Tuple[float, float] = (2.5, 3.7)

# 联合类型(多种可能类型)
result: Union[int, str] = "success" if True else 404

# 可选类型(值或None)
user_id: Optional[int] = None
```

**使用场景：**

- API设计
- 大型项目中的类型安全
- 团队协作
- 文档自生成

### 4.3 高级类型标注

```python
from typing import TypeVar, Generic, Callable, Type, Self

# 泛型类型变量
T = TypeVar('T')


# 泛型函数
def first_element(collection: List[T]) -> T:
    return collection[0]


# 泛型类
class Box(Generic[T]):
    def __init__(self, content: T):
        self.content = content


# 标注回调函数
def apply_operation(x: int, operation: Callable[[int], int]) -> int:
    return operation(x)


# 标注类型为参数
def create_instance(cls: Type[T]) -> T:
    return cls()


# 标注自身类型(Python 3.11+)
class ChainableObject:
    def set_value(self, value: int) -> Self:
        self.value = value
        return self
```

**使用场景：**

- 复杂库设计
- 框架开发
- 可复用组件设计

## 5. 异常处理

### 5.1 基本异常处理

```python
try:
    # 可能引发异常的代码
    result = 10 / 0
except ZeroDivisionError:
    # 处理特定类型的异常
    print("除数不能为零")
except (TypeError, ValueError) as e:
    # 处理多种异常类型
    print(f"输入错误: {e}")
else:
    # 没有发生异常时执行
    print("计算成功")
finally:
    # 无论是否发生异常都会执行
    print("清理资源")
```

**使用场景：**

- 错误处理和恢复
- 资源管理
- 用户输入验证
- 网络和I/O操作

### 5.2 异常抛出

```python
def validate_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数")
    if age > 150:
        raise ValueError("年龄不能超过150岁")
    return age


try:
    user_age = validate_age(-5)
except ValueError as e:
    print(f"错误: {e}")
```

**使用场景：**

- 输入验证
- 业务规则强制执行
- API错误传播
- 流程控制

### 5.3 自定义异常

```python
class NetworkError(Exception):
    """网络相关错误的基类"""
    pass


class ConnectionError(NetworkError):
    """连接失败时抛出"""
    pass


class TimeoutError(NetworkError):
    """连接超时时抛出"""

    def __init__(self, timeout, operation):
        self.timeout = timeout
        self.operation = operation
        super().__init__(f"{operation} operation timed out after {timeout} seconds")


try:
    raise TimeoutError(30, "download")
except TimeoutError as e:
    print(f"超时错误: {e}")
except NetworkError:
    print("网络错误")
```

**使用场景：**

- 领域特定错误处理
- 错误分类
- API设计

## 6. 生成器和迭代器

### 6.1 生成器函数

```python
def countdown(n):
    """从n倒数到1的生成器"""
    while n > 0:
        yield n
        n -= 1


# 使用生成器
for i in countdown(5):
    print(i)  # 5, 4, 3, 2, 1

# 手动迭代生成器
counter = countdown(3)
print(next(counter))  # 3
print(next(counter))  # 2
print(next(counter))  # 1
```

**使用场景：**

- 处理大量数据
- 惰性计算
- 内存效率优化
- 流数据处理

### 6.2 生成器表达式

```python
# 生成器表达式
squares = (x * x for x in range(1, 6))
print(list(squares))  # [1, 4, 9, 16, 25]

# 转换为列表
values = (-x for x in [1, 2, 3, 4, 5])
gen_to_list = list(values)
print(gen_to_list)  # [-1, -2, -3, -4, -5]
```

**使用场景：**

- 数据转换
- 过滤操作
- 链式数据处理
- 替代简单的函数

### 6.3 迭代器协议

```python
class Fibonacci:
    """生成斐波那契数列的迭代器"""

    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration

        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return result


# 使用自定义迭代器
for num in Fibonacci(10):
    print(num)  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

**使用场景：**

- 自定义序列
- 状态机实现
- 惰性数据源
- 自定义集合类

## 7. 装饰器

### 7.1 基本装饰器

```python
def timing_decorator(func):
    """记录函数执行时间的装饰器"""

    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 执行用时: {end_time - start_time:.4f} 秒")
        return result

    return wrapper


@timing_decorator
def slow_function():
    import time
    time.sleep(1)
    return "完成"


result = slow_function()  # slow_function 执行用时: 1.0012 秒
```

**使用场景：**

- 性能监控
- 日志记录
- 访问控制
- 缓存实现

### 7.2 带参数的装饰器

```python
def repeat(times):
    """重复执行函数多次的装饰器"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results

        return wrapper

    return decorator


@repeat(3)
def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))  # ['Hello, Alice!', 'Hello, Alice!', 'Hello, Alice!']
```

**使用场景：**

- 配置功能行为
- 条件执行
- 参数验证
- 自定义错误处理

### 7.3 类装饰器

```python
def singleton(cls):
    """单例模式装饰器"""
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Configuration:
    def __init__(self):
        self.settings = {}

    def set(self, key, value):
        self.settings[key] = value

    def get(self, key, default=None):
        return self.settings.get(key, default)


# 创建两个实例，但实际上是同一个对象
config1 = Configuration()
config2 = Configuration()
print(config1 is config2)  # True
```

**使用场景：**

- 实现设计模式
- 类行为修改
- 元编程
- AOP(面向切面编程)

## 8. 函数式编程

### 8.1 lambda表达式

```python
# 简单的lambda函数
square = lambda x: x ** 2
print(square(5))  # 25


# 在函数中使用lambda
def get_sorter(reverse=False):
    return lambda x: -x if reverse else x


numbers = [3, 1, 4, 1, 5, 9]
numbers.sort(key=get_sorter(reverse=True))
print(numbers)  # [9, 5, 4, 3, 1, 1]
```

**使用场景：**

- 短小的一次性函数
- 作为高阶函数参数
- 回调函数

### 8.2 map, filter, reduce

```python
# map函数
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# filter函数
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]

# reduce函数
from functools import reduce

sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)  # 15 (1+2+3+4+5)
```

**使用场景：**

- 数据转换
- 集合操作
- 函数式数据处理管道
- 替代循环的清晰表达

### 8.3 高阶函数

```python
def create_multiplier(factor):
    """返回一个乘以指定系数的函数"""

    def multiply(x):
        return x * factor

    return multiply


double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15


# 函数组合
def compose(f, g):
    """创建两个函数的组合"""
    return lambda x: f(g(x))


def add_one(x):
    return x + 1


square_then_add_one = compose(add_one, lambda x: x ** 2)
print(square_then_add_one(3))  # 10 (3^2 + 1)
```

**使用场景：**

- 策略模式实现
- 函数定制
- 拓展现有函数
- 组合复杂行为

### 8.4 闭包

```python
def counter():
    """创建一个计数器函数"""
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


my_counter = counter()
print(my_counter())  # 1
print(my_counter())  # 2
print(my_counter())  # 3


# 带参数的闭包
def make_power_function(exponent):
    def power(base):
        return base ** exponent

    return power


square = make_power_function(2)
cube = make_power_function(3)
print(square(4))  # 16
print(cube(3))  # 27
```

**使用场景：**

- 状态封装
- 工厂函数
- 创建特定环境的函数
- 避免全局变量

## 9. 高级特性

### 9.1 列表推导式和生成器表达式

```python
# 列表推导式
squares = [x ** 2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 带条件的列表推导式
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# 嵌套列表推导式
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 生成器表达式(使用圆括号而非方括号)
gen = (x ** 2 for x in range(10))
```

**使用场景：**

- 数据转换和过滤
- 扁平化嵌套结构
- 高效内存使用
- 简化循环操作

### 9.2 字典和集合推导式

```python
# 字典推导式
squares_dict = {x: x ** 2 for x in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 从序列创建字典
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # {'Alice': 5, 'Bob': 3, 'Charlie': 7}

# 集合推导式
vowels = {char for char in "hello world" if char in "aeiou"}
print(vowels)  # {'e', 'o'}
```

**使用场景：**

- 键值映射转换
- 数据过滤和提取
- 从序列创建映射
- 去重和集合操作

### 9.3 装饰器类

```python
class Trace:
    """跟踪函数调用的装饰器类"""

    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"Call {self.calls} to {self.func.__name__}")
        return self.func(*args, **kwargs)


@Trace
def say_hello(name):
    return f"Hello, {name}!"


print(say_hello("World"))  # Call 1 to say_hello
# Hello, World!
print(say_hello("Python"))  # Call 2 to say_hello
# Hello, Python!
```

**使用场景：**

- 状态跟踪装饰器
- 参数验证
- 函数调用监控
- 实现带状态的装饰器

### 9.4 上下文管理器

```python
from contextlib import contextmanager


@contextmanager
def file_manager(filename, mode="r"):
    """文件管理上下文管理器"""
    try:
        file = open(filename, mode)
        yield file
    finally:
        file.close()


# 使用自定义上下文管理器
with file_manager("example.txt", "w") as f:
    f.write("Hello, World!")
```

**使用场景：**

- 资源管理
- 状态临时修改
- 事务处理
- 锁管理

### 9.5 元类

```python
class MetaSingleton(type):
    """单例模式元类"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    def __init__(self, url):
        self.url = url
        print(f"数据库连接创建: {url}")


# 无论创建多少次实例，都只会有一个
db1 = Database("mysql://localhost:3306/db1")
db2 = Database("mysql://localhost:3306/db2")  # 不会创建新连接
print(db1 is db2)  # True
print(db1.url)  # mysql://localhost:3306/db1
```

**使用场景：**

- 控制类的创建过程
- 实现设计模式
- 自动注册类
- ORM系统实现

## 10. 并发编程

### 10.1 线程

```python
import threading
import time


def worker(name, delay):
    """线程工作函数"""
    print(f"{name} 开始工作")
    time.sleep(delay)
    print(f"{name} 完成工作")


# 创建线程
thread1 = threading.Thread(target=worker, args=("线程1", 2))
thread2 = threading.Thread(target=worker, args=("线程2", 1))

# 启动线程
thread1.start()
thread2.start()

# 等待线程完成
thread1.join()
thread2.join()
print("所有线程完成")
```

**使用场景：**

- I/O密集型任务
- 后台任务
- 用户界面响应
- 并行数据处理

### 10.2 线程同步

```python
import threading

counter = 0
counter_lock = threading.Lock()


def increment_counter(amount):
    global counter
    for _ in range(amount):
        with counter_lock:  # 使用锁保护共享资源
            counter += 1


# 创建线程
threads = []
for _ in range(5):
    thread = threading.Thread(target=increment_counter, args=(1000,))
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

print(f"最终计数: {counter}")  # 应该是5000
```

**使用场景：**

- 共享资源保护
- 线程协调
- 避免竞态条件
- 并发数据结构

### 10.3 进程

```python
import multiprocessing
import os


def worker(name):
    """进程工作函数"""
    print(f"{name} 进程ID: {os.getpid()}")


if __name__ == "__main__":
    # 创建进程
    process1 = multiprocessing.Process(target=worker, args=("进程1",))
    process2 = multiprocessing.Process(target=worker, args=("进程2",))

    # 启动进程
    process1.start()
    process2.start()

    # 等待进程完成
    process1.join()
    process2.join()

    print("所有进程完成")
```

**使用场景：**

- CPU密集型任务
- 并行计算
- 隔离执行环境
- 充分利用多核处理器

### 10.4 异步IO

```python
import asyncio


async def fetch_data(delay):
    """模拟异步数据获取"""
    print(f"开始获取数据 (延迟 {delay}s)")
    await asyncio.sleep(delay)  # 非阻塞等待
    print(f"数据获取完成 (延迟 {delay}s)")
    return f"数据 {delay}"


async def main():
    # 并发运行任务
    tasks = [
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    ]
    results = await asyncio.gather(*tasks)
    print(f"所有结果: {results}")


# 运行异步程序
asyncio.run(main())
```

**使用场景：**

- 高并发I/O操作
- Web服务器
- 网络客户端
- 实时应用

## 11. 实际应用示例

```python
import requests
import json
import time


def get_weather(city):
    """获取城市天气信息"""
    api_key = "your_api_key"
    url = f"https://api.example.com/weather?city={city}&key={api_key}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # 检查HTTP错误

        data = response.json()
        return {
            "city": data["city"],
            "temperature": data["temp"],
            "conditions": data["conditions"]
        }
    except requests.exceptions.RequestException as e:
        print(f"API请求错误: {e}")
        return None


def get_news(category, count=5):
    """获取特定类别的新闻"""
    api_key = "your_api_key"
    url = f"https://api.example.com/news?category={category}&count={count}&key={api_key}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        return response.json()["articles"]
    except requests.exceptions.RequestException as e:
        print(f"新闻API请求错误: {e}")
        return []


class RestApiClient:
    """RESTful API客户端基类"""

    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        self.api_key = api_key
        self.session = requests.Session()

        if api_key:
            self.session.headers.update({"Authorization": f"Bearer {api_key}"})

    def get(self, endpoint, params=None):
        """发送GET请求"""
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"GET请求错误: {e}")
            return None

    def post(self, endpoint, data=None, json_data=None):
        """发送POST请求"""
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.post(url, data=data, json=json_data, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"POST请求错误: {e}")
            return None

    def put(self, endpoint, data=None, json_data=None):
        """发送PUT请求"""
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.put(url, data=data, json=json_data, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"PUT请求错误: {e}")
            return None

    def delete(self, endpoint, params=None):
        """发送DELETE请求"""
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.delete(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"DELETE请求错误: {e}")
            return None


class TodoApiClient(RestApiClient):
    """待办事项API客户端示例"""

    def __init__(self, api_key):
        super().__init__("https://api.example.com/todos", api_key)

    def get_todos(self):
        """获取所有待办事项"""
        return self.get("")

    def get_todo(self, todo_id):
        """获取特定待办事项"""
        return self.get(f"{todo_id}")

    def create_todo(self, title, description, due_date=None):
        """创建新的待办事项"""
        todo_data = {
            "title": title,
            "description": description,
            "completed": False
        }

        if due_date:
            todo_data["due_date"] = due_date

        return self.post("", json_data=todo_data)

    def update_todo(self, todo_id, **kwargs):
        """更新待办事项"""
        return self.put(f"{todo_id}", json_data=kwargs)

    def delete_todo(self, todo_id):
        """删除待办事项"""
        return self.delete(f"{todo_id}")

    def mark_completed(self, todo_id):
        """将待办事项标记为已完成"""
        return self.update_todo(todo_id, completed=True)


def retry_request(max_retries=3, delay=1):
    """请求重试装饰器"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except requests.exceptions.RequestException as e:
                    retries += 1
                    if retries == max_retries:
                        print(f"达到最大重试次数 ({max_retries}). 最后错误: {e}")
                        return None
                    print(f"请求失败，{delay}秒后重试 ({retries}/{max_retries})")
                    time.sleep(delay)

        return wrapper

    return decorator


@retry_request(max_retries=3, delay=2)
def fetch_user_data(user_id):
    """获取用户数据(带重试机制)"""
    url = f"https://api.example.com/users/{user_id}"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()


# 使用示例
if __name__ == "__main__":
    # 基本天气API调用
    weather = get_weather("Beijing")
    if weather:
        print(f"{weather['city']}的天气: {weather['temperature']}°C, {weather['conditions']}")

    # 获取科技新闻
    tech_news = get_news("technology", count=3)
    if tech_news:
        print("\n今日科技新闻:")
        for i, article in enumerate(tech_news, 1):
            print(f"{i}. {article['title']} - {article['source']}")

    # 使用Todo API客户端
    todo_client = TodoApiClient("your_todo_api_key")

    # 创建新的待办事项
    new_todo = todo_client.create_todo(
        "完成Python报告",
        "编写Web API客户端示例并提交给团队审核",
        "2023-12-15"
    )

    if new_todo:
        print(f"\n创建了新的待办事项: {new_todo['title']} (ID: {new_todo['id']})")

        # 获取所有待办事项
        todos = todo_client.get_todos()
        if todos:
            print(f"\n您有 {len(todos)} 个待办事项:")
            for todo in todos:
                status = "已完成" if todo["completed"] else "未完成"
                print(f"- {todo['title']} ({status})")

        # 将待办事项标记为已完成
        todo_client.mark_completed(new_todo["id"])
        print(f"\n已将待办事项 '{new_todo['title']}' 标记为已完成")

    # 使用重试机制获取用户数据
    user = fetch_user_data(123)
    if user:
        print(f"\n用户信息: {user['name']} ({user['email']})")
```

**使用场景：**

Python是一种功能强大且灵活的编程语言，适用于各种应用场景：

1. **数据分析与科学计算**：凭借NumPy、Pandas、Matplotlib等库，Python成为数据分析的首选语言。
2. **Web开发**：Django、Flask等框架使Python能够开发各种复杂度的网站和应用。
3. **自动化**：Python简洁的语法非常适合编写自动化脚本和工具。
4. **机器学习和人工智能**：TensorFlow、PyTorch等框架使Python成为AI开发的主流语言。
5. **桌面应用**：通过Tkinter、PyQt等库，可以创建跨平台的桌面应用。

