import ConfigParser
import mysql.connector
import requests
import json    
import array
import os.path
import ftplib


url = 'https://www.medicsoft.com.my/email_python/public/sendMail'

array_all = ['email']
array_attach = []

HOSTNAME = "ftp.mmedicsoft.com.my"
USERNAME = "medics"
PASSWORD = ""

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
            attch = db_conf.items(section)[6][1]
            if(attch not in array_attach):
                array_attach.append(attch)

        my_all[ini_name] = my_dict

ftp = ftplib.FTP("ftp.medicsoft.com.my")
ftp.login("hazman@medicsoft.com.my", "rahsia123")
ftp.cwd('/public_html/email_python/public/attachment')

for attach in array_attach:
    file = open(attach,'rb')
    ftp.storbinary('STOR %s'%attach, file)
    file.close()


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