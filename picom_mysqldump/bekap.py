import subprocess

subprocess.Popen('mysqldump --defaults-extra-file=my.cnf > hisdb.sql', shell=True)