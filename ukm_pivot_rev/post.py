import requests

url = 'http://eis.medicsoft.com.my/post'
files = {'file': open('pivot.ini', 'rb')}

r = requests.post(url)
print r.text