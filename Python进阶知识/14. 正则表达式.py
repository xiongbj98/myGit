"""
一、正则表达式 re
    1. 含义: 记录文本规则的代码
    2. 特点: 语法复杂,通用性强
    
二、字符
    1. [] 和 | 的区别, []中只能为单字符或, | 左右可单可多字符
三、数量

四、分组 (正则中的小括号)
    1. 提取数据区域
    2. 获取指定区域+或条件
    3. 命名分组 (?P<名称>正则)

五、常见方法
    - findall(): 获取匹配到的所有数据
    - match(): 从起始位置开始匹配,匹配成功返回对象,否则None
    - search(): 浏览整个字符串去匹配第一个,返回对象或None
    - sub(): 替换匹配成功的位置
    - split(): 根据匹配成功的位置分割
    - finditer(): findall返回的只能是列表,finditer返回的是迭代器,如果有命名分组,可以字典形式取值(groupdict())
"""

class SLS(object):
    
    attr_a = "ATT_A"
    
sls = SLS()
print(SLS.attr_a)
print(sls.attr_a)
sls.attr_a = "SLS_A"
SLS.attr_a = "ATT_B"
print(SLS.attr_a)
print(sls.attr_a)