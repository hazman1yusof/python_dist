import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host='medicsoft.com.my',
    user='medicsof',
    passwd='ms0126215840',
    database='medicsof_hisdb'
)


mycursor = mydb.cursor()

query = ("SELECT mrn, episno, doctorstatus, reg_date FROM episode "
         "WHERE doctorstatus = %s AND reg_date = %s")

mycursor.execute(query, ['SEEN', datetime.datetime.today().strftime('%Y-%m-%d')])

f = open("doctorstatus.txt", "w")
for (mrn, episno, doctorstatus, reg_date) in mycursor:
  f.write(str(mrn)+
    "|"+str(episno)+
    "|"+str(doctorstatus)+
    "|"+str(datetime.datetime.strptime(str(reg_date), '%Y-%m-%d').strftime('%d/%m/%Y'))
    )
  f.write("\n")


f.close()
mycursor.close()
mydb.close()
