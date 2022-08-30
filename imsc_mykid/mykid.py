import win32com.client, datetime
obj = win32com.client.Dispatch('mykidproweb.mykidproweb.jpn')
strRet = obj.BeginJPN('Feitian SCR301 0')
open('mykid.txt', 'w').close()
if strRet == '0':
    data = obj.getIDNum().rstrip('\x00') + '|'
    newdob = datetime.datetime.strptime(obj.getBirthDate(), '%Y-%m-%d').strftime('%d-%m-%Y')
    data += newdob + '|'
    data += obj.getBirthPlace() + '|'
    data += obj.getGMPCName() + '|'
    data += obj.getReligion() + '|'
    data += obj.getGender() + '|'
    data += obj.getFatherRace() + '|'
    data += obj.getAddress1() + '|'
    data += obj.getAddress2() + '|'
    data += obj.getAddress3() + '|'
    data += obj.getPostcode() + '|'
    data += obj.getCity() + '|'
    data += obj.getState() + '|'
    print(data.strip())
    with open('mykid.txt', 'r+') as (f):
        f.write(data)
else:
    with open('mykid.txt', 'r+') as (f):
        f.write(strRet)
        print(strRet)
obj.EndJPN()