"""
1. 什么是字符串编码：本质就是二进制与语言文字的对应关系
2. 常见的编码方式：
    - ASCII: 表示英语及西欧语言
    - GB2312: 简体中文字符集，兼容ASCII
    - GBK: GB2312的扩展字符集，支持繁体字，兼容GB2312
    - Unicode: 国际标准组织统一标准字符集
        所有字符都是两个字节，转化速度快，占用空间大
    - UTF-8: 不定长编码
        对不同字符不同长度，节省空间，转化速度比较慢
3. 编码和解码
    编码: encode()  # bytes, 以字节为单位进行处理
    解码: decode()  # str...

4. 字符串运算符
    - 加 (+), 字符串拼接
    - 乘 (*), 重复字符串
    - 成员运算符，检查字符串中是否包含了某个或多个字符
        in: 包含返回 True
        not in: 不包含返回 True
    - 索引
        [i] / [m:n] / [m:] / [:n] / [m:n:step]
        如果是从右往左切，步长因为负数
    - 字符串常见操作
        .find() / .index()
            find没找到返回-1, index没找到报错
        .count()
        .replace()
        .split()
        .capitalize()
        .startwith() / .endwith()
        .lower() .islower() / .upper() .isupper()
"""