import subprocess
from datetime import datetime, timedelta
import shutil
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
import os

datestr = datetime.today().strftime('%d%m%y')
todel_date = datetime.now() - timedelta(days=10)
todel_path = 'picombekap_'+todel_date.strftime('%d%m%y')
savepath = 'picombekap_'+datestr

if os.path.isfile(todel_path+'.zip'):
	print('Deleting old file: '+todel_path+'.zip')
	os.remove(todel_path+'.zip')


if os.path.isdir(todel_path):
	print('Deleting old folder: '+todel_path)
	shutil.rmtree(todel_path,True,None)

os.makedirs(savepath, exist_ok=True) 

debtor = '.\/'+savepath+'\debtor_'+datestr+'.sql'
eisdb = '.\/'+savepath+'\eisdb_'+datestr+'.sql'
finance = '.\/'+savepath+'\/finance_'+datestr+'.sql'
hisdb = '.\/'+savepath+'\hisdb_'+datestr+'.sql'
material = '.\/'+savepath+'\material_'+datestr+'.sql'
nursing = '.\/'+savepath+'\/nursing_'+datestr+'.sql'
sysdb = '.\/'+savepath+'\sysdb_'+datestr+'.sql'


# debtor
p1 = subprocess.Popen('mysqldump --defaults-extra-file=my.cnf debtor > '+debtor, shell=True)
p1.wait()
print('Succesfully dump debtor')

# eisdb
p2 = subprocess.Popen('mysqldump --defaults-extra-file=my.cnf eisdb > '+eisdb, shell=True)
p2.wait()
print('Succesfully dump eisdb')

# finance
p3 = subprocess.Popen('mysqldump --defaults-extra-file=my.cnf finance > '+finance, shell=True)
p3.wait()
print('Succesfully dump finance')

# hisdb
p4 = subprocess.Popen('mysqldump --defaults-extra-file=my.cnf hisdb > '+hisdb, shell=True)
p4.wait()
print('Succesfully dump hisdb')

# material
p5 = subprocess.Popen('mysqldump --defaults-extra-file=my.cnf material > '+material, shell=True)
p5.wait()
print('Succesfully dump material')

# nursing
p6 = subprocess.Popen('mysqldump --defaults-extra-file=my.cnf nursing > '+nursing, shell=True)
p6.wait()
print('Succesfully dump nursing')

# sysdb
p7 = subprocess.Popen('mysqldump --defaults-extra-file=my.cnf sysdb > '+sysdb, shell=True)
p7.wait()
print('Succesfully dump sysdb')

exit_codes = [p.wait() for p in (p1, p2, p3, p4, p5, p6, p7)]
print(' ')
print('dump db to folder : '+savepath)

shutil.make_archive(savepath, 'zip', savepath)
print(' ')
print('make zip file for all DB backup at : '+savepath+'.zip')

# print(' ')
# print('Trying to connect to google Drive')
# gauth = GoogleAuth()           

# # Try to load saved client credentials
# gauth.LoadCredentialsFile("mycreds.txt")
# if gauth.credentials is None:
#     # Authenticate if they're not there
#     gauth.LocalWebserverAuth()
# elif gauth.access_token_expired:
#     # Refresh them if expired
#     gauth.Refresh()
# else:
#     # Initialize the saved creds
#     gauth.Authorize()
# gauth.SaveCredentialsFile("mycreds.txt")
# print('Succesfully connect to google Drive')

# drive = GoogleDrive(gauth)

# print(' ')
# print('Upload dumpfile: '+savepath+'.zip to google Drive')
# textfile = drive.CreateFile()
# textfile.SetContentFile(savepath+'.zip')
# textfile.Upload()
# print('Upload success')

# file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

# print('dump file stored in Google Drive:')
# for file in file_list:
# 	print(" - "+file['title'])
# 	if file['title'] == todel_path+'.zip':
# 		print('  - Delete old file: '+todel_path+'.zip from google Drive')
# 		drive.CreateFile({'id': file['id']}).Trash()

# print(' ')
# print('Finish')