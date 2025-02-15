"""
在Python中，对象（object）是指在内存中具有唯一标识符、类型和值的实例。
换言之，它是一个具有属性和方法的实体，这些属性和方法可以被访问和操作
"""

"""
===== 唯一标识符，即内存地址 =====
"""
# num = 10
# print(id(num))
# 所谓的对象，就是保存在内存中的一段数据。它包括函数、类、数据类型等

# def wrapper_parms(*parms, **kwparms):
#     def my_wrapper(func):
#         def wrapper(*args, **kwargs):
#             print("这是一个装饰器...")
#             res = func(*args, **kwargs)
#             print("现在输出装饰器的参数",parms, kwparms)
#             return res
#         return wrapper
#     return my_wrapper

# @wrapper_parms("test", test1="test1")
# def test_wrapper(msg):
#     print(msg)
#     return "func finish..."
# res = test_wrapper("这是一个测试函数")
# print(res)

"""
===== type object class =====
"""
# type 可以判断对象的类型，也可以用于创建类；
# Python中的数据类型是由类型类创建出来的（对象由类创建）
# Python中的类型是由type创建出来的（类由type创建）
# a = 10
# print(type(a)) # 类型类int
# print(type(int)) # int 由 type创建


# 在Python3中，自定义类如无继承，即默认继承object
# print(int.__bases__) # 查询继承关系

# object没有继承任何类
# object被type创建
# type继承了object
# type是由自身创建的

"""
===== 对象的三个特征 =====
1. 唯一标识符
2. 类型
3. 值
"""
# a = 1
# print(id(a)) # 标识符
# print(type(a)) # 类型
# print(a) # 值

""" 类型 [None], 全局只有一个"""
""" 类型 [数值], int / float / complex(复数) / bool """
""" 类型 迭代类型 """
""" 类型 序列类型 
 - list
 - bytes、bytearray、memoryview（二进制序列）
 - range
 - tuple
 - str
 - array
"""
""" 类型 映射 dict """
""" 类型 集合 set / frozenset（有序集合） """
""" 类型 上下文管理 with """