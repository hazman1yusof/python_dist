from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
#import reportlab.rl_settings
import win32print,win32api
import ConfigParser

width=80 * 2.8346456693
height=25 * 2.8346456693

c = canvas.Canvas("sticker.pdf", pagesize=(width,height),bottomup = 1)
config = ConfigParser.RawConfigParser()
config.read('sticker.ini')
configlist=config.sections()

def output(c,section):
    c.translate(mm,mm)
    yline=25 * 1.8346456693
    xline=10
    c.setFont("Helvetica-Bold",8)
    for (key, val) in config.items(section):
        if(key == 'nama'):
            c.setFont("Helvetica-Bold",8)
            #if(len(val)>45):
            #    yline=yline+4
            #    c.drawString (xline, yline+8, val[:45])
            #    yline=yline-8
            #    val = val[45:]
        elif(key == 'mrn'):
            yline=yline-16
            c.setFont("Helvetica-Bold",8)
        elif(key == 'dob'):
            xline = 80
            c.setFont("Helvetica-Bold",8)
        elif(key == 'doa'):
            xline = 150
            c.setFont("Helvetica-Bold",8)
        elif(key == 'kp'):
            yline=yline-16
            c.setFont("Helvetica-Bold",8)
        elif(key == 'sex'):
            xline = 150
            c.setFont("Helvetica-Bold",8)
        elif(key == 'age'):
            xline = 85
            c.setFont("Helvetica-Bold",8)
        #elif(key == 'ward'):
            #yline=yline-16
            #c.setFont("Helvetica-Bold",8)

        c.drawString (xline, yline, val)
        xline=10

for section in configlist:
    output(c,section)
    c.showPage()

c.save()

GHOSTSCRIPT_PATH = "GHOSTSCRIPT\\bin\\gswin32.exe"
GSPRINT_PATH = "GSPRINT\\gsprint.exe"

currentprinter = win32print.GetDefaultPrinter()
win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "sticker.pdf"', '.', 0)  # lint:ok