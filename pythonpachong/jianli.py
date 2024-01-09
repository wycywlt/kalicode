import requests
from lxml import etree


headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
     Chrome/119.0.0.0 Safari/537.36"

}

for i in range(1, 3):
    if i == 1:
        main_url = 'https://sc.chinaz.com/jianli/free.html'
    else:
        main_url = f'https://sc.chinaz.com/jianli/free_{i}.html'
    print(f'正在爬取第{i}页的数据')

    #请求主页 数据
    response_free = requests.get(url=main_url, headers=headers)
    response_free.encoding = 'utf-8'
    response_page_text = response_free.text

    #获得标题&超链
    tree = etree.HTML(response_page_text)
    div_list = tree.xpath('//*[@id="container"]/div')
    for div in div_list:
        detail_url = div.xpath('./a/@href')[0]
        title = div.xpath('./p/a/text()')[0]

        #请求详情页面
        detail_page = requests.get(detail_url)
        detail_page.encoding = 'utf-8'
        detail_page_text = detail_page.text

        #解析详情页面
        detail_tree = etree.HTML(detail_page_text)
        download_url = detail_tree.xpath('//*[@id="down"]/div[2]/ul/li[1]/a/@href')[0]

        #发起请求，下载数据
        data = requests.get(url=download_url, headers=headers).content
        filename = './jianli/' + title + '.rar'
        with open(filename, 'wb') as fp:
            fp.write(data)
        print(f'{title}下载完成')
