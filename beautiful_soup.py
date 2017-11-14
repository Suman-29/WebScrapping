import bs4 as bs
import requests
import re
import csv
from urllib.request import urlopen ,Request

url="https://clutch.co/directory/mobile-application-developers"
print (type(url))


webdata = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))

#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
#webdata = urlopen("https://clutch.co/directory/mobile-application-developers",None,headers = {'User-Agent': 'Mozilla/5.0'})

sauce = webdata.read()
soup = bs.BeautifulSoup(sauce,'lxml')

fp = open("MobileApp.csv",'w')
wo = csv.writer(fp)
#print(soup.prettify())
body = soup.find('body')
wo.write(['Company Name','Min Project Size','Avg hourly rate','Employees','Founded','Client Focus','Industry focus','Locations','Contact email','Contact phone','Company website','Source URL'])
for url in body.find_all('a', href=re.compile("^https://clutch.co/profile")):
	print (url.get('href'))
	fp.writelines(url.get('href'))
	fp.writelines("\n")


	#fp.writelines("\n")


'''for i in range (1,97):
	page="?page="

	urlp= str(url)+page+str(i)

	print (urlp)

	webdata = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))


	sauce = webdata.read()
	soup = bs.BeautifulSoup(sauce,'lxml')

	fp = open("MobileApp.csv",'a')
#print(soup.prettify())
	body = soup.find('body')
	for url in body.find_all('a', href=re.compile("^https://clutch.co/profile")):
		#print (url.get('href'))
		fp.writelines(url.get('href'))
		fp.writelines("\n")'''
fp.close()
	