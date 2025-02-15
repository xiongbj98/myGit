"""
一、初识线程和进程
    - 线程: 计算机中可以被cpu调度的最小单元(工作的单位)
    - 进程: 计算机资源分配的最小单元（提供工作资源的单位, 资源消耗多）
    - 一个程序, 至少有一个进程, 一个进程中至少有一个线程, 最终是线程在工作
    - 同一个进程中的线程可以共享此进程中的资源
    - 线程之间共享资源（全局变量）
"""

def func(x,y,z):
    pass

"""创建一个线程"""
from threading import Thread
t1 = Thread(target=func, args=(1,2,3))

# 启动一个线程
t1.start()

"""创建一个进程"""
from multiprocessing import Process
t2 = Process(target=func, args=(1,2,3))

# 启动一个进程
if __name__ == "__main__":  # win spawn驱动，不加会报错
    t2.start()
    
"""
二、GIL锁 (全局解释器锁)
    1. 让一个进程中同一时刻只能有一个线程可以被CPU调度 (CPython独有)
    2. 多进程适合计算密集型: 程序利用计算机的多核优势, 让CPU同时处理一些任务 (资源开销大)
    3. 多线程合适IO密集型: 程序不利用计算机的多核优势 (文件读写、网络下载)
    4. 实际开发过程中, 进程和线程 配合使用
三、多线程开发
    1. 一个程序开始执行后，会开辟一个进程，一个进程中的主线程开始执行，
        若执行过程中开辟了子线程，主线程代码执行完不会立即结束，而会等待所有子线程结束才结束
    2. 常见方法
        - start(): 当前线程准备就绪, 等待CPU调度, 具体执行时间由CPU决定
        - join(): 控制主线程等待子线程执行结束
        - setDaemon(bool): 设置线程是否是守护线程(必须在start之前)
            守护线程(True): 主线程执行完毕后, 子线程也自动关闭
            默认False, 主线程得等子线程结束才结束
        - 线程对象.setName(): 设置线程的名称 (必须在start之前)
            获取线程名称: threading.current_thread().getName()
        - 自定义线程类
            class MyThread(threading.Thread):
                def run(self):
                    print('执行此线程', self._args)
            t = MyThread(args=(1,2))
"""

"""
四、线程安全
    1. 在执行子线程时, 优先执行到lock_obj.acquire()的子线程会锁住该子线程, 其他子线程只能等待
        当执行到lock_obj.release()时, 其他子线程才能开始执行
    2. 在python中部分操作是线程安全的不需要加锁(如 list.append()), 具体需要查看官方文档
"""
import threading

# 创建锁对象
lock_obj = threading.RLock()

# 创建子线程执行函数
def funcA():
    lock_obj.acquire()  # 申请锁
    # do something...
    lock_obj.release() # 释放锁
    
def funcB():
    lock_obj.acquire()  # 申请锁
    # do something...
    lock_obj.release() # 释放锁
    
def func():
    with lock_obj: # 自动执行 acquire 和 release
        pass
    
"""
五、线程锁&死锁
    1. threading.RLock()
        - 递归锁, 支持锁多次, 解锁也需要同样次数
    2. threading.Lock()
        - 同步锁,只支持一次锁一次解, 不支持多次锁和解锁
        - 如果一个同步锁对象被多次上锁,便会出现死锁,程序不再往下执行
六、线程池
    1. 当线程创建太多, 反而会降低执行效率, 这时就需要线程池
"""

# 创建线程池
from concurrent.futures import ThreadPoolExecutor
pool = ThreadPoolExecutor(100)  # 表示这个线程池最多维护100个线程
pool.submit()  # 把一个任务交给线程池, 让线程池来安排执行任务 submit(函数名,参数1,参数2)

# 示例代码
def task(url, arg):
    print("开始执行任务")

def outer(arg):  # 闭包函数, 主要用于带参数
    def done(response):
        print(arg)
        print("任务执行完毕后执行", response.result())
    return done

# 创建线程池, 最多维护10个线程
pool1 = ThreadPoolExecutor(10)
urls = [f"www.xxx{i}.com" for i in range(300)]
for url in urls:
    # 在线程池中提交一个任务, 线程池中如果有空闲线程, 则分配一个线程去执行, 执行完毕后再将线程交还给线程池
    # 如果没有空闲, 则等待
    future = pool1.submit(task, url, "arg2")  # future类似于任务编号
    future.add_done_callback(outer(arg="arg"))  # 一个task执行完毕后执行done函数中的内容
print("执行中...")  # 循环完后执行print
pool1.shutdown(True)  # 等待线程池中执行完毕, 再继续执行
print("END")  # 线程池中执行完毕后print

"""
七、单例模式在多线程中实现
    1. 对象存在时, 后续创建的对象都是引用的这个对象
"""
import threading
class SingleCls:
    instance = None
    lock = threading.RLock()
    
    def __init__(self):
        pass
    
    def __new__(cls):
        if cls.instance: return cls.instance
        with cls.lock:
            cls.instance = object.__new__(cls=cls)
            return cls.instance