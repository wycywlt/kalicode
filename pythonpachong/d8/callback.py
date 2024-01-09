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

async def get_request(url):
    print('正在请求的网址是:',url)
    time.sleep(2)
    print('请求网址结束！')
    return 123

#如何获取特殊函数内部的返回值（任务对象回调函数来实现的）
c = get_request('www.1.com')
task = asyncio.ensure_future(c)
#给任务对象绑定一个回调函数（回头调用的函数）,该函数一定是在任务对象被执行完毕后再调用的函数
def task_callback(t): #必须有且仅有一个参数
    #函数的参数t就是回调函数的调用者task任务对象本身
    ret = t.result() #任务对象调用result()就可以返回特殊函数的内部return后的结果值
    print('我是回调函数，我被执行了，t.result()返回的结果是:',ret)
#给task任务对象绑定了一个叫做task_callback的回调函数
task.add_done_callback(task_callback)
loop = asyncio.get_event_loop()
loop.run_until_complete(task)