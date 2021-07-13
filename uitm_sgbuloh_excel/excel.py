# -*- coding: utf-8 -*-
import xlsxwriter
import subprocess
import ConfigParser
import os.path

def control_column_length(rows,arroflen,worksheet):

    columnlen_c = 0
    for columnlen in arroflen:
        worksheet.set_column(columnlen_c,columnlen_c, columnlen+3)
        columnlen_c += 1


db_conf = ConfigParser.RawConfigParser()
db_conf.read('path.ini')

exelpath = db_conf.get('DATA1','exelpath')

if(os.path.exists(db_conf.get('DATA1','wpspath1'))):
    wpspath=db_conf.get('DATA1','wpspath1')
elif(os.path.exists(db_conf.get('DATA1','wpspath2'))):
    wpspath=db_conf.get('DATA1','wpspath2')
elif(os.path.exists(db_conf.get('DATA1','wpspath3'))):
    wpspath=db_conf.get('DATA1','wpspath3')
elif(os.path.exists(db_conf.get('DATA1','wpspath4'))):
    wpspath=db_conf.get('DATA1','wpspath4')
elif(os.path.exists(db_conf.get('DATA1','wpspath5'))):
    wpspath=db_conf.get('DATA1','wpspath5')

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('document.xlsx')

f = open("document.txt", "r")
rows = f.readlines()

worksheet_first_name = rows[0].rstrip("\n").split("|")[1]
# arroflen = [1]
rows_count = 0
# Strips the newline character
for row in rows:

    columns = row.rstrip("\n").split("|")
    columns_count = 0

    if columns[0] == '{ws}':
        worksheet_name = columns[1]

        if worksheet_first_name != worksheet_name:
            rows_count = 0
            # control_column_length(rows,arroflen,worksheet)

        worksheet = workbook.add_worksheet(columns[1])

        rows_count += 1
        continue
    elif columns[0] == '{h}':
        format_line = workbook.add_format({'bold': True, 'text_wrap': True})

        # arrlen = len(columns) - 1
        # arroflen = [1]*arrlen

    elif columns[0] == '{cs}':
        worksheet.set_column(0,0,10)
        arroflen_ = columns[1:]
        columnlen_c = 0
        for columnlen in arroflen_:
            worksheet.set_column(columnlen_c,columnlen_c,int(columnlen))
            columnlen_c += 1
        continue
    elif columns[0] == '{b}':
        format_line = workbook.add_format({'bold': True, 'text_wrap': True})

    elif columns[0] == '{n}':
        format_line = workbook.add_format({'bold': False, 'text_wrap': True})

    elif columns[0] == '{s}':
        format_line = workbook.add_format({'bold': True, 'text_wrap': False})

        worksheet.write(rows_count, 0, columns[1], format_line)
        rows_count += 1
        continue

    for column in columns:
        if columns_count == 0:
            columns_count += 1
            continue

        # if len(column) > arroflen[columns_count-1]:
        #     arroflen[columns_count-1] = len(column)

        worksheet.write(rows_count, columns_count-1, column, format_line)
        columns_count += 1

    rows_count += 1


# control_column_length(rows,arroflen,worksheet)

workbook.close()

subprocess.call([wpspath, exelpath])