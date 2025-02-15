"""
一、异常
    1. 含义: 程序执行过程中出现的非正常现象
    2. 异常处理
        - 根据控制台的错误提示找到异常点并分析改正
        - 捕获异常
            try:
                不确定是否能够正常执行的代码
            except NameError:
                捕获指定异常
            except (TypeError, NameError):
                捕获多个异常
            except Exception as e:
                捕获所有异常
            else:
                没有异常时执行
            finally:
                无论是否异常都执行
    3. 自定义异常
        - 创建一个Exception("xxx")对象, 然后抛出异常
            e.g: raise Exception("xxx")
        - 自己创建异常类
            e.g: 
                class MyException(Exception):
                    pass
    
二、模块
    1. 含义: 一个py文件就是一个模块, 导入一个模块本质上就是执行一个py文件
    2. 内置模块
        - random / time / os / logging
    3. 第三方模块
        - openpyxl
        - 需要通过 pip install 进行安装的模块
    4. 自定义模块
        - 要遵循命名规范, 且不与内置模块冲突
    5. 导入模块
        - import 模块名1,模块名2,...
        - from 模块名 import 功能(函数)1,功能(函数)2...
        - from 模块名 import *  (导入所有功能、函数)
        - import 模块名 as 别名
        - from 模块名 import 功能名1 as 别名1, 功能名2 as 别名2
    6. 内置全局变量
        - if __name__ == "__main__":
            作用: 用来控制py文件在不同的应用场景执行不同的逻辑
            - 文件自己执行时 __name__ == "__main__"
            - 文件被导入时 __name__ == 模块名
        
三、包
    1. 含义: 项目结构中的目录
    2. 区别于普通文件夹, 包含有 __init__.py, 首先会执行 init 文件中的内容
        init内容,方式一: 「from 包名 import 模块名」, 而后在其他地方就可以直接 「import 模块名」
        init内容,方式二: __all__ = ["模块名1", "模块名2"], 而后通过 「from 包名 import *」导入列表中的模块
    3. 作用: 将有联系的模块放到同一个文件夹下, 有效避免模块名称冲突问题, 让结构清晰
    4. 补充, 包本质依然是模块, 包又可以包含包

"""
