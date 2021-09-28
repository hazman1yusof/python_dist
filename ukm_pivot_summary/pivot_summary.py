import ConfigParser
import mysql.connector
import requests

db_conf = ConfigParser.RawConfigParser()
db_conf.read('rev.ini')

for (key, val) in db_conf.items('DATA1'):
    if(key == 'month'):
        month= val[1:]
    elif(key == 'year'):
        year=val[1:]

print('generate summary dashboard for month '+month+' and year '+year)

url = 'https://www.ukmsc.com.my/eis/public/store_dashb?month='+month+'&year='+year
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)

print('dashboard updated form month '+month+' and year '+year)
