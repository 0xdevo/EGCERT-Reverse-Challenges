import requests
import re

file = open("hashes.txt","r")
firstPart = []
secondPart = []
for h in file.readlines():
	h = h.replace("\n","")
	user_agent = {
	                'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
	url = "https://hashtoolkit.com/reverse-hash?hash=" + h
	r = requests.get(url,headers=user_agent)
	val = re.findall('decrypted sha256 hash">.*?<',r.text)[0].replace('decrypted sha256 hash">','').replace('<','')
	val = val.decode('utf-8')
	firstPart.append(val[0])
	secondPart.append(val[1])


print ''.join(firstPart)
print ''.join(secondPart)