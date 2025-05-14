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
    yline=100
    xline=0
    for (key, val) in config.items(section):
        if(key == 'mrn'):
            xline=180
            c.setFont("Helvetica",8)
            c.drawString (xline, yline, val)
        elif(key == 'name'):
            nameskip = 0
            if(len(val)>36):
                c.drawString (xline, yline, val[:36])
                val = val[36:]
                yline=yline-10
                nameskip = 1
            c.drawString (xline, yline, val)
        elif(key == 'date'):
            c.setFont("Helvetica",8)
            xline=180
            if(nameskip == 0):
                yline=yline-10
            c.drawString (xline, yline, val)

            c.line(0, yline-5, 250, yline-5)

        elif(key == 'description'):
            yline=yline-15
            c.setFont("Helvetica-Bold",8)
            if(len(val)>52):
                c.drawString (xline, yline, val[:52])
                val = val[52:]
                yline=yline-10
            c.drawString (xline, yline, val)

        elif(key == 'generic'):
            c.setFont("Helvetica",8)
            yline=yline-10
            if(len(val)>52):
                c.drawString (xline, yline, val[:52])
                val = val[52:]
                yline=yline-10
            c.drawString (xline, yline, val)

        elif(key == 'freq'):
            yline=yline-13
            c.setFont("Helvetica",8)
            c.drawString (xline, yline, val)
        elif(key == 'quantity'):
            c.setFont("Helvetica",8)
            xline=180
            c.drawString (xline, yline, val)

        elif(key == 'instruction'):
            c.setFont("Helvetica",8)
            yline=yline-10
            if(len(val)>36):
                c.drawString (xline, yline, val[:36])
                val = val[36:]
                yline=yline-10
            c.drawString (xline, yline, val)
        elif(key == 'unitprice'):
            c.setFont("Helvetica",8)
            xline=180
            c.drawString (xline, yline, val)

        elif(key == 'addinstruction'):
            c.setFont("Helvetica-Bold",8)
            yline=yline-13
            if(len(val)>36):
                c.drawString (xline, yline, val[:36])
                val = val[36:]
                yline=yline-10
            c.drawString (xline, yline, val)
        elif(key == 'totamt'):
            c.setFont("Helvetica",8)
            xline=180
            c.drawString (xline, yline, val)

        elif(key == 'newic'):
            yline=yline-10
            c.setFont("Helvetica",6)
            c.drawString (xline, yline, val)
        elif(key == 'bed'):
            xline=180
            c.setFont("Helvetica",6)
            c.drawString (xline, yline, val)
        # else:
        #     c.setFont("Helvetica",8)
        xline=0

for section in configlist:
    output(c,section)
    c.showPage()

c.save()

GHOSTSCRIPT_PATH = "GHOSTSCRIPT\\bin\\gswin32.exe"
GSPRINT_PATH = "GSPRINT\\gsprint.exe"

currentprinter = win32print.GetDefaultPrinter()

win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "label.pdf"', '.', 0)  # lint:ok
