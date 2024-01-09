import requests
from urllib.parse import urljoin
import re
import os
import asyncio
import aiohttp
from threading import Thread


dirName = 'tsLib'
if not os.path.exists(dirName):
    os.mkdir(dirName)

headers  = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
#m3u8地址
url = "https://cdn1.tvtvgood.com/202311/17/ac3733369a68/playlist.m3u8?token=RFDG5qtodgGj5XpaG1tXQA&expires=1702458261"
page_text = requests.get(url=url, headers=headers).text
page_text = page_text.strip()


#存储解析出来的每一个ts片段的url
ts_url_list = []
for line in page_text.split('\n'):
    if not line.startswith('#'):
        ts_url = line
        ts_url = 'https://cdn1.tvtvgood.com/202311/17/ac3733369a68/' + ts_url
        ts_url_list.append(ts_url)

#基于协程实现 异步的ts片段的请求
async def get_request(url):
    async with aiohttp.ClientSession() as req:
        async with await req.get(url=url, headers=headers) as response:
            ts_data = await response.read()
            dic = {
                'ts_data': ts_data,
                'ts_title': url.split('/')[-1]
            }
            return dic

def save_ts_data(t):
    dic = t.result()
    ts_data = dic['ts_data']
    ts_title = dic['ts_title']
    ts_path = dirName + '/' + ts_title
    with open(ts_path,'wb') as fp:
        fp.write(ts_data)
    print(ts_title, ':保存下载成功')


tasks = []
for url in ts_url_list:
    c = get_request(url)
    task = asyncio.ensure_future(c)
    task.add_done_callback(save_ts_data)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
