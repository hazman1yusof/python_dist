import configparser
import mysql.connector
import datetime

db_conf = ConfigParser.RawConfigParser()
db_conf.read('db.ini')
db_conf_sect = db_conf.sections()

for (key, val) in db_conf.items('DATA1'):
    if(key == 'host'):
        host=val
    elif(key == 'user'):
        user=val
    elif(key == 'passwd'):
        passwd=val
    elif(key == 'database'):
        database=val
    elif(key == 'compcode'):
        compcode=val

mydb = mysql.connector.connect(
    host=host,
    user=user,
    passwd=passwd,
    database=database
)

def format_date(date):
    if date is None:
        return ''
    elif date == '0000-00-00':
        return ''
    else:
        return datetime.datetime.strptime(str(date), '%Y-%m-%d').strftime('%d/%m/%Y')

def format_yesno(strg):
    if strg is None:
        return 'no'
    else:
        return 'yes'

patmast_arr = []
epispay_arr = []
debtorm_arr = []

mycursor = mydb.cursor(dictionary=True,buffered=True)

query = ("SELECT * FROM episode "
         "WHERE compcode = %s AND episactive = %s ")

mycursor.execute(query,(compcode, '1'))

row_count = mycursor.rowcount

if row_count != 0:
    myresult = mycursor.fetchall()

    for row in myresult:
        query = ("SELECT * FROM pat_mast "
             "WHERE compcode = %s AND mrn = %s ")

        mycursor.execute(query,(compcode, row['mrn']))

        patmast = mycursor.fetchone()
        if patmast != None:
            patmast_arr.append(patmast)

        query = ("SELECT * FROM epispayer "
             "WHERE compcode = %s AND mrn = %s AND episno = %s ")

        mycursor.execute(query,(compcode, row['mrn'], row['episno']))

        epispay = mycursor.fetchone()
        if epispay != None:
            epispay_arr.append(epispay)

for row_ in epispay_arr:
    query = ("SELECT * FROM debtor.debtormast "
         "WHERE compcode = %s AND debtorcode LIKE %s ")

    mycursor.execute(query,(compcode, '%'+row_['payercode']))

    debtorm = mycursor.fetchone()
    if debtorm != None:
        debtorm_arr.append(debtorm)


mycursor.close()
mydb.close()

if row_count != 0:
    # write episode
    f = open("episode.txt", "w")
    for row in myresult:
        f.write(str(row['compcode'] or '')+
        "|"+str(row['mrn'] or '0')+
        "|"+str(row['episno'] or '0')+
        "|"+str(row['admsrccode'] or '')+
        "|"+str(row['epistycode'] or '')+
        "|"+str(row['case_code'] or '')+
        "|"+str(row['ward'] or '')+
        "|"+str(row['bedtype'] or '')+
        "|"+str(row['room'] or '')+
        "|"+str(row['bed'] or '')+
        "|"+str(row['admdoctor'] or '')+
        "|"+str(row['attndoctor'] or '')+
        "|"+str(row['refdoctor'] or '')+
        "|"+str(row['prescribedays'] or '')+
        "|"+str(row['pay_type'] or '')+
        "|"+str(row['pyrmode'] or '')+
        "|"+str(row['climitauthid'] or '')+
        "|"+str(row['crnumber'] or '')+
        "|"+str(row['depositreq'] or '0.00')+
        "|"+str(row['deposit'] or '0.00')+
        "|"+str(row['pkgcode'] or '')+
        "|"+str(row['billtype'] or '')+
        "|"+str(row['remarks'] or '')+
        "|"+str(row['episstatus'] or '')+
        "|"+format_yesno(str(row['episactive']))+
        "|"+format_date(row['adddate'])+
        "|"+str(row['adduser'] or '')+
        "|"+format_date(row['reg_date'])+
        "|"+str(row['reg_time'] or '')+
        "|"+format_date(row['dischargedate'])+
        "|"+str(row['dischargeuser'] or '')+
        "|"+str(row['dischargetime'] or '')+
        "|"+str(row['dischargedest'] or '')+
        "|"+str(row['allocdoc'] or '0')+
        "|"+str(row['allocbed'] or '0')+
        "|"+str(row['allocnok'] or '0')+
        "|"+str(row['allocpayer'] or '0')+
        "|"+str(row['allocicd'] or '0')+
        "|"+format_date(row['lastupdate'])+
        "|"+str(row['lastuser'] or '')+
        "|"+str(row['lasttime'] or '')+
        "|"+str(row['procedure'] or '')+
        "|"+str(row['dischargediag'] or '')+
        "|"+str(row['lodgerno'] or '')+
        "|"+str(row['regdept'] or '')+
        "|"+str(row['diet1'] or '')+
        "|"+str(row['diet2'] or '')+
        "|"+str(row['diet3'] or '')+
        "|"+str(row['diet4'] or '')+
        "|"+str(row['diet5'] or '')+
        "|"+str(row['glauthid'] or '')+
        "|"+str(row['treatment'] or '')+
        "|"+str(row['diagcode'] or '')+
        "|"+str(row['complain'] or '')+
        "|"+str(row['diagfinal'] or '')+
        "|"+str(row['clinicalnote'] or '')+
        "|"+format_yesno(str(row['conversion']))+
        "|"+format_yesno(str(row['newcaseNP']))+
        "|"+format_yesno(str(row['followupNP']))+
        "|"+format_yesno(str(row['followupP']))+
        "|"+str(row['bed2'] or '')+
        "|"+str(row['bed3'] or '')+
        "|"+str(row['bed4'] or '')+
        "|"+str(row['bed5'] or '')+
        "|"+str(row['bed6'] or '')+
        "|"+str(row['bed7'] or '')+
        "|"+str(row['bed8'] or '')+
        "|"+str(row['bed9'] or '')+
        "|"+str(row['bed10'] or '')+
        "|"+format_yesno(str(row['newcaseP']))+
        "|"+str(row['diagprov'] or '')+
        "|"+str(row['visitcase'] or '')+
        "|"+format_yesno(str(row['EDDept']))+
        "|"+str('')+
        "|"+str(row['procode'] or '')+
        "|"+format_yesno(str(row['treatcode']))+
        "|"+str('no')+
        "|"+str('no')+
        "|"+str('no')+
        "|"+str('')+
        "|"+str('')+
        "|"+str('')+
        "|"+str('')+
        "|"+str('')+
        "|"+str('')+
        "|"+str('')+
        "|"+str('')+
        "|"+str('')+
        "|"+str('')+
        "|"+str('')+
        "|"+str('')+
        "|"+str('')+
        "|"+str('')+
        "|"+str('no')+
        "|"+str('no')+
        "|"+str('no')+
        "|"+str('no')+
        "|"+str('')+
        "|"+str('')+
        "|"+str('')+
        "|"+str('no')+
        "|"+str('no')+
        "|"+str('no')+
        "|"+format_date(row['lastarrivaldate'])
        )
        f.write("\n")

    f.close()

    # write patmast
    f = open("patmast.txt", "w")
    for row in patmast_arr:
        f.write(str(row['CompCode'] or '')+
        "|"+str(row['MRN'] or '0')+
        "|"+str(row['Episno'] or '0')+
        "|"+str(row['Name'] or '')+
        "|"+str(row['Call_Name'] or '')+
        "|"+str(row['addtype'] or '')+
        "|"+str(row['Address1'] or '')+
        "|"+str(row['Address2'] or '')+
        "|"+str(row['Address3'] or '')+
        "|"+str(row['Postcode'] or '0')+
        "|"+str(row['citycode'] or '')+
        "|"+str(row['AreaCode'] or '')+
        "|"+str(row['StateCode'] or '')+
        "|"+str(row['CountryCode'] or '')+
        "|"+str(row['telh'] or '')+
        "|"+str(row['telhp'] or '')+
        "|"+str(row['telo'] or '')+
        "|"+str(row['Tel_O_Ext'] or '')+
        "|"+str(row['ID_Type'] or '')+
        "|"+str(row['idnumber'] or '')+
        "|"+str(row['Newic'] or '')+
        "|"+str(row['Oldic'] or '')+
        "|"+str(row['icolor'] or '')+
        "|"+str(row['Sex'] or '')+
        "|"+format_date(row['DOB'])+
        "|"+str(row['Religion'] or '')+
        "|"+str(row['AllergyCode1'] or '')+
        "|"+str(row['AllergyCode2'] or '')+
        "|"+str(row['Century'] or '0')+
        "|"+str(row['Citizencode'] or '')+
        "|"+str(row['OccupCode'] or '')+
        "|"+str(row['Staffid'] or '')+
        "|"+str(row['MaritalCode'] or '')+
        "|"+str(row['LanguageCode'] or '')+
        "|"+str(row['TitleCode'] or '')+
        "|"+str(row['RaceCode'] or '')+
        "|"+str(row['bloodgrp'] or '')+
        "|"+str(row['Accum_chg'] or '0.00')+
        "|"+str(row['Accum_Paid'] or '0.00')+
        "|"+format_date(row['first_visit_date'])+
        "|"+format_date(row['Reg_Date'])+
        "|"+format_date(row['last_visit_date'])+
        "|"+str(row['last_episno'] or '')+
        "|"+format_yesno(str(row['PatStatus']))+
        "|"+format_yesno(str(row['Confidential']))+
        "|"+format_yesno(str(row['Active']))+
        "|"+str(row['FirstIpEpisNo'] or '0')+
        "|"+str(row['FirstOpEpisNo'] or '0')+
        "|"+str(row['AddUser'] or '')+
        "|"+format_date(row['AddDate'])+
        "|"+format_date(row['Lastupdate'])+
        "|"+str(row['LastUser'] or '')+
        "|"+str(row['OffAdd1'] or '')+
        "|"+str(row['OffAdd2'] or '')+
        "|"+str(row['OffAdd3'] or '')+
        "|"+str(row['OffPostcode'] or '')+
        "|"+format_yesno(str(row['MRFolder']))+
        "|"+str(row['MRLoc'] or '')+
        "|"+str(row['MRActive'] or '')+
        "|"+str(row['OldMrn'] or '')+
        "|"+str(row['NewMrn'] or '0')+
        "|"+str(row['Remarks'] or '')+
        "|"+str(row['RelateCode'] or '')+
        "|"+str(row['ChildNo'] or '')+
        "|"+str(row['CorpComp'] or '')+
        "|"+str(row['Email'] or '')+
        "|"+str(row['CurrentEpis'] or '')+
        "|"+str(row['NameSndx'] or '')+
        "|"+str(row['BirthPlace'] or '')+
        "|"+str(row['TngID'] or '')+
        "|"+str(row['PatientImage'] or '')+
        "|"+str(row['pAdd1'] or '')+
        "|"+str(row['pAdd2'] or '')+
        "|"+str(row['pAdd3'] or '')+
        "|"+str(row['pPostCode'] or '0')+
        "|"+str(row['DeptCode'] or '')+
        "|"+format_date(row['DeceasedDate'])+
        "|"+str(row['PatientCat'] or '')+
        "|"+str(row['PatType'] or '')
        )
        f.write("\n")

    f.close()

    # write epispayer
    f = open("epispayer.txt", "w")
    for row in epispay_arr:
        f.write(str(row['compcode'] or '')+
        "|"+str(row['mrn'] or '0')+
        "|"+str(row['episno'] or '0')+
        "|"+str(row['payercode'] or '')+
        "|"+str(row['lineno'] or '0')+
        "|"+str(row['epistycode'] or '')+
        "|"+str(row['pay_type'] or '')+
        "|"+str(row['pyrmode'] or '')+
        "|"+format_yesno(str(row['pyrcharge']))+
        "|"+format_yesno(str(row['pyrcrdtlmt']))+
        "|"+str(row['pyrlmtamt'] or '0.00')+
        "|"+str(row['totbal'] or '0.00')+
        "|"+format_yesno(str(row['allgroup']))+
        "|"+format_yesno(str(row['alldept']))+
        "|"+format_date(row['adddate'])+
        "|"+str(row['adduser'] or '')+
        "|"+format_date(row['lastupdate'])+
        "|"+str(row['lastuser'] or '')+
        "|"+str(row['billtype'] or '')+
        "|"+str(row['refno'] or '')+
        "|"+str(row['chgrate'] or '0.00')
        )
        f.write("\n")

    f.close()

    #write debtormast
    f = open("debtormast.txt", "w")
    for row in debtorm_arr:
        f.write(str(row['compcode'] or '')+
        "|"+str(row['debtortype'] or '')+
        "|"+str(row['debtorcode'] or '')+
        "|"+str(row['name'] or '').strip()+
        "|"+str(row['address1'] or '')+
        "|"+str(row['address2'] or '')+
        "|"+str(row['address3'] or '')+
        "|"+str(row['address4'] or '')+
        "|"+str(row['postcode'] or '0')+
        "|"+str(row['statecode'] or '')+
        "|"+str(row['countrycode'] or '')+
        "|"+str(row['contact'] or '')+
        "|"+str(row['position'] or '')+
        "|"+str(row['teloffice'] or '')+
        "|"+str(row['fax'] or '')+
        "|"+str(row['billtype'] or '')+
        "|"+str(row['billtypeop'] or '')+
        "|"+str(row['recstatus'] or '')+
        "|"+str(row['outamt'] or '0.00')+
        "|"+str(row['depamt'] or '0.00')+
        "|"+str(row['creditlimit'] or '0.00')+
        "|"+str(row['actdebccode'] or '')+
        "|"+str(row['actdebglacc'] or '')+
        "|"+str(row['depccode'] or '')+
        "|"+str(row['depglacc'] or '')+
        "|"+str(row['otherccode'] or '')+
        "|"+str(row['otheracct'] or '')+
        "|"+str('')+
        "|"+str('')+
        "|"+str(row['debtorgroup'] or '')+
        "|"+str(row['crgroup'] or '')+
        "|"+str(row['otheraddr1'] or '')+
        "|"+str(row['otheraddr2'] or '')+
        "|"+str(row['otheraddr3'] or '')+
        "|"+str(row['otheraddr4'] or '')+
        "|"+str(row['accno'] or '')+
        "|"+str(row['othertel'] or '')+
        "|"+str(row['requestgl'] or '')+
        "|"+str(row['creditterm'] or '0.00')+
        "|"+str(row['adduser'] or '')+
        "|"+format_date(row['adddate'])+
        "|"+str(row['coverageip'] or '0.00')+
        "|"+str(row['coverageop'] or '0.00')+
        "|"+str('0.00')+
        "|"+str('no')
        )
        f.write("\n")

    f.close()