import ConfigParser
import mysql.connector


def date(string):
    date_ = string.split('/')
    date = date_[2]+'-'+date_[1]+'-'+date_[0]
    return date

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

config = ConfigParser.RawConfigParser()
config.read('rev.ini')
configlist=config.sections()

year=''
month=''
datetype=''
for section in configlist:
    for (key, val) in config.items(section):
        if(year != '' and month != '' and datetype != ''):
            break
        elif(key == 'datetype'):
            datetype=val
        elif(key == 'year'):
            year=val
        elif(key == 'month'):
            month=val

de_tuple = (month,year,datetype)
del_pat = 'delete from pateis_rev where month = %s and year = %s and datetype = %s'
mycursor.execute(del_pat, de_tuple)
print('deleted month - '+month+' year - '+year+' datetype - '+datetype)

for section in configlist:
    list_ = []
    for (key, val) in config.items(section):
        if (key == 'regdate'):
            if (val.strip() == ""):
                val = None
            else:
                val = date(val)
        elif (key == 'disdate'):
            if (val.strip() == ""):
                val = None
            else:
                val = date(val)
        list_.append(val)

    tuple_ = tuple(list_)

    add_pat = 'insert into pateis_rev '
    add_pat += '(units,mrn,episno,epistype,chgcode,chgdesc,groupcode,groupdesc,chgtype,typedesc,quantity,unitprice,amount,month,quarter,year,regdate,disdate,datetype)'
    add_pat += ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    mycursor.execute(add_pat, tuple_)
    print('added row section - '+section)

mydb.commit()
mycursor.close()
