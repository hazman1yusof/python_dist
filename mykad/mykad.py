import win32com.client, datetime
obj = win32com.client.Dispatch('mykadproweb.mykadproweb.jpn')
strRet = obj.BeginJPN('Feitian SCR301 0')
open('mykad.txt', 'w').close()
if strRet == '0':
    data = obj.getIDNum() + '|'
    newdob = datetime.datetime.strptime(obj.getBirthDate(), '%Y-%m-%d').strftime('%d-%m-%Y')
    data += newdob + '|'
    data += obj.getBirthPlace() + '|'
    data += obj.getGMPCName() + '|'
    data += obj.getOldIDNum() + '|'
    data += obj.getReligion() + '|'
    data += obj.getGender() + '|'
    data += obj.getRace() + '|'
    data += obj.getAddress1() + '|'
    data += obj.getAddress2() + '|'
    data += obj.getAddress3() + '|'
    data += obj.getPostcode() + '|'
    data += obj.getCity() + '|'
    data += obj.getState() + '|'
    obj.getPhoto('myphotov1.jpg')
    print data
    with open('mykad.txt', 'r+') as (f):
        f.write(data)
else:
    with open('mykad.txt', 'r+') as (f):
        f.write(strRet)
        print strRet
obj.EndJPN()