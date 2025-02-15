"""
一、递归函数
    1. 含义: 如果一个函数在内部调用它本身, 这个函数就是递归函数
    2. 条件:
        - 明确的结束条件（递归出口）
        - 每进行一次递归, 问题规模相比上次递归都要有所减少
        - 相邻两次重复之间有紧密联系
    3. e.g
        - 实现1~100累加和
            def add(n):
                if n == 1: return 1  # 递归出口
                return n + add(n-1)
        - 斐波那契数列
            规律: 1,1,2,3,5,8,13...
            def fun(n):  # n 代表第几项
                if n <= 1: return n
                return fun(n-2) + fun(n-1)
    4. 优缺点
        - 优点: 简洁、逻辑清晰、解题更有思路
        - 缺点: 需要反复调用, 耗内存, 运行效率低 (代码简洁用循环, 代码冗长用递归)
    
二、闭包
    1. 含义: 在嵌套函数的前提下, 内部函数使用了外部函数的变量, 而且外部函数返回了内部函数,
        我们就把使用了外部函数变量的内部函数称为闭包
    2. 条件:
        - 函数嵌套 (函数里再定义函数)
        - 内层函数使用外层函数的局部变量
        - 外层函数的返回值是内存函数的函数名
    3. 定义一个闭包函数
        def outer():
            n = 10
            def inner():
                print(n)
            return inner  # 返回函数名, 是因为inner函数里参数比较多或者受到限制时,写法不规范
        print(outer())  # 返回的是内部函数的内存地址
        【调用方法】
            - outer()()
            - ot = outer() \n ot()
    4. 带参数的闭包函数
        def outer(m):  # m是形参, 也是外函数的局部变量
            n = 10
            def inner():
                print(n+m)
            return inner
    5. 每次开启内函数都在使用同一份闭包变量
        def outer(m):
            def inner(n):
                return n+m
            return inner
        ot = outer(10)
        # 第一次调用内函数给inner传值
        ret = ot(20)  # ret = 30
        # 第一个调用inner
        ret = ot(40)  # 50
    6. 总结
        使用闭包的过程中,一旦外函数被调用,返回了内函数的引用,虽然每次调用内函数会开启一个函数执行后消亡,
            但是闭包变量实际上只有一份,每次开启内函数都在使用同一个闭包变量

三、装饰器(本质就是闭包函数实现)
    1. 作用: 不改变原函数的情况下拓展其他功能
    2. 条件
        - 不修改原程序或函数的代码
        - 不改变函数或程序的调用方法
    3. 语法糖
        - 格式 @装饰器名称
    4. 定义一个装饰器(带参数)
        def decoratorWithArgs(*params, **kwparams):  # 装饰器带参数
            def outer(fun):
                def inner(*args, **kwargs):  # 被装饰函数带参数
                    # setup...
                    ret = fun(*args, **kwargs)
                    # teardown...
                    return ret
                return inner
            return outer
    5. 多个装饰器
        @dec1
        @dec2
        def test():
            print("test...")
        【执行顺序】
        离函数最近的装饰器先装饰,由内到外的装饰过程
"""