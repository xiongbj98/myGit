# Python 全套教学
视频来源B站：[2024最新版，从零基础小白到精通Python全栈](https://www.bilibili.com/video/BV1Qf421q7n9?p=4&vd_source=c0050214c17f6a387f4c5cf2bed4f1df)

# Python 进阶知识
视频来源B站：[2023年 Python 进阶天花板教程](https://www.bilibili.com/video/BV1Nh4y137N2?p=21&spm_id_from=pageDriver&vd_source=c0050214c17f6a387f4c5cf2bed4f1df)
（进度到第21节）
<hr>

## 1、一切皆对象
**===== 对象的三个特征 =====**
1. 唯一标识符
2. 类型
3. 值

**===== type object class =====**
1. 对象由类创建
2. 类由type创建
3. object没有继承任何类
4. object被type创建
5. type继承了object
6. type是由自身创建的

**===== Python 中的类型 =====**
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

## 2、魔法函数
**概念**
1. 添加后让类有特性的特性（例如可以迭代）
2. python解释器提供的，不能改其方法名

## 3、深入类和对象
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