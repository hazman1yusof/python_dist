from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import reportlab.rl_settings
import win32print,win32api
import ConfigParser
import subprocess
import os

width=109 * 2.8346456693
height=59 * 2.8346456693

c = canvas.Canvas("label.pdf", pagesize=(width,height),bottomup = 1)
config = ConfigParser.RawConfigParser()
config.read('pharmacy.ini')
configlist=config.sections()
# c.line(xline, yline-5, xline+185+40, yline-5)

def output(c,section):
    c.translate(mm,mm)
    yline=104
    xline=20

    for (key, val) in config.items(section):

        xline=20
        c.setFont("Helvetica-Bold",7)

        if(key == 'name'):
            c.drawString (xline, yline, "NAME")
            xline = xline + 45

        elif(key == 'newic'):
            yline=yline-12
            c.drawString (xline, yline, "IC")
            xline = xline + 45

        elif(key == 'date'):
            xline=165
            c.drawString (xline, yline, "DATE")
            xline = xline + 28

        elif(key == 'mrn'):
            yline=yline-12
            c.drawString (xline, yline, "RN")
            xline = xline + 45

        elif(key == 'ward'):
            xline=165
            c.drawString (xline, yline, "WARD")
            xline = xline + 28

        elif(key == 'medicine'):
            yline=yline-12
            c.drawString (xline, yline, "MEDICINE")
            xline = xline + 45

        elif(key == 'take'):
            yline=yline-12
            c.drawString (xline, yline, "TAKE/APPLY")
            xline = xline + 45

        elif(key == 'quan'):
            xline=155
            c.drawString (xline, yline, "QUANTITY")
            xline = xline + 38

        elif(key == 'freq'):
            yline=yline-12
            c.drawString (xline, yline, "FREQUENCY")
            xline = xline + 45

        elif(key == 'days'):
            xline=155
            c.drawString (xline, yline, "DURATION")
            xline = xline + 38

        elif(key == 'instruction'):
            yline=yline-12
            c.drawString (xline, yline, "DIRECTION")
            xline = xline + 45

        elif(key == 'addinstruction'):
            yline=yline-12
            c.setFont("Helvetica",7)
            c.drawString (xline, yline, val)
            continue

        c.setFont("Helvetica-Bold",7)
        c.drawString (xline, yline, ":")

        xline = xline + 3
        c.setFont("Helvetica",7)
        c.drawString (xline, yline, val)

for section in configlist:
    output(c,section)
    c.showPage()

c.save()


bat_file = "print.bat"
bat_file_path = os.path.join(os.path.abspath(bat_file))


p = subprocess.Popen(bat_file_path, shell=True, stdout = subprocess.PIPE)

# GHOSTSCRIPT_PATH = "GHOSTSCRIPT\\bin\\gswin32.exe"
# GSPRINT_PATH = "GSPRINT\\gsprint.exe"

# currentprinter = win32print.GetDefaultPrinter()

# win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "label.pdf"', '.', 0)  # lint:ok
