import requests

url = 'https://st4.depositphotos.com/3591429/21905/i/1600/depositphotos_219059996-stock-photo-little-kids-halloween-party.jpg'

r = requests.get(url)

with open('img.jpg', 'wb') as f:
    f.write(r.content)