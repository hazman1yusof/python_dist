from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import reportlab.rl_settings
import win32print,win32api
import configparser

import subprocess
import os

width=101.6 * 2.8346456693
height=48.26 * 2.8346456693

c = canvas.Canvas("label.pdf", pagesize=(width,height),bottomup = 1)
config = configparser.RawConfigParser()
config.read('pharmacy.ini')
configlist=config.sections()

def output(c,section):
    c.translate(mm,mm)
    yline=85
    xline=20
    for (key, val) in config.items(section):
        if(key == 'mrn'):
            yline=yline-10
            c.setFont("Helvetica",8)
        elif(key == 'date'):
            c.setFont("Helvetica-Bold",8)
            xline=190
        elif(key == 'name'):
            c.setFont("Helvetica-Bold",8)
            yline=yline-10
            if(len(val)>80):
                c.drawString (xline, yline, val[:80])
                val = val[80:]
                yline=yline-10
        elif(key == 'description'):
            c.setFont("Helvetica-Bold",8)
            yline=yline-10
            if(len(val)>80):
                c.drawString (xline, yline, val[:80])
                val = val[80:]
                yline=yline-10
        elif(key == 'generic'):
            c.setFont("Helvetica",8)
            yline=yline-10
            if(len(val)>80):
                c.drawString (xline, yline, val[:80])
                val = val[80:]
                yline=yline-10
        elif(key == 'freq'):
            c.setFont("Helvetica",8)
            yline=yline-10
        elif(key == 'instruction'):
            c.setFont("Helvetica",8)
            yline=yline-10
            if(len(val)>80):
                c.drawString (xline, yline, val[:80])
                val = val[80:]
                yline=yline-10
        elif(key == 'addinstruction'):
            c.setFont("Helvetica-Bold",8)
            yline=yline-10
            if(len(val)>80):
                c.drawString (xline, yline, val[:80])
                val = val[80:]
                yline=yline-10
        elif(key == 'days'):
            c.setFont("Helvetica",8)
            xline=190
        elif(key == 'quantity'):
            c.setFont("Helvetica",8)
            xline=190
        else:
            c.setFont("Helvetica",8)
        c.drawString (xline, yline, val)
        xline=20

for section in configlist:
    output(c,section)
    c.showPage()

c.save()

# GHOSTSCRIPT_PATH = "GHOSTSCRIPT\\bin\\gswin32.exe"
# GSPRINT_PATH = "GSPRINT\\gsprint.exe"

# currentprinter = win32print.GetDefaultPrinter()

# win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "label.pdf"', '.', 0)  # lint:ok

pdf_file = "label.bat"
pdf_file_path = os.path.join(os.path.abspath(pdf_file))

p = subprocess.Popen(pdf_file_path, shell=True, stdout = subprocess.PIPE)