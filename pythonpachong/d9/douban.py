from time import sleep
from selenium import webdriver
from lxml import etree
bro = webdriver.Chrome(executable_path='./chromedriver')
bro.get('https://movie.douban.com/typerank?type_name=%E6%82%AC%E7%96%91&type=10&interval_id=100:90&action=')
sleep(2)
bro.execute_script('document.documentElement.scrollTo(0,2000)')
sleep(20)
#获取页面源码数据
page_text = bro.page_source
#数据解析：解析页面源码数据中动态加载的电影详情数据
tree = etree.HTML(page_text)
ret = tree.xpath('//*[@id="content"]/div/div[1]/div[6]/div/div/div/div[1]/span[1]/a/text()')
print(ret)
bro.quit()