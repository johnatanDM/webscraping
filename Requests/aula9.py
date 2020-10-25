import requests

proxies = {'http':'162.159.244.26:80'}

url = 'https://www.hide-my-ip.com/pt/proxylist.shtml'

try:
    r = requests.get(url, proxies=proxies)
    print(r.status_code)
except requests.exceptions.ConnectionError as e:
    print(str(e))