"""
概念
1. 鸭子类型和多态
2. 抽象基类
3. 使用isinstance而不是type
4. 类变量、对象变量
5. 类属性、实例属性及查到顺序
6. 静态方法、类方法、对象方法
7. 数据封装、私有属性
8. python对象的自省机制
9. super函数
10. django rest framework中对多继承使用的经验（混合继承）
11. python中的with语句
12. contextlib实现上下文管理
"""

"""
# 鸭子类型：在多个类中实现同一个方法，那么这些类可以看成同一个类型。以下是举例
"""
# class Cat:
#     def say(self):
#         print("我是猫")
        
# class Dog:
#     def say(self):
#         print("我是狗")
        
# class Duck:
#     def say(self):
#         print("我是鸭子")

"""        
# 多态：在多个类中同时继承了一个类并重写父类方法，在每个类中所调用的同一个方法会返回不同的行为。以下是举例
"""
# class Animal:
#     def run(self):
#         print("动物在跑")
        
# class Dog(Animal):
#     def run(self):
#         print("狗在跑")
        
# class Cat(Animal):
#     def run(self):
#         print("猫在跑")

""" 抽象基类（接口）
1. 本质也是一个类，类中实现了一些方法
2. 子类继承时必须重写父类方法

作用：
1. 可以检查对象中是否实现了某一指定功能
2. 强制子类去实现父类的所有方法
"""
# from collections.abc import Sized
# class Student:
#     def __init__(self,stu_list) -> None:
#         self.stu_list = stu_list
        
#     def __getitem__(self,item):
#         return self.stu_list[item]

#     def __len__(self,item):
#         return len(self.stu_list)

# print(hasattr(Student, "__getitem__")) # 检查类中是否存在此方法
# print(isinstance(Student([1,2,3]), Sized)) # 检查类中实现了计算长度的方法

# 自定义抽象基类示例
# from abc import ABC, abstractmethod
# class Cache(ABC):
#     @abstractmethod
#     def get_cache(self):
#         pass
    
#     def set_cache(self, value):
#         pass

"""
isinstance: 判断对象是否是指定类型，判断的对象也参考类的继承关系
type
    == 是判断值的！不能用于判断类型
    is 是判断内存地址
"""
# class A: pass
# class B: pass
# a = A()
# b = B()
# # 判断类型是否相等
# print(isinstance(a, A))
# print(isinstance(b, B))
# # == 判断值是否相等
# print(type(a))
# print(A)
# print(type(a) == A)
# print(type(a) == B)
# # is 判断内存地址是否相等
# print(type(b) is A)
# print(type(b) is B)
# print(type(b))
# print(B)

"""
类属性：被类对象所访问
实例属性：被实例对象所访问，类对象无法访问实例属性
"""
# class A:
#     a = 1 # 类属性
#     def __init__(self,b,c) -> None:
#         # 实例属性
#         self.b = b
#         self.c = c
# 类属性和实例属性的访问
# a = A(2,3)
# print(a.a, a.b, a.c) # 1,2,3
# print(A.a) # 1
# print(A.b, A.c) # 报错
# 类对象修改类属性
# A.a = 11
# print(A.a) # 11
# print(a.a) # 11
# 实例对象修改类属性
# a.a = 22 
# print(A.a) # 11 实例属性无法修改类属性
# print(a.a) # 22 实例属性新增一个属性'a'

"""
# 属性查找顺序
"""
# class A:
#     name = 'cls_a'
#     def __init__(self) -> None:
#         # self.name = 'obj_a'
#         pass
        
# a = A()
# print(a.name) # 实例属性 obj_a
# print(a.name) # 实例属性中没有，则查到类属性 cls_a

# 菱形继承
# class D:
#     name = 'cls_d'
# class B(D):
#     name = 'cls_b'
# class C(D):
#     name = 'cls_c'
# class A(B,C):
#     pass
# a = A()
# print(a.name) # cls_b，因为在继承顺序中，B在前，C在后
# print(A.__mro__) # 打印查找顺序

# 树状继承
# class E:
#     name = 'cls_e'
# class D:
#     name = "cls_d"
# class C(E):
#     name = "cls_c"
# class B(D):
#     name = "cls_b"
# class A(B,C):
#     pass
# a = A()
# print(a.name) # cls_b
# print(A.__mro__)

"""
类方法：可以被类对象和实例对象调用，类方法可以使用类属性，不能访问实例属性
静态方法：类对象可以访问，类名修改后静态方法内的类名也需同步修改，不能访问类中的属性和方法（静态方法内可以 class.类属性 访问）
实例方法：实例对象可以访问，方法的第一个参数是self，实例方法可以访问类中的所有属性和方法

根据需求定义方法：
    1. 不需要创建实例对象且不需要访问实例属性和类属性，采用静态方法
    2. 不需要创建实例对象但需要访问实例属性和类属性，采用类方法
    3. 需要创建实例对象且需要访问实例属性和类属性，采用实例方法
"""
# class Student:
#     address = "cq"
#     def __init__(self,name,age,gender) -> None:
#         self.name = name
#         self.age = age
#         self.gender = gender
        
#     def __str__(self) -> str:
#         return f"{self.name}, {self.age}, {self.gender}"
    
#     # 实例方法
#     def get_info(self):
#         print(self.address,self.name,self.age,self.gender)
    
#     # 实例方法 
#     def set_info(self, addr):
#         self.get_info()
    
#     @staticmethod # 静态方法
#     def parse_from_string_1(stu_info):
#         name, age, gender = tuple(stu_info.split(','))
#         return Student(name, age, gender)
    
#     @classmethod # 类方法
#     def parse_from_string_2(cls, stu_info): # cls 即加装饰器后自动指向调用的类
#         name, age, gender = tuple(stu_info.split(','))
#         return cls(name, age, gender)
    
# stu_1 = Student("xbj",26,"male")
# # print(stu_1.address)
# stu_1.get_info()
# stu_2 = Student.parse_from_string_1('lj,25,male')
# stu_2.get_info()
# stu_3 = Student.parse_from_string_2('lsl,27,male')
# stu_3.get_info()

"""
数据封装
私有属性：私有属性无法在类的外部使用，私有方法同理
    tips：私有属性在创建时会对当前属性的名称进行处理：_clsname__attrname
"""

# class Person:
#     def __init__(self,name,money) -> None:
#         self.name = name
#         self.__money = money # 私有属性
        
#     def get_curMoney(self):
#         print(self.__money)
    
#     # 私有方法
#     def __set_curMoney(self, money):
#         self.__money = money
        
# p = Person('xbj', 20)
# print(p.name, p.__money)
# p.get_curMoney()
# print(p._Person__money) # 访问私有属性的用法

"""
Python对象的自省机制：检测一个类的内部结构
"""
# class Person:
#     name = 'user'
    
# class Student(Person):
#     def __init__(self, school_name) -> None:
#         self.school_name = school_name
        
# stu = Student('sc_name')
# 查询这个对象中包含的属性，仅包含自身的属性，继承的无法查询
# print(stu.__dict__)
# stu.__dict__['addr'] = 'chongqing' # 通过dict来创建属性
# print(Person.__dict__) # 查询父类自身的属性
# 查询对象中的所有属性和方法，包含父类
# print(dir(stu))

"""
super 函数
    1. super函数的作用：调用“父类”的方法，不仅限于构造函数
    2. super的使用场景：代码重复的场景
    3. super函数的运行过程：根据类中的mro顺序进行查询并调用
"""
# class A:
#     def __init__(self) -> None:
#         print("A")
# class B(A):
#     def __init__(self) -> None:
#         print("B")
#         A.__init__(self) # 执行父类的构造函数
#         super().__init__() # 通过super来调用__mro__的方法，不仅限于构造函数
# b = B()

# import threading
# class MyThread(threading):
#     def __init__(self, thread_name, user):
#         self.user = user
#         super().__init__(name=thread_name) # 代码重用

# class D:
#     def __init__(self) -> None:
#         print("d")
# class B(D):
#     def __init__(self) -> None:
#         print("b") 
#         super().__init__()
# class C(D):
#     def __init__(self) -> None:
#         print("c")
#         super().__init__()
# class A(B,C):
#     def __init__(self) -> None:
#         print("a")
#         super().__init__()
# a = A() # a, b, c, d
# print(A.__mro__)

"""
混合继承
    1. mixin功能是单一的
    2. mixin类不继承其他的类（除object）
    
Mixin因为功能简单，且没有复杂的继承关系，便于管理
tips：在使用mixin中尽量避免在子类中使用super
"""
# class Animal:
#     def __init__(self,name) -> None:
#         self.name = name
# class RunMixin:
#     def run(self):
#         print(f'{self.name} is running')
# class SwimMixin:
#     def swim(self):
#         print(f'{self.name} is swimming')
# class FlyMixin:
#     def fly(self):
#          print(f'{self.name} is flying')   
# class Duck(Animal,RunMixin,SwimMixin,FlyMixin):
#     pass

# duck = Duck("duck")
# duck.run() # duck is running
# duck.swim() # duck is swimming
# duck.fly() # duck is flying

"""
with 语句:
    1. 适用于网络编程和文件读写编程
"""

# try:
#     print("程序运行中...")
#     # KeyError("ooooo")
# except KeyError:
#     print("key error...")
# else:
#     print("当前程序未产生异常")
# finally:
#     print("程序执行结束")
    
# 在函数中使用 try 语句
# def func_try():
#     try:
#         print("程序运行中...")
#         # KeyError("ooooo")
#         return 1
#     except KeyError:
#         print("key error...")
#         return 2
#     else:
#         print("当前程序未产生异常")
#         return 3
#     finally:
#         print("程序执行结束")
#         # return 4 # 如果finally中有return，则优先级最高
# print(func_try())

# 上下文管理协议 -- 魔术方法
# class Sample:
#     def __enter__(self):
#         print("enter trigged")
#         return self
        
#     def __exit__(self,exc_type,exc_val,exc_tb):
#         print('exit trigged')
        
#     def run(self):
#         print("program is running")
        
# with Sample() as sp:
#     sp.run()

"""
contextlib 实现上下文管理
"""
# import contextlib
# @contextlib.contextmanager # 此装饰器实现上下文管理
# def open_file(file_name):
#     print(f'open: {file_name}')
#     yield {'name':'xbj', 'age':26} # 被此装饰的必须是一个生成器函数
#     print(f"close:{file_name}")
    
# with open_file('xbj.txt') as f:
#     print("程序启动")
#     print(f)