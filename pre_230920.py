# 匿名函数 定义：函数没有名字，用lambda关键字定义的
# 优点：对代码进行简化，增加运行的效率，特点：只适用于简单的操作，返回值不加上return
# 普通函数
# def func(a, b, c):
#     return a + b + c
# print(func(1, 2, 3))

# 匿名函数
# a, b, c：形式参数
# 1, 2, 3：实际参数
# result = (lambda a, b, c: a + b + c)(1, 2, 3)
# print(result)

# 面向对象：是一种程序设计的思想，将对象作为程序的基本单元
# 面向过程：就是一系列的函数，将这些功能组合在一起

# 注意：在python中，所有数据类型都可以视为对象

# 面向对象中的类和对象
# 类：一类事物，是一个概念，植物、水果、动物等等，一个类中有多个对象
# 对象：在一类事物中具体到某一个东西（细化）
# 对象可以有属性和方法（功能） Dog：属性：大小，品种，颜色，毛发等等，方法：吃，跑，叫
# 类和对象的关系：一个类中有多个对象，一对多的关系
# 面向对象的三大特征：封装、继承、多态

# 类的定义
# class Teacher(object):
#     # 定义类的属性
#     country = '中国'
#
#     # 定义类的方法
#     def show(self):
#         print('老师')

# 根据类创建对象
# teacher = Teacher()
# 获取对象的属性
# print(teacher.country)
# teacher.show()
# 查看Teacher类继承的父类
# print(Teacher.__base__)

# 对象中的属性和方法
# class Teacher(object):
#     def show(self):
#         print('老师')

# 通过对象进行动态的属性添加
# teacher = Teacher()
# teacher.name = 'zhangsan'
# teacher.age = 20

# 获取属性
# print(teacher.name, teacher.age)

# 修改属性，前提：该对象必须首先有这个属性
# teacher.name = 'lisi'
# print(teacher.name, teacher.age)

# self是什么
# class Cat(object):
#     def eat(self):
#         print('%s在吃'%self.name)
#         pass

# 创建对象
# cat1 = Cat()
# cat1.name = 'cat1'
# cat1.eat()
#
# cat2 = Cat()
# cat2.name = 'cat2'
# cat2.eat()

# __init__() 作用：初始化
# class Teacher(object):
#     # 魔法方法
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print('%s老师的年纪是%s'%(self.name, self.age))
#
# teacher1 = Teacher('zhangsan', 19)
# print(teacher1.age)
# teacher1.show()

# 继承 定义：描述多个类之间的关系
# 注意：
# 1、如果一个类A里面的属性和方法可以复用的话，则可以通过继承的方式传递到类B里面
# 2、类A就是基类，即父类，类B就是派生类，即子类
# 3、子类可以继承父类的属性和方法
# 在继承中，有单继承和多继承
# 单继承：子类只继承一个父类。优点：子类可以直接使用父类的属性和方法

# 父类
# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(self.name, self.age)

# 子类
# class Student(Person):
#     pass
#
# stu = Student('zhangsan', 24)
# print(stu.name, stu.age)
# stu.show()

# 多继承
# class A(object):
#     def show(self):
#         print('A类')
#
# class B(object):
#     def show(self):
#         print('B类')
#
# class C(A, B):
#     pass
#
# c = C()
# c.show()
# print(C.mro())

# 重写定义：子类可以继承父类，父类中的方法满足不了子类的需要，可以对父类的方法进行重写
# 重写特点：1、继承，2、方法名相同

# 父类
# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(self.name, self.age)

# 子类
# class Student(Person):
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def show(self):
#         print('我的名字：%s' %self.name)
#         print('我的年龄：%d' % self.age)
#         print('我的性别：%s' % self.gender)
#
# stu = Student('zhangsan', 20, '男')
# stu.show()

# 私有方法和私有属性
# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(self.name, self.age)
#
# class Student(Person):
#     def __init__(self, name, age, height):
#         # 公有属性
#         self.name = name
#         self.age = age
#         # 私有属性 以__开始的属性，只能在本类的内部进行使用，在类外面不能使用
#         self.__height = height
#
#     def show(self):
#         print('我的名字：%s' %self.name)
#         print('我的年龄：%d' % self.age)
#         print('我的身高：%d' % self.__height)
#
# stu = Student('zhangsan', 20, 180)
# stu.show()
# stu.__height = 190
# stu.show()
# print(stu.__height)

# 多态 多态在python中表现不是很明显
# 多态：不同的子类对象调用相同的父类方法，产生不同的执行结果。优点：增加代码外部的灵活性
# 多态的形成的前提：1、继承，2、重写父类的方法

# 定义Animal
# class Animal(object):
#     def run(self):
#         print('Animal run')
#
# class Dog(Animal):
#     def run(self):
#         print('Dog run')
#
# class Cat(Animal):
#     def run(self):
#         print('Cat run')
#
# def run_two(animal):
#     animal.run()
#     animal.run()
#
# dog = Dog()
# cat = Cat()
# run_two(dog)
# run_two(cat)

# 异常
# 程序运行出错，就会向上抛出，直到某个函数可以处理该异常，每种语言都有try cache 错误处理机制
# try:
#     print(num)
# except NameError as e:
#     print('有异常出现的时候会执行里面的代码')
#     print(e)
#
# print('有异常处理，不会影响到下面的代码的执行')

# 异常常使用的 Exception类
# try:
#     print(num)
# except Exception as e:
#     print('有异常出现的时候会执行里面的代码')
#     print(e)
#
# print('有异常处理，不会影响到下面的代码的执行')

# while True:
#     my_str = input('请输入数字：')
#
#     try:
#         my_str = int(my_str) + 1
#     except Exception as e:
#         print('有异常会执行')
#         print('重新输入数字')
#     else:
#         print('没有异常会执行else')
#     finally:
#         print('有没有异常都会执行finally')

# 模块
# 通俗的讲，就是一个.py文件，.py文件就是一个模块
# 作用：管理功能代码，在代码里面可以定义变量、函数、类
# import time
# import random
# time.sleep(2)
# print('123')
# help('modules')

# 自定义模块
# import 导入别人或者自己封装好的功能py文件
# import first_module
# print(first_module.g_num)
# first_module.show()
#
# stu = first_module.Student('zhangsan', 20)
# stu.show_msg()

# 模块导入的方式
# import first_module # 导入整个模块（并且导入的这个文件和该程序文件在同一个目录下）

# from 模块名 import 功能名
# 推荐使用
# from first_module import show
# from first_module import Student
# show()
# stu = Student('zhang', 20)
# stu.show_msg()

# from 模块名 import *
# 导入模块下所有的功能代码
# 不推荐使用

# 给模块别名
# from 模块名 import 功能名 as 重命名
# from first_module import show as show_msg
# show_msg()
# def show():
#     print('badou')
# show()

# 文件读写
# 1、打开文件
# 2、对文件内容进行操作（读、写）
# 3、关闭文件

# 文件的打开方式
# r：只读 文件不存在的话，程序会崩溃，出现程序不存在的异常
# w：只写 会将原来的内容进行覆盖，如果文件不存在，会创建一个文件
# a：追加写入
# b：表示二进制的形式 常用rb：以二进制的方式打开一个文件用于只读 wb：以二进制的方式打开一个文件用于只写

# w 模式
# 打开文件
# encoding 指定编码格式：win 写入是需要指定的，mac 默认为UTF-8
# f = open('./Badou.txt', 'w', encoding = 'utf-8')
# print(f.encoding)
# 操作文件
# 注意：文件被打开之后，多次写入数据不会覆盖
# f.write('Badou')
# f.write('cv')
# 关闭文件
# f.close()

# r 模式
# f = open('./Badou.txt', 'r', encoding='UTF-8')
# 读取数据
# content = f.read()
# print(content)
# f.close()

# a 模式
# f = open('./Badou.txt', 'a', encoding='UTF-8')
# f.write('ABC')
# f.close()

# rb 模式
# 注意：带有b的模式都是二进制的模式，在这种模式下，不管什么系统都不要添加encoding参数
# f = open('./Badou.txt', 'rb', encoding='UTF-8')
# f = open('./Badou.txt', 'rb')
# content = f.read()
# print(content, type(content))
# 对二进制的数据进行utf-8的解码操作，将bytes类型的数据转换为str类型
# result = content.decode('utf-8')
# print(result)
# 将str类型的转换为bytes类型，编码
# print(result.encode('utf-8'))
# 关闭
# f.close()

# 1.定义一个列表，并按照降序排列
# my_list = [1,3,6,4,7,2]
# # reverse=True：表示降序排列，默认不写表示升序
# my_list.sort(reverse=True)
# print(my_list)

# 2.判断是否为偶数（分别用普通函数和匿名函数实现）
# 普通函数
# def is_os(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# print(is_os(5), is_os(8))
# 匿名函数
# f = lambda num: True if num % 2 == 0 else False
# print(f(5), f(8))

# 3.如何用匿名函数对列表中的字典进行排序
# 源数据：[{'name': 'zhangsan', 'age': 18}, {'name': 'lisi', 'age': 20}]
# my_list = [{'name': 'zhangsan', 'age': 18}, {'name': 'lisi', 'age': 20}]
# my_list.sort(key=lambda item: item['age'], reverse=True)
# print(my_list)
# my_list = [{'name': 'zhangsan', 'age': 18}, {'name': 'lisi', 'age': 20}]
# def get_value(item):
#     return item['age']
# my_list.sort(key=get_value, reverse=True)
# print(my_list)

# 4.利用python进行文件拷贝
old_f = open('./Badou.txt', 'rb')
new_f = open('./target.txt', 'wb')

# 文件操作
while True:
    # 1024：读取1024 字节的数据
    file_data = old_f.read(1024)
    # 判断是否读取完了
    if len(file_data) == 0:
        break
    new_f.write(file_data)

# 关闭文件
old_f.close()
new_f.close()











