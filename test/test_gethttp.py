import requests

url = 'https://medicsoft.com.my/patientcare/public/store_dashb?month=5&year=2021'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)
print(result.content.decode())