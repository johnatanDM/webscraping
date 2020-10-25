import requests

url = 'https://www.submarino.com.br'

r = requests.get(url)
cookie = r.cookies.get_dict()

busca = 'notebook'
url = f'https://www.submarino.com.br/busca?conteudo={busca}'

r = requests.get(url, cookies=cookie)
with open('submarino.html', 'w', encoding='utf8') as f:
    f.write(r.text)