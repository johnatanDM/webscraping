import requests

url = 'https://www.youtube.com/results?'
payload = {'search_query':'como fazer estrogonofe de frango'}

r = requests.get(url, params=payload)

print(r.url)
print(r.encoding)

with open('youtube.html', 'wb') as f:
    f.write(r.content)