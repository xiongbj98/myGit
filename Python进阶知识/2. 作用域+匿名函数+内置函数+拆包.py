"""
一、作用域
    1. 含义: 变量的生效范围
    2. 全局变量: 在整个文件都有效
    3. 局部变量: 函数内部定义的变量, 从定义位置开始到函数定义结束位置有效
    4. 函数内部修改全局变量的值, 可以使用 global 关键字 (将变量声明为全局变量)
        - 注意语法格式,必须先声明全局变量 [global 变量名]
    5. 关键字 nonlocal: 用来声明外层的局部变量, 只能在嵌套函数中使用, 在外部函数先进行声明
        内部函数进行 nonlocal 声明。e.g
        a = 10  # 全局变量
        def outer():
            a = 5  # 局部变量
            def inner():
                nonlocal a
                a = 20
        # 使用nonlocal关键字后 inner函数a=20, outer a=20(被关键字影响), 全局a=10
    
二、匿名函数
    1. 定义: 函数名 = lambda 形参: 表达式(返回值)
        e.g: add = lambda a,b: a+b
    2. 调用: 结果 = 函数名(实参)
        e.g: print(add(1,2))  # 3
    3. 参数:
        - 无参: lambda: 'no args'
        - 必备参数: lambda a: a
        - 默认参数: lambda name, age=18: (name, age)  # 以元组形式返回
        - 关键字参数: lambda: *args, **kwargs: (args, kwargs)
    4. lambda 结合 if 判断
        - lambda a, b: "a>b" if a>b else "a<=b"
    5. 适用范围: 实现简单逻辑的函数, 简化代码

三、内置函数
    1. 查看所有的内置函数, e.g
        import builtins
        print(dir(builtins))
    2. 常见的内置函数
        - 类型转换
        - abs() 返回绝对值
        - sum() 求和
        - min() / max() 求最小值 / 求最大值
        - zip() 将可迭代对象作为参数, 打包成一个个元组
            取值: 通过 for 循环遍历出来 / 转换成列表
        - map() 对可迭代对象中的每一个元素进行映射, 分别去执行
            取值: 通过 for 循环遍历出来 / 转换成列表
        - reduce()  先把对象中的两个元素取出, 计算出一个值然后保存, 然后跟第三个元素进行计算
            from functools import reduce
            reduce(function, sequence)
            # function -- 必须是有两个参数的函数
            # sequence -- 可迭代对象

四、拆包
    1. 含义: 对于函数的多个返回数据，去掉元组、列表或者字典 直接获取里面数据的过程
    2. 拆包方法
        tua = (1,2,3,4)
        - a,b,c,d = tua
        - a, *b = tua  # 1 [2,3,4]
"""