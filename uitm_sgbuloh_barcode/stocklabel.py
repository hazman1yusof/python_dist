# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from svglib.svglib import svg2rlg
import win32print,win32api
import ConfigParser
import barcode
barcode.PROVIDED_BARCODES
[u'code39', u'code128', u'ean', u'ean13', u'ean8', u'gs1', u'gtin',u'isbn', u'isbn10', u'isbn13', u'issn', u'jan', u'pzn', u'upc', u'upca']


#width2=58mm
#height2=28mm
#label gap=2mm
width=164.409
height=79.3701

c = canvas.Canvas("label.pdf", pagesize=(width,height),bottomup = 1)
config = ConfigParser.RawConfigParser()
config.read('barcode.ini')
configlist=config.sections()

def output(c,section):
    c.translate(mm,mm)
    yline=60
    xline=10
    for (key, val) in config.items(section):
        if(key == 'title'):
            c.setFont("Helvetica",5)
            c.drawCentredString (width/2, yline, val)
            yline=yline-6
        elif(key == 'barcode'):

            barcode.Code39(val,add_checksum = True).save("barcode")

            drawing = svg2rlg("barcode.svg")
            drawing.scale(1,0.5)
            drawing.drawOn(c,28,24)
            yline=yline-38

        elif(key == 'DESCRIPTION'):
            c.setFont("Helvetica",5)
            c.drawCentredString (50, yline, val)
        else:
            c.setFont("Helvetica",5)
            c.drawCentredString (width/2, yline, val)
            yline=yline-6

for section in configlist:
    output(c,section)
    c.showPage()

c.save()

GHOSTSCRIPT_PATH = "GHOSTSCRIPT\\bin\\gswin32.exe"
GSPRINT_PATH = "GSPRINT\\gsprint.exe"

currentprinter = win32print.GetDefaultPrinter()
win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "label.pdf"', '.', 0)  # lint:ok
