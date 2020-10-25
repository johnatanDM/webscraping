import requests
from bs4 import BeautifulSoup

def get_http(url, nome_livro):
    nome_livro = nome_livro.replace(' ', '%20')
    url = f'{url}/busca?q={nome_livro}'

    try: 
        return requests.get(url)
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException,
            requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            print(str(e))
            pass
    except Exception as e:
        raise 

if __name__ == '__main__':
    url = 'https://busca.saraiva.com.br/'
    nome = 'Harry Potter'

    r = get_http(url, nome)

    with open('result.html', 'w', encoding='utf8') as f:
        f.write(r.text)