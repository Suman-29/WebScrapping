
import bs4 as bs
import re
import csv
from urllib.request import urlopen ,Request



class Company_details:
	
	def __init__(self):
		self.Name = ""
		self.ProjectSize = ""
		self.HourRate = ""
		self.EmpCount = ""
		self.Founded = ""
		self.Clfocus = ""
		self.Infocus = ""
		self.Location = ""
		self.Email = ""
		self.Phone = ""
		self.Website = ""
		self.SrcUrl = ""
	

	def writeToCSv(self):
		wo.writerow([self.name,self.ProjectSize,self.HourRate,self.EmpCount,self.Founded,self.Location,self.Phone,self.Website])
		

	def parse_companies_url(self,comp_url):
		print("Inside company URl",comp_url)
		webComp = urlopen(Request(comp_url, headers={'User-Agent': 'Mozilla/5.0'}))
		csauce = webComp.read()
		csoup = bs.BeautifulSoup(csauce,'lxml')
		
		cbody = csoup.find('body')

		divTag = cbody.find("div",{"class":"field field-name-field-pp-year-founded field-type-number-integer field-label-inline clearfix"})
		try:
			founded = divTag.find("div",{"class":"field-item even"})
		except Exception as e:
			print (e)
		
		try:
			print (founded.text)
			self.Founded = founded.text
		except Exception as e:
			print (e)
			self.Founded ="Undisclosed"

		divmenu = cbody.find("div",{"class":"quick-menu"})
		try:
			website = divmenu.find("a")
			print (website.get('href'))	
			self.Website = 	website.get('href')
		except Exception as e:
			print (e)

		location = divmenu.find("div",{"class":"city-name"})
		try:
			print (location.text)
			self.Location = location.text
		except Exception as e:
			print (e)

		try:
			telephone = divmenu.find("span",{"class":"contact-dropdown-phone-ico"})
			print (telephone.parent.get('href'))				
			self.Phone = telephone.parent.get('href')
		except Exception as e:
			print (e)
		
	
#----------------------------------------------------------------#
url="https://clutch.co/directory/mobile-application-developers"
fp = open("MobileApp1.csv",'w+',newline='', encoding='utf-8')
wo = csv.writer(fp)
wo.writerow(['Company Name','Min Project Size','Avg hourly rate','Employees','Founded','Location','Phone','Website'])

for i in range (5,6):

	if i==0:
		pageUrl = url
	else:
		page ="?page="
		pageUrl = str(url)+page+str(i)
	print (pageUrl)
	webdata = urlopen(Request(pageUrl, headers={'User-Agent': 'Mozilla/5.0'}))
	sauce = webdata.read()
	soup = bs.BeautifulSoup(sauce,'lxml')
	#print(soup.prettify())
	body = soup.find('body')

	i=0
	divTags= soup.find_all("div",{"class":"col-xs-12 col-md-10 bordered-right provider-base-info"})
	for div in divTags:
		CompDetails = Company_details()
		name = div.find("h3",{"class":"company-name"})

		try:			
			print (name.a.text)
			CompDetails.name=name.a.text
		except:
			pass

		link = div.find('a', href=re.compile("^https://clutch.co/profile"))
		try:
			print (link.get('href'))
			comp_url =link.get('href')
			CompDetails.parse_companies_url(comp_url)
		except:
			pass

		projectSize = div.find("div",{"class":"module-list"}).find_all("div",{"class":"list-item"})[0]
		try:
			CompDetails.ProjectSize = projectSize.text
			print(projectSize.text)
		except:
			pass

		employees = div.find("span",{"class":"employees"})
		try:
			CompDetails.EmpCount=(employees.text.replace(" ","-"))
			print (CompDetails.EmpCount)
		except:
			pass

		hourRate = div.find("span",{"class":"hourly-rate"})
		try:
			CompDetails.HourRate = hourRate.text
			print(CompDetails.HourRate)
		except:
			CompDetails.HourRate="Undisclosed"

		CompDetails.writeToCSv()


fp.close()

