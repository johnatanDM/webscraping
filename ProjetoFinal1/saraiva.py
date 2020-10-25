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
    except Exception as e:
        raise 

def get_produto(content):
    soup = BeautifulSoup(content, 'lxml')
    produtos = soup.find_all('li', {'class':'nm-product-item'})

    lista_produtos = []
    for produto in produtos:
        info_produto = [f'https:{produto.a.get("href")}', produto.a.get('title')]
        lista_produtos.append(info_produto)
    return(lista_produtos)


def get_http_page_produto(lista_produtos):
    for produto in lista_produtos:
        print(produto)
        try: 
            r = requests.get(produto[0])
        except (requests.exceptions.HTTPError, requests.exceptions.RequestException,
            requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            print(str(e))
            r = None
        except Exception as e:
            raise 
        
        parse_page_produto(r.text, produto[0], produto[1])
        break

def parse_page_produto(content, url_produto, titulo):
    soup = BeautifulSoup(content, 'lxml')
    with open('result.html', 'w', encoding='utf8') as f:
        f.write(content)


if __name__ == '__main__':
    url = 'https://busca.saraiva.com.br/'
    nome = 'Harry Potter'

    r = get_http(url, nome)
    if r: 
        lista_produtos = get_produto(r.text)
        get_http_page_produto(lista_produtos)



'''
    não vamos mais escrever em arquivo
    with open('result.html', 'w', encoding='utf8') as f:
        f.write(r.text)
'''
