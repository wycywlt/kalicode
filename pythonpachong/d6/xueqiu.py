import requests
import os
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

url = "https://xueqiu.com/statuses/hot/listV2.json"

params ={
    "since_id": "-1",
    "max_id": "564771",
    "size": "15"
}

#session对象会实时保存跟踪服务器端给客户端的cookie
#创建一个session对象
session = requests.Session()

#从第一次请求开始跟踪cookie
first_url = "https://xueqiu.com/"

#使用session对象进行请求发送：如果该次请求时，服务器端给客户端创建cookie的话，则该cookie就会被保存seesion对象中
session.get(url=first_url, headers=headers)

ret = session.get(url=url, headers=headers, params=params).json()
print(ret)

