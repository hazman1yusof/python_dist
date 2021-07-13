import ConfigParser
import mysql.connector


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


query = ("SELECT mrn, episno, ordercomplete FROM episode "
         "WHERE mrn = %s AND episno = %s")

mycursor.execute(query, mrnepis)

f = open("episode.txt", "w")
for (mrn, episno, ordercomplete) in mycursor:
  f.write(str(mrn)+"|"+str(episno)+"|"+str(ordercomplete)+"|")



f.close()
mydb.commit()
mycursor.close()
mydb.close()
