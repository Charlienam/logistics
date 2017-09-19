import requests

url = "https://my.maerskline.com/tracking/search"
payload = {"searchNumber":"573184350"}
headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
req = requests.get(url, params=payload, headers=headers)

print(req.text)