from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import reportlab.rl_settings
import win32print,win32api
import ConfigParser

width=90 * 2.8346456693
height=57 * 2.8346456693

c = canvas.Canvas("label.pdf", pagesize=(width,height),bottomup = 1)
config = ConfigParser.RawConfigParser()
config.read('pharmacy.ini')
configlist=config.sections()

def output(c,section):
    c.translate(mm,mm)
    yline=90
    xline=0
    for (key, val) in config.items(section):
        if(key == 'name'):
            if(len(val)>36):
                c.drawString (xline, yline, val[:36])
                val = val[36:]
                yline=yline-10
        elif(key == 'date'):
            c.setFont("Helvetica",8)
            c.line(xline, yline-5, xline+185+40, yline-5)
            xline=185
            yline=yline-15
        elif(key == 'description'):
            c.setFont("Helvetica-Bold",8)
            if(len(val)>41):
                c.drawString (xline, yline, val[:41])
                val = val[41:]
                yline=yline-10
        elif(key == 'mrn'):
            xline=172
            c.setFont("Helvetica",8)
        elif(key == 'generic'):
            c.setFont("Helvetica",8)
            yline=yline-10
            if(len(val)>41):
                c.drawString (xline, yline, val[:41])
                val = val[41:]
                yline=yline-10
        elif(key == 'freq'):
            c.setFont("Helvetica",8)
            yline=yline-13
        elif(key == 'instruction'):
            c.setFont("Helvetica",8)
            yline=yline-10
            if(len(val)>41):
                c.drawString (xline, yline, val[:41])
                val = val[41:]
                yline=yline-10
        elif(key == 'addinstruction'):
            c.setFont("Helvetica-Bold",8)
            yline=yline-13
            if(len(val)>56):
                c.drawString (xline, yline, val[:56])
                val = val[56:]
                yline=yline-10
        elif(key == 'days'):
            c.setFont("Helvetica",8)
            xline=185
        elif(key == 'quantity'):
            c.setFont("Helvetica",8)
            xline=185
        elif(key == 'newic'):
            yline=yline-13
            c.setFont("Helvetica",8)
        elif(key == 'bed'):
            c.setFont("Helvetica",8)
            xline=145
        else:
            c.setFont("Helvetica",8)
        c.drawString (xline, yline, val)
        xline=0

for section in configlist:
    output(c,section)
    c.showPage()

c.save()

GHOSTSCRIPT_PATH = "GHOSTSCRIPT\\bin\\gswin32.exe"
GSPRINT_PATH = "GSPRINT\\gsprint.exe"

currentprinter = win32print.GetDefaultPrinter()

win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "label.pdf"', '.', 0)  # lint:ok
