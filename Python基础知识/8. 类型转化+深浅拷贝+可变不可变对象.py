"""
一、类型转换
    1. int()
        - 如果是字符串只能转换由纯数字组成的字符串
        - 浮点型强转会舍到小数点及其后面的数值，保留整数部分
    2. float()
        - 整形转换为浮点型, 会自动添加一位小数
        - 如果是字符串,除正负号、数字、小数点以外的字符,则不支持转换
    3. str()
        - 转化为字符串类型, 任何类型都可以
        - float 转换 str会取出末位为0的小数部分
    4. eval()
        - 执行运算
        - 可以实现list、dict、tuple、str之间的转换
        - 非常强大, 但不太安全
    5. list()
        - 将可迭代对象转换成列表 (str, tuple, dict, set)
        - 字典转列表取键名
        - 集合转换成列表会先去重再转换
"""

"""
二、深浅拷贝
"""
li1 = [1,2,3]
li2 = li1
li1.append(4)
# print(li1, li2)  # 两个都是 [1,2,3,4]
# 赋值：等于完全共享资源，一个值的改变会完全被另一个值共享（内存地址相同）

# =====浅拷贝 (数据半共享)=====
# 会创建新的对象, 拷贝第一层的数据, 嵌套层会指向原来的内存地址
import copy
li3 = [1,2,3,[4,5,6]]
li4 = copy.copy(li3)  # 浅拷贝
# print("li3 内存地址", id(li3))  # 4376590208
# print("li4 内存地址", id(li4))  # 4376767296
# li3 li4内存地址不一样，如果更改其中一个列表的数据，另一个数据不受影响，eg
li3.append(7)
# print(li3, li4)
# 第二层数据一致是相同的，因此是浅拷贝
li4[3].append(8)
# print(li3, li4)  # 由于第二层数据内存地址相同，资源会被完全共享

# =====深拷贝 (数据完全不共享)=====
# 外层的对象和内部的元素都拷贝了一遍
import copy
li5 = [1,2,3,[4,5,6]]
li6 = copy.deepcopy(li5)  # 深拷贝
# print("li5 内存地址", id(li5))  # 4376590208
# print("li6 内存地址", id(li6))  # 4376767296
# 内存地址独立，同浅拷贝
# 第二层数据也是独立的，因此是深拷贝
li6[3].append(8)
# print(li5, li6)  # 二层数据独立

"""
三、可变类型
    含义: 变量对应的值可以增删改, 但是内存地址不会发生改变
    常见的可变类型:
        - list / dict / set
        
四、不可变类型
    含义: 存储空间保存的数据不允许被修改, 如果修改便会生成新的值且分配新的内存空间
    常见的不可变类型:
        - int / str / tuple
        
深浅拷贝只针对可变对象, 因此对于不可变对象不存在深浅拷贝
"""