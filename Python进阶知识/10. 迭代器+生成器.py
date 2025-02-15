"""
前言: 可迭代对象
    1. 可迭代对象Iterable, 即可被遍历的对象
    2. 可迭代对象的条件:
        - 可迭代对象实现了 __iter__()
        - __iter__() 返回了迭代器对象
    3. for 循环的工作原理:
        - 先通过 __iter__() 获取可迭代对象的迭代器
        - 对获取到的迭代器不断调用 __next__() 方法来获取下一个值并将其赋值给临时变量
    4. 判断是否为可迭代对象
        from collections.abc import Iterable
        isinstance(object, Iterable)
        
一、迭代器 Iterator
    1. 可以记住遍历位置的对象, 在上次停留的位置继续做一些事情
    2. e.g
        li = [1,2,3,4,5]
        li1 = iter(li)  # li1 为迭代器， iter(li) 等同于 li.__iter__()
        next(li1) # 1  # 等同于 li1.__next__()
        next(li1) # 2
        ...
        若取完后再调用 next() 会报错
    3. 可迭代对象iterable和迭代器iterator
        - 凡是可作用于 for 循环的都属于可迭代对象
        - 凡是可作用于 next() 的都是迭代器
        - 可迭代对象并不一定是迭代器对象
        - 迭代器对象一定是可迭代对象
        - 因此可迭代对象可以通过iter()转换为迭代器对象
        - 总结:
            拥有 __iter__() 的是可迭代对象
            拥有 __iter__() + __next__() 是迭代器对象
    4. 迭代器协议
        对象必须提供 next 方法
    5. 自定义迭代器类
        class MyIterator(object):
            def __init__(self):
                self.num = 0
            def __iter__(self):
                return self
            def __next__(self):
                # 结束条件
                if self.num == 10: raise StopIteration("终止迭代")
                self.num += 1
                return self.num
        for i in MyIterator():
            print(i)  # 1 ~ 10
    
二、生成器 generator
    1. 一边循环一边计算的机制就是生成器
    2. 生成器表达式
        - 列表推导式 li = [i*2 for i in range(10)]  # list
        - 生成器表达式 gen = (i*3 for i in range(10))  # generator
    3. 取值 next()
    4. 生成器函数
        - python 中使用了 yield 关键字的函数就是生成器函数
        - yield 类似于 return, 将指定值或多个值返回给调用者
        - yield 一次返回一个结果, 在每个结果中间挂起函数, 执行next(), 再重新从挂起点继续往下执行
        - e.g
            def gen():
                print("start")
                yield 'a'
                yield 'b'
                yield 'c'
            print(gen())  # generator
            g = gen()
            print(next(g))  # a
            print(next(g))  # b
            print(next(g))  # c
            
            def gen1(n):
                li = []
                a = 0
                while a < n:
                    li.append(a)
                    yield a
                    a += 1
                    
后言、三者关系
    1. 可迭代对象: 指实现了python迭代协议, 可通过 for...in... 循环遍历
    2. 迭代器: 可以记住知己遍历位置的对象, 直观体现就是通过next()函数返回值,只能往前不能往后
    3. 生成器: 特殊的迭代器, 但迭代器并不一定是生成器,它是python提供的通过简便方法写出迭代器的一种手段
    4. 包含关系: 可迭代对象 > 迭代器 > 生成器
"""