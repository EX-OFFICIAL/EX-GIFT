#make by Samir
#Full Credit By Samir
import random,string,time,re,sys,os
from concurrent.futures import ThreadPoolExecutor as tdp
try:
    import requests as r
    from bs4 import BeautifulSoup as bs
except:
    os.system("pip install bs4 requests")
    os.system('pkg install espeak')
    os.system("clear")
def clear():
	os.system('clear')
	print(sa)
def logo():
	print(sa)
def linex():
	print('\33[1;32m----------------------------------------------')
import getpass

attemps = 0

while attemps < 12345677901:
    username = input('Enter username: ')
    password = input('Enter password: ')

    if username == 'SAMIR' and password == 'CYBER-143':
        print('You have successfully logged in.')
        break
    else:
        print('\033[1;35mINCORRECT THIS TOOLS IS FREE BUT YOU NEED USER & PASS')
        attemps += 1
        continue
os.system('clear')
os.system('xdg-open https://youtube.com/@samircyber143')
os.system('espeak -a 300 "WELCOME TO SAMIR AUTO DUMP TOOLS"')
sa="""
 \033[1;33m ######    \033[1;91m ###   \033[1;32m ##     ##\033[1;34m ####\x1b[1;95m ########
\033[1;33m##    ##  \033[1;91m ## ##  \033[1;32m ###   ### \033[1;34m ## \x1b[1;95m ##     ##
\033[1;33m##       \033[1;91m ##   ## \033[1;32m #### #### \033[1;34m ## \x1b[1;95m ##     ##
\033[1;33m ###### \033[1;91m ##     ##\033[1;32m ## ### ## \033[1;34m ## \x1b[1;95m ########
\033[1;33m      ##\033[1;91m #########\033[1;32m ##     ## \033[1;34m ## \x1b[1;95m ##   ##
\033[1;33m##    ##\033[1;91m ##     ##\033[1;32m ##     ## \033[1;34m ## \x1b[1;95m ##    ##
\033[1;33m ###### \033[1;91m ##     ##\033[1;32m ##     ##\033[1;34m #### \x1b[1;95m##     ##


\x1b[1;96m┏─══─━══─══━─══─| ✠ |─══━─══─══━─══─┓
\x1b[38;5;46m┃AUTHOR    ; SADMAN SAMIR SNIGDHO   ┃
\x1b[1;93m┃WHATSAPP  ; +8801871778635         ┃
\x1b[1;95m┃FACEBOOK  ; SNIGDHO AFRIDI         ┃
\x1b[1;91m┃GITHUB    ; SAMIR-CYBER-143        ┃
\x1b[1;96m┗─══─━════─━─══─| ✠ |─══━─══─══━─══─┛"""
uids=[]
n=0
c=0
  
clear()
#file=input("ENTER ")
try:
    open(file,"r").read()
except:
    file="/sdcard/SAMIR-AUTO-DUMP.txt"

def s(code):
    ln=15-len(code)
    lim=int("9"*(ln))+1
    for i in range(lim):
        uids.append(code+str(i).zfill(ln))

def gen(code,tt):
    clear()
    print('[1] START FOR AUTO DUMP ..')
    linex()
    op=int(input("""select :  """))
    clear()
    print(' process his been started ...')
    print(' Use CTRL+z for stop')
    linex()
    if op==2:
        s(code)
    else:
        for i in range(tt):
            uids.append(code+''.join(random.choice(string.digits) for _ in range(
        15-len(code)
        )))
        
def geno(code,l,tt):
    for i in range(tt):
        uids.append(code+''.join(random.choice(string.digits) for _ in range(
        l-len(code)
        )))


uao=['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101','Mozilla/5.0 (Linux; Android 8.1.0; vivo 1812 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.9.0.1','Dalvik/2.1.0 (Linux; U; Android 5.1; Lenovo P1ma40 Build/LMY47D)',
'Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G7102 Build/KOT49H)',
'Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G920K Build/NRD90M)']

def inputs():
    os.system("clear")
    os.system('espeak -a 300 "ENTER YOUR DUMP LIMIT"')
    print(sa)
    print(' \nENTER YOUR DUMP LIMIT')
    print(' \nExample : 10001 ,100089,100090**etc')
    linex()
    code=input("SELECT YOUR LIMIT : ")
    clear()
    os.system('espeak -a 300 "ENTER YOUR COUNT LIMIT"')
    print('\nENTER YOUR COUNT LIMIT')
    print(' \nExample : 10000,100000,300000,3000484, etc')
    linex()
    tt=int(input("Total ids :"))
    l=0
    if len(code)<4:
        l=int(input("Uid length: "))
    return code,tt,l
    
    

def getname(uid):
    global n,c
    ua=random.choice(uao)
    hd={'authority':'m.facebook.com',

           'method': 'GET',
            'user-agent':ua
            
        
            
            }
    url="https://m.facebook.com/profile.php?id="+uid
    pi=r.get(url,headers=hd)
    bp=bs(pi.content,"html.parser")
    name=bp.find("title").text.split("|")[0].strip()
    if "Content not found" not in name and "Log in to Facebook" not in name:
        n+=1
        
        
        print(f"\033[1;34m[SAMIR-AUTO-DUMP-SUCCESFULL]\033[1;32m{uid}")
        open(file,"a").write(uid+" | "+name+"\n")
    #else:
        print(f"\033[1;34m[SAMIR-AUTO-DUMP-SUCCESFULL]\033[1;32m{uid}")
    
    c+=1
    print(f'[Couting : %s ]'%(n),end="\r")


def run():
    with tdp(max_workers=30) as t:
        for uid in uids:
            t.submit(getname,uid)

while True:
    code,tt,l=inputs()
    if len(code)>=4:
        gen(code,tt)
    else:
        geno(code,l,tt)
    
    run()
    print("DUMP IDS ARE SAVE: "+file)
    rr=input("DUMP AGAIN? [Y or N]")
    if rr in ["Y","y"]:
        code,tt,l=inputs()
        n=0
        c=0
        uids=[]
        gen(code,tt)
        run()
    else:
        break
