"""
一、进程三大模式
    1. 注意点: 进程启动需要从 main代码块启动 (spawn / forkserver)
    2. fork 模式: 
        - 进程在创建时 子进程拷贝主进程中的数据单独开辟内存空间, 之后主进程和子进程数据相互独立不影响
        - 支持文件对象和线程锁
    3. spawn 模式:
        - 创建子进程时 子进程不会主动拷贝进程数据,需要以参数传入 (之后数据独立)
        - 但是文件对象和线程锁不支持参数传入 (进程锁可以)
    4. forkserver 模式:
        - 创建子进程时 同spawn
    5. 进程的状态
        - 就绪状态: 等待cpu调度
        - 执行状态: cpu正在执行
        - 等待状态（阻塞状态）: 等待某些条件满足, 比如sleep
        
二、进程常见方法
    1. start(): 当前进程准备就绪, 等待被CPU调度
    2. join(): 等待当前进程的任务执行完毕后再继续执行
    3. 进程对象.daemon: 设置为守护/非守护进程
    4. 进程对象.name: 设置进程名称
    5. mutiprocessing.current_process().name: 获取进程名
    6. os.getpid():  获取主进程、子进程的pid
    7. os.getppid(): 父进程pid (在子进程中获取主进程的pid)
    8. threading.enumerate(): 获取进程中的线程数
    9. 自定义进程类,MyClass(mutiprocessing.Process): def run(self): pass
    10. 通常来讲, CPU多少个数, 创建多少进程-1 (出去主进程), 获取CPU核数: mutiprocessing.cpu_count()
    
三、进程之间数据共享
    1. 方式1 (了解): 通过Value or Array 实现
    2. 方式2 (常见): 通过 Manager() 实现
    3. 方式3 (常见): 通过 Queues 队列实现
    4. 方式4: 通过 Pipes 管道实现
    5. 其他 (最多): 文件、数据库、redis等
    6. Queue 队列
        - q.put() : 放入数据
        - q.get() : 取出数据
        - q.empty() : 判断队列是否为空
        - q.qsize() : 返回当前队列包含的消息数量
        - q.full() : 判断队列是否满了
        - 创建队列: q = Queue(3) 最多可以接收3条消息,默认无限制直到内存的尽头
    
四、进程锁
    1. 多个进程共享同一个资源时使用 (避免数据混乱)
    2. 创建锁 mutiprocessing.RLock(), 创建线程时将锁作为参数传入
    3. spawn 模式, 需要特殊处理 (子进程未执行完,主进程需sleep或者join,否则报错)
    
五、进程池
    1. 控制同时处理数据的进程数量
    2. 创建进程池: 
        from concurrent.futures import ProcessPoolExecutor
        pool = ProcessPoolExecutor(4)  # 创建容量为4的进程池
        pool.submit()  # 提交到进程池
        pool.add_done_callback(done)  # 单个进程执行完后的回掉, 由主进程执行done (相对应线程的回调则由子线程执行)
            def done(res): 这里的res是对应task的return
            res.result() 获取task的return
        pool.shutdown(True)  # 阻塞 (主进程等待所有子进程结束后往下执行)
"""