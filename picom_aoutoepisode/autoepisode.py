import requests

url = 'http://localhost:8080/patientcare/public/webservice/auto_episode'
header = {
        'Accept' : 'application/json', 
        'Content-Type' : 'application/json',
        "Accept-Encoding": "gzip, deflate, sdch, br",
        "Accept-Language": "en-US,en;q=0.8",
        "User-Agent": "Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion",
    }

# requests.post(url,data=json.dumps(data),headers = header,timeout=2.0)

# get = requests.get(url,data=json.dumps(data),headers = header).text

get = requests.get(url)

f = open("result.txt", "w")
f.write(get)
f.close()