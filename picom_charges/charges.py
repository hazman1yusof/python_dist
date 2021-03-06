import ConfigParser
import mysql.connector
import datetime

db_conf = ConfigParser.RawConfigParser()
db_conf.read('db.ini')
db_conf_sect = db_conf.sections()

for (key, val) in db_conf.items('DATA1'):
    if(key == 'host'):
        host=val
    elif(key == 'user'):
        user=val
    elif(key == 'passwd'):
        passwd=val
    elif(key == 'database'):
        database=val

mydb = mysql.connector.connect(
    host=host,
    user=user,
    passwd=passwd,
    database=database
)


mycursor = mydb.cursor()

f = open("mrnepis.txt", "r")
mrnepis = f.read().strip("|").split("|")

query = ("SELECT mrn, episno, chgcode, quantity, trxdate, trxtime, isudept, lastuser, lastupdate, idno FROM chargetrx "
         "WHERE mrn = %s AND episno = %s")

mycursor.execute(query, mrnepis)

f = open("charges.txt", "w")
for (mrn, episno, chgcode, quantity, trxdate, trxtime, isudept, lastuser, lastupdate, idno) in mycursor:
  f.write(str(mrn)+
    "|"+str(episno)+
    "|"+str(chgcode)+
    "|"+str(quantity)+
    "|"+str(datetime.datetime.strptime(str(trxdate), '%Y-%m-%d').strftime('%d/%m/%Y'))+
    "|"+str(trxtime)+
    "|"+str(isudept)+
    "|"+str(lastuser)+
    "|"+str(datetime.datetime.strptime(str(lastupdate), '%Y-%m-%d').strftime('%d/%m/%Y'))+
    "|"+str(idno)
    )
  f.write("\n")


f.close()
mycursor.close()
mydb.close()
