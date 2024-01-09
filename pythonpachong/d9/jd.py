# 导入selenium
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By

#新版的selenium方式
# 选择谷歌浏览器
s = Service(executable_path=r'./chromedriver')
driver = webdriver.Chrome(service=s)
# 输入网址

driver.get("https://www.jd.com/")
search_box = driver.find_element(By.ID, 'key')
search_box.send_keys('xiaomi pad 6 pro')

btn = driver.find_element(By.XPATH, '//*[@id="search"]/div/div[2]/button')
btn.click()
sleep(10)
