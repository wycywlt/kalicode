import asyncio
from pyppeteer import launch
from lxml import etree


async def main():
    # headless参数设为False，则变成有头模式
    browser = await launch(
        headless=False,
        #可在浏览器中输入chrome://version/，在页面的"个人资料路径"查看浏览器的执行程序
        executablePath='/opt/google/chrome/google-chrome'
    )
    page = await browser.newPage()

    await page.goto('https://news.163.com/domestic/')

    await asyncio.sleep(3)
    # 打印页面文本
    page_text = await page.content()

    return page_text


def parse(task):
    page_text = task.result()
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//div[@class="data_row news_article clearfix "]')
    for div in div_list:
        title = div.xpath('.//div[@class="news_title"]/h3/a/text()')[0]
        print('wangyi:', title)


# tasks = []
# task1 = asyncio.ensure_future(main())
# task1.add_done_callback(parse)
# tasks.append(task1)
# asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
c = main()
task = asyncio.ensure_future(c)
task.add_done_callback(parse)
asyncio.get_event_loop().run_until_complete(task)