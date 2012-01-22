import sys 
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
			print (url)
		#We filter anchor that do not have a destination
		links = tree.xpath('//a[@href]')
		for link in links:
			if('href' in link.attrib):
				scrape(link.attrib['href'], depth -1)
	except urllib2.URLError as e:
	  #when 403 error, we have been recognized as a bot. Which we are :-)
	  # We could spoof a user agent but it's not the best approach.
	  writeerror('url '+url+' could not be retrived ' + str(e.code))

	except UnicodeEncodeError as e:
	  writeerror('characters for url '+url+' are not valid '+str(e.reason))
	  
	except:
		raise

def writeerror(error, message):
  sys.stderr.write("Error : "+message+ "\n")

#Command line parameter handling
#argv first parameter is commandName
if (len(sys.argv) != 4):
  print ("usage : app.py seed pattern depth")
  exit(1)
url = sys.argv[1]#'http://news.ycombinator.com'
pattern = sys.argv[2]#"css3"
depth = int(sys.argv[3])#5

scrape(url, depth)