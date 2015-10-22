import feedparser
from datetime import datetime

BBC_FEED_URL = 'http://feeds.bbci.co.uk/news/%s/rss.xml'

def read_news(feed_url):
 	try:
 		data=feedparser.parse(feed_url)
 	except Exception, e:
 		print 'Get Error: %s' %e

 	for entry in data.entries:
 		print entry.title
 		print entry.link
 		print entry.description
 		print '\n'

if __name__ == '__main__':
	print "==== Reading technology news feed from bbc.co.uk (%s)====" %datetime.today()
	print "Enter the type of news feed: " 
	print "Available options are: world, uk, health, sci-tech, business, technology" 
	typ=raw_input('News feed type:')
	read_news(BBC_FEED_URL %typ)
	print "==== End of BBC news feed =====" 
