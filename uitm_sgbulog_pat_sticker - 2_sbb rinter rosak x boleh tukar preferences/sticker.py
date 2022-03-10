from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from svglib.svglib import svg2rlg
import win32print,win32api
import ConfigParser
import barcode
import subprocess
import os


barcode.PROVIDED_BARCODES
[u'code39', u'code128', u'ean', u'ean13', u'ean8', u'gs1', u'gtin',u'isbn', u'isbn10', u'isbn13', u'issn', u'jan', u'pzn', u'upc', u'upca']

width=65 * 2.8346456693
height=25 * 2.8346456693

c = canvas.Canvas("sticker.pdf", pagesize=(width,height),bottomup = 1)
config = ConfigParser.RawConfigParser()
config.read('sticker.ini')
configlist=config.sections()

def output(c,section):
    c.translate(mm,mm)
    yline=31 * 1.8346456693
    xline=40
    for (key, val) in config.items(section):

        if(key == 'title'):
            xline = 52

        elif(key == 'mrn'):
            barcode.Code39(val,add_checksum = False).save("barcode")

            drawing = svg2rlg("barcode.svg")
            drawing.scale(1,0.4)
            drawing.drawOn(c,55,28)
            continue

        elif(key == 'ic'):
            xline = 40
            yline=yline-40

        elif(key == 'age'):
            xline = 105

        elif(key == 'sex'):
            xline = 125

        elif(key == 'race'):
            xline = 140

        elif(key == 'name'):
            yline=yline-8
            xline=40
            if(len(val)>40):
               c.drawString (xline, yline, val[:40])
               val = val[40:]
               yline=yline-8

        else: continue

        c.setFont("Helvetica-Bold",6)
        c.drawString (xline, yline, val)

for section in configlist:
    output(c,section)
    c.showPage()

c.save()

pdf_file = "sticker.bat"
pdf_file_path = os.path.join(os.path.abspath(pdf_file))


p = subprocess.Popen(pdf_file_path, shell=True, stdout = subprocess.PIPE)