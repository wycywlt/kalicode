# 特殊的函数：
#     在函数定义前添加一个async关键字，该函数就变成了一个特殊的函数。
#     特殊函数的特殊之处：
#         1. 特殊函数被调用后，函数内部的程序语句不会被立即执行.
#         2. 特殊函数被调用后，会返回一个协程对象
# 协程：
#     特殊函数调用后，返回一个协程对象（协程对象是由特殊函数创建）
#     协程 == 特殊的函数 == 函数 == 一组指定形式的操作
#     协程 == 一组指定形式的操作
# 任务对象：
#     任务对象本质上是一个高级的协程。高级之处是什么？后面讲！
#     任务对象 == 高级协程 == 协程 == 一组指定形式的操作
#     任务对象 == 一组指定形式的操作
#
# 事件循环loop：
#     当做是一种容器。该容器是用来装载多个任务对象。
#     loop就可以将其内部装载的任务对象进行异步的执行。

import asyncio
import time


start = time.time()
urls = [
    'a.com', 'b.com', 'c.com'
]
async def get_requester(url):
    print('正在请求:', url)
    #没有加await关键字之前：每一个任务中的阻塞操作并没有被执行
    #await关键字：必须要加在每一个任务的阻塞操作前，作用就是强调执行任务中的阻塞操作
    #await是用来手动控制任务的挂起操作。
    await asyncio.sleep(2)
    print('请求完毕', url)
    return 123

if __name__ == '__main__':
    #创建三个任务对象和一个事件循环对象
    tasks = []
    for url in urls:
        c = get_requester(url)
        task = asyncio.ensure_future(c)
        tasks.append(task)
    #将三个任务对象添加到一个事件循环对象中
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    print('总耗时：', time.time()-start)
