"""
一、协程的概念
    1. 计算机本身不存在, 由程序员构造出来的, 又被称为微线程
    2. 简而言之, 就是在一个线程中实现代码块相互切换执行
    3. 意义: 程序遇到IO等待时, 自动切换 (如网络请求、文件读写)
"""
import asyncio
import aiohttp
import time

async def func1(x):
    """异步请求（requests 是同步请求）"""
    async with aiohttp.ClientSession() as session:  # 创建一个异步环境（必须）
        async with session.get(url="", verify_ssl=False) as resp:  # 同上
            data = await resp.content.read() # 拿到的是字节串
            print(data.decode('gbk'))
    
async def func2(x):
    """异步文件写操作"""
    async with open() as f:
        print("await f...")

def callbackfunc(x):
    print(f"Get result ==>> {x.result()}")

async def main(x):
    """main() 是固定写法, 会自动执行loop"""
    print(f"start ==>> {time.strftime('%X')}")
    
    tasks = [
        asyncio.create_task(func1(x)),
        asyncio.create_task(func2(x))
    ]
    # 任务执行完后自动回调
    tasks[0].add_done_callback(callbackfunc)
    # 自动收集每一个任务的返回值, 代替 task对象.result(), 以list返回
    ret = await asyncio.gather(*tasks)
    print(ret)
    print(f"end ==>> {time.strftime('%X')}")
    
asyncio.run(main(10))  # 运行的main必须是协程任务