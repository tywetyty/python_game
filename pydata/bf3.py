import urllib2
from BeautifulSoup import *
from urlparse import urljoin
import sqlite3
url1='https://ruby-china.org/'
c=urllib2.urlopen('https://ruby-china.org/')
soup = BeautifulSoup(c.read())
def gettextonly(soup):
		v=soup.string
		if v ==None:
			c=soup.contents
			resultetext=''
			for t in c:
				subtext=gettextonly(t)
				resultetext+=subtext+'\n'
			return resultetext
		else:
			return v.strip()

# urlall= urljoin('https://ruby-china.org/', '#index')
# print links[0]['href']
# print urlall
# print urlall.find("x")
# urlall=urlall.split('#')[0]
# print urlall
#print(soup.prettify())
#
# for link in links:
# 	if ('href' in dict(link.attrs)):
# 		#print link['href'] 
# 		url=urljoin(url1, link['href'])
# 		print url[0:4]
# 		print url[0:4]=='http'
# 		print type(url)
# print soup('a')[0].contents
# print len(soup('a'))
# print dict(soup('a'))
# print soup.contents
