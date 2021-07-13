from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import reportlab.rl_settings
import win32print,win32api
import ConfigParser

width=101.6 * 2.8346456693
height=50.8 * 2.8346456693

c = canvas.Canvas("label.pdf", pagesize=(width,height),bottomup = 1)
config = ConfigParser.RawConfigParser()
config.read('pharmacy.ini')
configlist=config.sections()

def output(c,section):
    c.translate(mm,mm)
    yline=85
    xline=40
    for (key, val) in config.items(section):
        if(key == 'mrn'):
            yline=yline-10
            c.setFont("Helvetica",8)
        elif(key == 'date'):
            c.setFont("Helvetica",8)
            xline=140
        elif(key == 'name'):
            yline=yline-10
            if(len(val)>47):
                c.drawString (xline, yline, val[:47])
                val = val[47:]
                yline=yline-10
        elif(key == 'description'):
            c.setFont("Helvetica-Bold",8)
            yline=yline-10
            if(len(val)>47):
                c.drawString (xline, yline, val[:47])
                val = val[47:]
                yline=yline-10
        elif(key == 'generic'):
            c.setFont("Helvetica",8)
            yline=yline-10
            if(len(val)>47):
                c.drawString (xline, yline, val[:47])
                val = val[47:]
                yline=yline-10
        elif(key == 'freq'):
            c.setFont("Helvetica",8)
            yline=yline-10
        elif(key == 'instruction'):
            c.setFont("Helvetica",8)
            yline=yline-10
            if(len(val)>47):
                c.drawString (xline, yline, val[:47])
                val = val[47:]
                yline=yline-10
        elif(key == 'addinstruction'):
            c.setFont("Helvetica-Bold",8)
            yline=yline-10
            if(len(val)>47):
                c.drawString (xline, yline, val[:47])
                val = val[47:]
                yline=yline-10
        elif(key == 'days'):
            c.setFont("Helvetica",8)
        elif(key == 'quantity'):
            c.setFont("Helvetica",8)
            xline=140
        else:
            c.setFont("Helvetica",8)
        c.drawString (xline, yline, val)
        xline=40

for section in configlist:
    output(c,section)
    c.showPage()

c.save()

GHOSTSCRIPT_PATH = "GHOSTSCRIPT\\bin\\gswin32.exe"
GSPRINT_PATH = "GSPRINT\\gsprint.exe"

currentprinter = win32print.GetDefaultPrinter()

win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "label.pdf"', '.', 0)  # lint:ok
