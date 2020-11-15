#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# Author D4RK5H4D0W5	Maklum kalo berantakan ster
# Big Thanks for Teguh Aprianto about the Google CSE Key
G = '\033[0;32m'; C = '\033[0;36m'; W = '\033[0;37m'; R = '\033[0;31m'; Y='\033[0;33m'
import requests as r,re,random,sys,os
def logo():
	os.system('cls' if os.name == 'nt' else 'clear')
	print '''%s   _____                 ________                __    \n  /  _  \_______________ \______ \   ___________|  | __ \n /  /_\  \_  __ \___   /  |    |  \ /  _ \_  __ \  |/ / \n/    |    \  | \//    /   |    `   (  <_> )  | \/    <  \n\____|__  /__|  /_____ \ /_______  /\____/|__|  |__|_ \ \n        \/   %scoded%s    \/   %sby%s    \/    %sdarkshadows%s   \/ \n'''%(C,W,C,W,C,W,C)
def main():
	try:
		logo()
		print '   %s[%s1%s] Single\n   %s[%s2%s] Mass'%(W,G,W,W,G,W)
		chc=raw_input('\n%s[%s?%s] Choice : '%(W,R,W))
		if chc == '1':logo();dork=raw_input('%s[%s?%s] Input dork : '%(W,G,W));print;dorker(dork);filter()
		elif chc == '2':
			logo()
			file=raw_input('%s[%s?%s] Input file : '%(W,G,W))
			for dork in open(file).read().splitlines():
				print '\n%s[%s!%s] %sDorking %s%s\n'%(W,Y,W,Y,dork,W)
				dorker(dork)
			filter()
		else:exit('    Bye goblok')
	except r.exceptions.ConnectionError:exit('%s[%s!%s] Check internet'%(W,R,W))
	except IndexError:exit('\n%s[%s!%s] Use : python2 %s dork.txt'%(W,R,W,sys.argv[0]))
	except IOError:exit('%s[%s×%s] File does not exist'%(W,R,W))
	except KeyboardInterrupt:exit('\n%s[%s!%s] Exit'%(W,R,W))
def dorker(search):
	page=0
	while True:
		page+=10
		get_token=r.get('https://cse.google.com/cse.js?cx=partner-pub-2698861478625135:3033704849',headers={'Referer': 'https://cse.google.com/cse?cx=partner-pub-2698861478625135:3033704849','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.'+str(random.randint(0000,3333))+'.100 Safari/537.36'}).text
		cse_token=re.findall(r'\"cse_token\": \"(.*?)\"',get_token)
		ngedork=r.get('https://cse.google.com/cse/element/v1?num=10&hl=en&cx=partner-pub-2698861478625135:3033704849&safe=off&cse_tok=%s&start=%s&q=%s&callback=x'%(cse_token[0],page,search),headers={'Referer': 'https://cse.google.com/cse?cx=partner-pub-2698861478625135:3033704849','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.'+str(random.randint(0000,3333))+'.100 Safari/537.36'}).text
		results=re.findall(r'\"unescapedUrl\": \"(.*?)\"',ngedork)
		if results==[]:break
		for url in results:
			print url;open('.dork','a+').write(url+'\n')
def filter():
	print '\n%s[%s*%s] Result filter menu\n\n    %s[%s1%s] Full path\n    %s[%s2%s] Just domain'%(W,R,W,W,G,W,W,G,W)
	chc=raw_input('\n%s[%s?%s] Choice : '%(W,R,W))
	if chc == '1':podo('.dork');os.system('rm -rf .p && rm -rf .dork');exit('\n%s[%s✓%s] Done, saved in results.txt'%(W,G,W))
	elif chc == '2':get_domain();podo('.p');os.system('rm -rf .p && rm -rf .dork');exit('\n%s[%s✓%s] Done, saved in results.txt'%(W,G,W))
	else:podo('.dork');os.system('rm -rf .p && rm -rf .dork');exit('\n%s[%s✓%s] Done, saved in results.txt'%(W,G,W))
def get_domain():
	for site in open('.dork').read().splitlines():
		try:_p=site.split('/')[0]+'//'+site.split('/')[2];open('.p','a+').write(_p+'\n')
		except:continue
def podo(file):
	podo=[]
	for site_ in open(file).read().splitlines():
		try:
			if site_ in podo:continue
			else:podo.append(site_);open('results.txt','a+').write(site_+'\n')
		except:continue
if __name__=='__main__':
	main()
