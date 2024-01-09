import requests
from lxml import etree


headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

#对首页进行数据请求
url = 'https://bixuejian.5000yan.com/'
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
page_text = response.text

#数据解析：解析章节的标题&详情页url
tree = etree.HTML(page_text)
zhangjie_list = tree.xpath('/html/body/div[2]/div[1]/main/ul/li')

fp = open('xiaoshuo.txt', 'w')

for list in zhangjie_list:
    title = list.xpath('./a/text()')[0]
    title_url = list.xpath('./a/@href')[0]
    detail_title = requests.get(url=title_url, headers=headers)
    detail_title.encoding='utf-8'
    detail_text = detail_title.text
    detail_tree = etree.HTML(detail_text)
    content = detail_tree.xpath('/html/body/div[2]/div[1]/main/section/div[1]//text()')
    content = ''.join(content).strip()
    fp.write(title + ':' + content + '\n')
    print(title + ':下载成功')
fp.close()