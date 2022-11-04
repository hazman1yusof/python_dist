import subprocess

subprocess.Popen('mysqldump -h localhost -P 3306 -u -root appdb > appdb.sql', shell=True)
