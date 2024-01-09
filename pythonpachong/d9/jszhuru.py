from selenium.webdriver import ActionChains
from selenium.webdriver import Chrome

driver = Chrome('./chromedriver',options=chrome_options)
#Selenium在打开任何页面之前，先运行这个Js文件。
with open('./stealth.min.js') as f:
    js = f.read()
#进行js注入，绕过检测
#execute_cdp_cmd执行cdp命令（在浏览器开发者工具中执行相关指令，完成相关操作）
#Page.addScriptToEvaluateOnNewDocument执行脚本
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": js
})

driver.get('https://www.taobao.com')