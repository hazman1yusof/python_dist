import mysql.connector

mydb = mysql.connector.connect(
  host="medicsoft.com.my",
  user="medicsof",
  password="ms0126215840",
  database="medicsof_hisdb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT mrn,newic,dept,adddate,addtime FROM pre_episode WHERE adddate  >= CURDATE() - INTERVAL 1 DAY AND adddate < CURDATE() + INTERVAL 1 DAY")

myresult = mycursor.fetchall()

with open('qrcode.txt', 'w') as f:
	# f.write('MRN|Episno|Newic|addate|dept\n')
	for x in myresult:
		count = 0
		for y in x:
			if(count == 3):
				f.write(str(y.strftime('%d-%m-%Y'))+'|')
			else:
				f.write(str(y)+'|')
			count += 1
		f.write('\n')