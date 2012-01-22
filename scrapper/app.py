#We want to developpe a scrapper app.

url = 'http://news.ycombinator.com'
pattern = 'sopa'
#It should start with a getting the content of a given url. 
import urllib2 
from lxml import etree
import StringIO
import re

seenUrls = set()

def scrape (url, depth):
	if (depth == 0):
		return
	if(url.find("http") != 0):	
		return
	if(url in seenUrls):
		#print ('skipping '+url)
		return
	#print (depth * '*')
	seenUrls.add(url)
	#print (str(depth) + ': ' + url)
	try:
		file = urllib2.urlopen(url)
		raw = file.read()
		if(len(raw) == 0):
		  return;

		#Multiple ways to extract the links
		#either using beautiful soup.
		#or using lxml.
		parser = etree.HTMLParser()
		tree   = etree.parse(StringIO.StringIO(raw), parser)
		textContent = tree.xpath('string()')
		if(re.match(pattern, textContent, re.IGNORECASE)):
			print ('match for '+url)
		#We filter anchor that do not have a destination
		links = tree.xpath('//a[@href]')
		for link in links:
			if('href' in link.attrib):
				scrape(link.attrib['href'], depth -1)
	except urllib2.URLError:
		pass
	except:
		raise

scrape(url, 5)