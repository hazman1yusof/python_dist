import subprocess
from datetime import datetime
import configparser
import os

config = configparser.ConfigParser()
config.read('picom_restore.ini')

todel_path = config['DATA1']['folder']

datestr = todel_path.split("_",1)[1]

if os.path.isdir(todel_path):
	print('Restore from folder: '+todel_path)

	debtor = '.\/'+todel_path+'\debtor_'+datestr+'.sql'
	eisdb = '.\/'+todel_path+'\eisdb_'+datestr+'.sql'
	finance = '.\/'+todel_path+'\/finance_'+datestr+'.sql'
	hisdb = '.\/'+todel_path+'\hisdb_'+datestr+'.sql'
	material = '.\/'+todel_path+'\material_'+datestr+'.sql'
	nursing = '.\/'+todel_path+'\/nursing_'+datestr+'.sql'
	sysdb = '.\/'+todel_path+'\sysdb_'+datestr+'.sql'


	# debtor
	p1 = subprocess.Popen('mysqldump --defaults-extra-file=my.cnf debtor < '+debtor, shell=True)
	p1.wait()
	print('Succesfully dump debtor')

	# eisdb
	p2 = subprocess.Popen('mysqldump --defaults-extra-file=my.cnf eisdb < '+eisdb, shell=True)
	p2.wait()
	print('Succesfully dump eisdb')

	# finance
	p3 = subprocess.Popen('mysqldump --defaults-extra-file=my.cnf finance < '+finance, shell=True)
	p3.wait()
	print('Succesfully dump finance')

	# hisdb
	p4 = subprocess.Popen('mysqldump --defaults-extra-file=my.cnf hisdb < '+hisdb, shell=True)
	p4.wait()
	print('Succesfully dump hisdb')

	# material
	p5 = subprocess.Popen('mysqldump --defaults-extra-file=my.cnf material < '+material, shell=True)
	p5.wait()
	print('Succesfully dump material')

	# nursing
	p6 = subprocess.Popen('mysqldump --defaults-extra-file=my.cnf nursing < '+nursing, shell=True)
	p6.wait()
	print('Succesfully dump nursing')

	# sysdb
	p7 = subprocess.Popen('mysqldump --defaults-extra-file=my.cnf sysdb < '+sysdb, shell=True)
	p7.wait()
	print('Succesfully dump sysdb')

else:
	print('Error: Folder '+todel_path+' not found')