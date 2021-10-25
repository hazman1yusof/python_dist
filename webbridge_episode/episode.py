import ConfigParser
import mysql.connector
import requests
import json    
import array
import os.path


array_all = ['episode']

my_all = {}

for ini_name in array_all:
    file_exists = os.path.exists(ini_name+'.ini')

    if(file_exists):
        my_dict = {}

        db_conf = ConfigParser.RawConfigParser()
        db_conf.read(ini_name+'.ini')
        configlist=db_conf.sections()

        for section in configlist:
            my_dict[section] = db_conf.items(section)

        my_all[ini_name] = my_dict

# print my_all


url = 'https://www.medicsoft.com.my/webbridge/public/episode2'
data = my_all
header = {
        'Accept' : 'application/json', 
        'Content-Type' : 'application/json',
        "Accept-Encoding": "gzip, deflate, sdch, br",
        "Accept-Language": "en-US,en;q=0.8",
        "User-Agent": "Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion",
    }

# requests.post(url,data=json.dumps(data),headers = header,timeout=2.0)

post = requests.post(url,data=json.dumps(data),headers = header).text

print(post)