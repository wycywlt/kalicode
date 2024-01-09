import asyncio
import time


async def get_request(url):
    print('ping:', url)
    time.sleep(2)
    print('done', url)
    return 123

c = get_request('a.com')
task = asyncio.ensure_future(c)

def task_callback(t):
    ret = t.result()
    print('回调函数返回值是:', ret)

task.add_done_callback(task_callback)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)