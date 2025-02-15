"""
魔法函数 (魔术方法)：
    1. 添加后让类有特性的特性（例如可以迭代）
    2. python解释器提供的，不能改其方法名
"""

# class Student:
#     def __init__(self, student_list) -> None:
#         self.student_list = student_list
        
#     # 魔术方法，让类有序列特性
#     def __getitem__(self, item):
#         return self.student_list[item]
        
# std = Student(['a','b','c'])

# 迭代
# for stu in std.student_list:
#     print(stu)

# 迭代实例对象(添加了魔术方法后)
# for stu in std:
#     print(stu)

# 直接索引取值
# print(std[1])

"""
数据模型：
    提供类似于python内置的数据行为
    __init__(): 构造函数
    __repr__(): 表示对象
    __str__(): 表示对象
    __eq__(): 比较对象
    __lt__(): 迭代对象
    __len__(): 获取对象长度
    __getitem__(): 让对象可迭代、切片、索引取值
"""

# class Student:
#     def __init__(self, student_list) -> None:
#         self.student_list = student_list
        
#     # 魔术方法，让类有序列特性
#     def __getitem__(self, item):
#         return self.student_list[item]
    
#     def __len__(self) -> list:
#         return len(self.student_list)
    
#     def __str__(self):
#         return "这是我自己定义的一个类，并且可以迭代切片"
        
# std = Student(['a','b','c'])
# print(len(std), std)

"""
魔法函数概览
 1. 非数学运算
    - 字符串表示：__str__ / __repr__ (print调用str，直接调用对象调用repr)
    - 集合、序列：__len__ / __getitem__ / __setitem__ / __delitem__ / __contains__
    - 迭代相关：__iter__ / __next__
    - 可调用：__call__
    - with上下文管理：__enter__ / __exit__
    - 数值转换：__abs__ / __bool__ / __int__ / __float__ / __hash__ / __index__
    - 元类相关：__new__ / __init__
    - 属性相关：__getattr__ / __setattr__ / __getattribute__ / setatrribute__ / __dir__
    - 属性描述符：__get__ / __set__ / __delete__
    - 协程：__await__ / __aiter__ / __anext__ / __aenter__ / __aexit__
 2. 数学运算
"""

# class Test:
#     def __str__(self):
#         return "print会调用这一行"
    
#     def __repr__(self):
#         return "cmd调用会打印这一行"
    
#     def __len__(self):
#         pass