import requests

main_url = "https://blog.wycywlt.ink/"

response = requests.get(url=main_url)

response.encoding = 'utf-8'

page = response.text

with open('dongfang.html','w') as fp:
    fp.write(page)

