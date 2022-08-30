import subprocess
import ConfigParser
import mysql.connector
import shutil
import ftplib
import datetime

db_conf = ConfigParser.RawConfigParser()
db_conf.read('db.ini')
foxitpath=db_conf.get('DATA1','foxitpath')
filepath=db_conf.get('DATA1','filepath')
blankpath=db_conf.get('DATA1','blankpath')
ftppath=db_conf.get('DATA1','ftppath')


f = open("mrnepis.txt", "r")
read = f.read().split(',')
f.close()

mrn = read[0]
epis = read[1]
type_ = read[2]
filename=type_+'_'+mrn+'_'+epis+".pdf"

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
mycursor = mydb.cursor(buffered=True)
query = ("SELECT * FROM patresult WHERE mrn = %s AND episno = %s AND type = %s")
mycursor.execute(query, (mrn, epis, type_))


ftp = ftplib.FTP("ftp.medicsoft.com.my")
ftp.login("hazman@medicsoft.com.my", "rahsia123")
ftp.cwd('/public_html/patientcare/public/uploads/pdf')

if mycursor.rowcount == 1:
	#get from server
	print('get from server')
	ftp.retrbinary('RETR %s'%filename,open(filepath+filename, 'wb').write)

	
	p = subprocess.Popen([foxitpath,filepath+filename], shell=True, stdout = subprocess.PIPE)
	p.wait()

	file = open(filepath+filename,'rb')
	ftp.storbinary('STOR %s'%filename, file)

	now = datetime.datetime.utcnow()
	query = ("UPDATE patresult set upduser = %s, upddate=%s  WHERE	mrn = %s and episno = %s and type = %s")
	data = ('system',now.strftime('%Y-%m-%d %H:%M:%S'),mrn,epis,type_)
	mycursor.execute(query, data)

	mydb.commit()
	file.close()
	ftp.close()
	mycursor.close()

else:
	#copy from blank file
	print('copy from blank file')
	src=blankpath+type_+".pdf"
	dst=filepath+filename

	shutil.copy(src,dst)

	
	p = subprocess.Popen([foxitpath,filepath+filename], shell=True, stdout = subprocess.PIPE)
	p.wait()

	file = open(filepath+filename,'rb')
	ftp.storbinary('STOR %s'%filename, file)

	now = datetime.datetime.utcnow()
	query = ("INSERT INTO patresult (resulttext,attachmentfile,mrn,type,episno,upduser,upddate) VALUES (%s,%s,%s,%s,%s,%s)")
	data = (filename,'pdf/'+filename,mrn,type_,epis,'system',now.strftime('%Y-%m-%d %H:%M:%S'))
	mycursor.execute(query, data)

	mydb.commit()
	file.close()
	ftp.close()
	mycursor.close()
