# -*- coding:utf8 -*-

# Supports python & python3
# Name   : PyObfuscate - Simple Python Code Obfuscator
# Author : SaiMun-cyber-403
# Date   : Sun Jul 19 00:19:27 2022

# Import Modules
import os
import sys
import zlib
import time
import base64
import marshal

if sys.version_info[0] == 2:
    _input = "raw_input('%s')"
elif sys.version_info[0] == 3:
    _input = "input('%s')"
else:
    sys.exit("\n Your Python Version is not Supported!")

logo = """
# Add your logo here
"""

# Encoding
zlb = lambda in_: zlib.compress(in_)
b64 = lambda in_: base64.b64encode(in_)
mar = lambda in_: marshal.dumps(compile(in_, '<x>', 'exec'))
note = "# \x54\x45\x41\x4d\x20\x44\x43\x43\x53\n"

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)

def menu(): # Program Menu
    jalan("\x20\x5B\x30\x31\x5D\x20\x45\x6E\x63\x6F\x64\x65\x20\x54\x45\x41\x4D\x20\x44\x43\x43\x53\x20\x53\x59\x53\x20\x0A")

class FileSize:  # Gets the File Size
    def datas(self, z):
        for x in ['Byte', 'KB', 'MB', 'GB']:
            if z < 1024.0:
                return "%3.1f %s" % (z, x)
            z /= 1024.0

    def __init__(self, path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            print(" [-] Encoded File Size : %s\n" % self.datas(dts))

def Encode(data, output):
    loop = int(eval(_input % " [-] Encode Count : "))
    print(' [-] Please Wait Encoding Is Starting ')

    xx = "b64(zlb(mar(data.encode('utf8'))))[::-1]"
    heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"

    for x in range(loop):
        try:
            data = "exec((_)(%s))" % repr(eval(xx))
        except TypeError as s:
            sys.exit(" TypeError : " + str(s))
    
    # Add more main variables with fake obfuscation code
    main = "exec(__import__('os').system('ls'))"  # Fake obfuscation code
    encode_func = lambda x: x + 1  # Fake obfuscation code
    data_list = [x**2 for x in range(10)]  # Fake obfuscation code

    result = 0
    for num in data:
        result += ord(num)

    # Hiding obfuscation code under a main variable
    hidden_code = "data = " + repr(data) + "; " + heading + "exec(data)"

    with open(output, 'w') as f:
        f.write(note + hidden_code + "\n")
        f.write("main = " + repr(main) + "\n")
        f.write("encode = lambda x: x + 1\n")
        f.write("data_list = " + repr(data_list) + "\n")
        f.write("result = " + repr(result) + "\n")
        f.close()

# Main Menu
def MainMenu():
    try:
        os.system('clear') # os.system('cls')
        print(logo)
        menu()
        try:
            option = int(eval(_input % " [-] Option : "))
        except ValueError:
            sys.exit("\n Invalid Option !")
        
        if option == 5:
            os.system('clear') # os.system('cls')
            print(logo)
        else:
            sys.exit('\n Invalid Option !')

        try:
            file = eval(_input % " [-] File Name : ")
            data = open(file).read()
        except IOError:
            sys.exit("\n File Not Found!")
        
        output = file.lower().replace('.py', '') + '_enc.py'
        Encode(data, output)
        print("\n [-] Successfully Encrypted %s" % file)
        print(" [-] Saved as %s" % output)
        FileSize(output)
    except KeyboardInterrupt:
        time.sleep(1)
        sys.exit()

if __name__ == "__main__":
    MainMenu()
