import requests

url = 'http://compras.dados.gov.br'
cnpj = '07689002000189' #EMBRAER

url_request = f'{url}/contratos/v1/contratos.json?cnpj_contratada={cnpj}'

r = requests.get(url_request)
print(r.json()['_embedded']['contratos'][0])