import requests


login_url = 'https://passport.17k.com/ck/user/login'
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

data = {
    "loginName": "15026554361",
    "password": "Lzy2293916034*"
}

session = requests.Session()

session.post(url=login_url, headers=headers, data=data)

book_url = 'https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919'
page_text = session.get(url=book_url, headers=headers).json()

print(page_text)

requests.session()