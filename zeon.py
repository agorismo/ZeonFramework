import os
import socket
import requests
import base64
import hashlib
import time
import subprocess

def design():
    os.system("clear")
    print("""
\033[1;94m  ________   _______ \033[1;94m  \033[37m ______    __   __ \033[37m 
\033[1;94m |       /  |   ____|\033[1;94m  \033[37m/  __  \  |  \ |  |\033[37m  \033[37mᶻᵉᵒⁿ ᶠʳᵃᵐᵉʷᵒʳᵏ\033[37m
\033[1;94m `---/  /   |  |__   \033[1;94m \033[37m|  |  |  | |   \|  |\033[37m  \033[1;94m⁻\033[1;94m \033[37mᶠᵃᵗᵉᵈ\033[37m 
\033[1;94m    /  /    |   __|  \033[1;94m \033[37m|  |  |  | |  . `  |\033[37m  \033[1;94m-\033[1;94m \033[37mᵃᵍ⁰ʳᶦˢᵐ\033[37m
\033[1;94m   /  /----.|  |____ \033[1;94m \033[37m|  `--'  | |  |\   |\033[37m 
\033[1;94m  /________||_______|\033[1;94m  \033[37m\______/  |__| \__|\033[37m  
""")


def crypto():
    design()
    print("""
\033[1;94m[1]\033[1;94m \033[37mBase64 Encode\033[37m
\033[1;94m[2]\033[1;94m \033[37mBase64 Decode\033[37m
\033[1;94m[3]\033[1;94m \033[37mMD5 Encode\033[37m
\033[1;94m[4]\033[1;94m \033[37mSHA-256 Encode\033[37m
    
    """)
    shellc = int(input(">> "))
    if shellc == 1:
        bs4ipt = str(input("Text >> "))
        print("""\033[1;94m[*]\033[1;94m \033[37mProcessing ...\033[37m""")
        time.sleep(3)
        enco64 = base64.b64encode(bs4ipt.encode()).decode('ISO-8859-1')
        enc = str(enco64)
        print("""\033[1;94m[*]\033[1;94m \033[37mResult: {resu}\033[37m""".format(resu=enc))


        time.sleep(4)
        print("""
>> Return for menu in 10 seconds ...""")
        time.sleep(5)
        main()
    if shellc == 2:
        bs4ipt2 = str(input("Hash >> "))
        print("""\033[1;94m[*]\033[1;94m \033[37mProcessing ...\033[37m""")
        time.sleep(3)
        deco64 = base64.b64decode(bs4ipt2).decode('ISO-8859-1')
        dec = str(deco64)
        print("""\033[1;94m[*]\033[1;94m \033[37mResult >> {deco}\033[37m""".format(deco=dec))
        time.sleep(4)

        print("""
>> Return for menu in 10 seconds ...""")
        time.sleep(5)
        main()

    if shellc == 3:
        md5ipt = str(input("Text >> "))
        md5dec = hashlib.md5(md5ipt.encode())
        print("""\033[1;94m[*]\033[1;94m \033[37mProcessing ...\033[37m""")
        time.sleep(3)
        rdm5 = md5dec.hexdigest()
        print("""\033[1;94m[*]\033[1;94m \033[37mResult >> {dec5}\033[37m""".format(dec5=rdm5))
        time.sleep(4)

        print("""
>> Return for menu in 10 seconds ...""")
        time.sleep(5)
        main()
    if shellc == 4:
        shaipt = str(input("Text >> "))
        shadec = hashlib.sha256(shaipt.encode())
        print("""\033[1;94m[*]\033[1;94m \033[37mProcessing ...\033[37m""")
        time.sleep(3)
        sha2 = shadec.hexdigest()
        print("""\033[1;94m[*]\033[1;94m \033[37mResult >> {sha25}\033[37m""".format(sha25=sha2))
        time.sleep(4)

        print("""
>> Return for menu in 10 seconds ...""")
        time.sleep(5)
        main()


def nmapOS():
    shellnm = str(input("\033[37mIP >> \033[37m"))
    print("""\033[1;94m[*]\033[1;94m \033[37mProcessing ...\033[37m""")
    time.sleep(3)
    print("""\033[1;94m[*]\033[1;94m \033[37mMode verbose on ...\033[37m""")
    time.sleep(3)
    ip = str(shellnm)
    cmd = os.system("nmap -A -Pn --script=vuln -v {i}".format(i=ip))
    time.sleep(3)
    print(cmd)

    time.sleep(2)
    print("""
>> Return for menu in 10 seconds ...""")
    time.sleep(5)
    main()

def scanport(st):

    ports = { 21: 'FTP',
              22: 'SSH',
              23: 'TELNET',
              25: 'SMTP',
              26: 'RSFTP',
              53: 'DOMAIN',
              80: 'HTTP',
              106: 'POP3PW',
              110: 'POP3',
              113: 'IDENT',
              139: 'NETBIOS-SSN',
              143: 'IMAP',
              256: 'FW1-SECUREREMOTE',
              443: 'HTTPS',
              465: 'SMTPS',
              554: 'RTSP',
              587: 'SMTP',
              993: 'IMAPS',
              995: 'POP3S',
              1720: 'H323Q931',
              1723: 'PPTP',
              2022: 'DOWN',
              2525: 'MS-V-WORLDS',
              3306: 'MYSQL',
              5222: 'XMPP-CLIENT',
              8080: 'HTTP-PROXY',
              9090: 'ZEUS-ADMIN',
              8443: 'HTTPS-ALT',
              9102: 'JETDIRECT'
}

    print("""\033[1;94m[*]\033[1;94m \033[37mProcessing ...\033[37m""")
    time.sleep(3)
    for p1 in ports:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        c = s.connect_ex((st,p1))
        svc = ports[p1]
        if c == 0:
            time.sleep(2)
            print("""
\033[1;94mPORT:\033[1;94m  \033[37m{s} - {s2}\033[37m
\033[1;94mSTATUS:\033[1;94m  \033[32mOPEN\033[32m
""".format(s=svc,s2=p1))
        else:
            time.sleep(2)
            print("""
\033[1;94mPORT:\033[1;94m \033[37m{s} - {s2}\033[37m
\033[1;94mSTATUS:\033[1;94m \033[31mCLOSED\033[31m
        """.format(s=svc,s2=p1))
    
    print("""
\033[37m>> Return for menu in 10 seconds ...\033[37m""")
    time.sleep(5)
    main()

def ipgeo(ip):
    print("""\033[1;94m[*]\033[1;94m \033[37mProcessing ...\033[37m""")
    time.sleep(3)
    webr = "http://api.hackertarget.com/geoip/?q="+ip
    getr = requests.get(webr)
    fresu = str(getr.text)
    if "error input" in fresu:
        print("""
     \033[1;94m[*]\033[1;94m \033[37mIP Invalid\033[37m  """)
    else:
        print(fresu)

    print("""
\033[37m>> Return for menu in 10 seconds ...\033[37m""")
    time.sleep(5)
    main()


def ops():
    print("""

\033[1;94m[1]\033[1;94m \033[37mCryptography\033[37m
\033[1;94m[2]\033[1;94m \033[37mOS Scan with Nmap\033[37m
\033[1;94m[3]\033[1;94m \033[37mPorts\033[37m
\033[1;94m[4]\033[1;94m \033[37mIP Geo\033[37m

\033[1;94m[0]\033[1;94m \033[37mExit\033[37m
    """
    )
    shell = int(input(">> "))
    if shell == 1:
        crypto()
    if shell == 2:
        nmapOS()
    if shell == 3:
        shellt = str(input("IP >> "))
        scanport(shellt)
    if shell == 4:
        shelli = str(input("IP >> "))
        ipgeo(shelli)
    if shell == 0:
        design()
        print("""\033[1;94m[*]\033[1;94m\033[1;37m Ideologies separate us, dreams and grief unite us. \033[1;37m\033[1;94m[*]\033[1;94m
        """)
        time.sleep(5)
        exit(0)

def main():
    verif = str(subprocess.check_output("whoami",shell=True))
    if 'root' in verif:
        design()
        ops()
    else:
        design()
        print("""\033[37m> Run as root\033[37m\n""")
        os.system("exit")
        exit(0)
    
main()
