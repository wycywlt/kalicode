import requests
from lxml import etree


main_url = 'https://www.51miz.com/shipin/'

headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/119.0.0.0 Safari/537.36'
}
response = requests.get(url=main_url, headers=headers)
page_text = response.text

#jiexi
tree = etree.HTML(page_text)
a_list = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/a')

for a_li in a_list:
    src = a_li.xpath('./div/div/div/video/source/@src')[0]
    download_url = 'https:' + src

    video_data = requests.get(download_url).content
    video_title = './video/' + download_url.split('/')[-1]
    with open(video_title, 'wb') as fp:
        fp.write(video_data)
    print(video_title, '下载成功')


