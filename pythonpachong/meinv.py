import requests
from lxml import etree
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/119.0.0.0 Safari/537.36'
}
for page in range (1, 3):
    if page == 1:
        url = 'http://pic.netbian.com/4kmeinv/'
    else:
        url = f'http://pic.netbian.com/4kmeinv/index_{page}.html'

    #获取首页数据
    main_page = requests.get(url=url, headers=headers)
    main_page.encoding = 'gbk'
    main_page_text = main_page.text

    #解析图片title和链接
    tree = etree.HTML(main_page_text)
    li_list = tree.xpath('//*[@id="main"]/div[3]/ul/li')
    for li in li_list:
        title = li.xpath('.//b/text()')[0]
        detail_url = 'http://pic.netbian.com/' + li.xpath('./a/@href')[0]

        #获取图片详情页面数据
        detail_page = requests.get(url=detail_url, headers=headers)
        detail_page.encoding = 'gbk'
        detail_page_text = detail_page.text

        #解析图片大图下载链接
        detail_tree = etree.HTML(detail_page_text)
        download_url = 'http://pic.netbian.com/' + detail_tree.xpath('//*[@id="img"]/img/@src')[0]

        #对图片地址发请求
        data_img = requests.get(url=download_url, headers=headers).content
        img_path = './img/' + title + '.jpg'

        #持久存储
        with  open(img_path,'wb') as fp:
            fp.write(data_img)
        print(title + '下载成功')
