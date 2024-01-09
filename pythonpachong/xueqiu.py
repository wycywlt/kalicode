import requests
import os
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Cookie": "xq_a_token=4fda997cf0d3bc4ef43eba42532cf38a54bcbc00; xqat=4fda997cf0d3bc4ef43eba42532cf38a54bcbc00; xq_r_token=a440894245f0f9be071ea5c41d674edb42789120; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcwMzI5MTg4MiwiY3RtIjoxNzAxMjQ1NTgzMDUxLCJjaWQiOiJkOWQwbjRBWnVwIn0.hvzWOLRyzyTLbJH6gDNKs1owxodNRz-8T6bXdlFGtLquq2WhsZBSN8lYsam6hoclupQ0etIUrlUgnmh0xKRH1AM56kql6MlEciyQ3u_RCPbNnvXLPpufkmROgKjGKEh5EkFOfiXiWQaZr2MshangcmlOr9bRJlsUbIUx3AWBJqBL6OwbXEDjTR4Z-g-PY7ZyMbuad7ibz8Fd7FyuSEcX5VxrzUj37upVr3e-eYc1srQuZGDWljgcQjV_O4Emb_Nlp5OmeJ_K47zLkCoXMAZYt0elubBzRF-wRWum1QjrJ08fY4AReh2q5jnS5hAwf3bkfoqXmQaoe7quv1nbHoGXCA; cookiesu=901701245639522; u=901701245639522; device_id=8076218da9cc652a91b983a28ac6c3bf; Hm_lvt_1db88642e346389874251b5a1eded6e3=1701245642; acw_tc=2760827f17012474591267727e0ffdba86c1f9b08200b653bf1933297341e6; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1701247798"
}

url = "https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=564771&size=15"

params ={
    "since_id": "-1",
    "max_id": "564771",
    "size": "15"
}

response = requests.get(url=url, headers=headers, params=params)
data = response.json()
print(data)