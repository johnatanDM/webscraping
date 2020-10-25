import requests

url = 'http://www.submarino.com.br'

s = requests.Session()
s.get(url)
cookie = s.cookies.get_dict()

busca = 'notebook'
url = f'http://www.submarino.com.br/busca/{busca}'

r = s.get(url)
with open('submarino2.html', 'w', encoding='utf8') as f:
    f.write(r.text)