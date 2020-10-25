import requests
from bs4 import BeautifulSoup
url = 'http://www.google.com/'

r = requests.get(url)

print(r.status_code)
'''
if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'html.parser')
'''

#print(r.headers['Set-cookie'])

print(r.request.headers)
