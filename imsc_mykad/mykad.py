import win32com.client, datetime
myobj_hazman = win32com.client.Dispatch('mykadproweb.mykadproweb.jpn')
mystrRet_hazman = myobj_hazman.BeginJPN('Feitian SCR301 0')
open('mykad.txt', 'w').close()

if mystrRet_hazman == '0':
    mydata_hazman = myobj_hazman.getIDNum + '|'
    newdob = datetime.datetime.strptime(myobj_hazman.getBirthDate, '%Y-%m-%d').strftime('%d-%m-%Y')
    mydata_hazman += newdob + '|'
    mydata_hazman += myobj_hazman.getBirthPlace + '|'
    mydata_hazman += myobj_hazman.getGMPCName + '|'
    mydata_hazman += myobj_hazman.getOldIDNum + '|'
    mydata_hazman += myobj_hazman.getReligion + '|'
    mydata_hazman += myobj_hazman.getGender + '|'
    mydata_hazman += myobj_hazman.getRace + '|'
    mydata_hazman += myobj_hazman.getAddress1 + '|'
    mydata_hazman += myobj_hazman.getAddress2 + '|'
    mydata_hazman += myobj_hazman.getAddress3 + '|'
    mydata_hazman += myobj_hazman.getPostcode + '|'
    mydata_hazman += myobj_hazman.getCity + '|'
    mydata_hazman += myobj_hazman.getState + '|'
    # mydata_hazman += myobj_hazman.getPhotoBase64String + '|'
    myobj_hazman.getPhoto('myphotov1.jpg')
    print(mydata_hazman+myobj_hazman.getPhotoBase64String)
    with open('mykad.txt', 'r+') as (f):
        f.write(mydata_hazman)
else:
    with open('mykad.txt', 'r+') as (f):
        f.write(mystrRet_hazman)
        print(mystrRet_hazman)
myobj_hazman.EndJPN