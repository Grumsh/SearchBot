#We want to developpe a scrapper app.

url = 'http://www.hackernews.com'
#It should start with a getting the content of a given url. 
import urllib2
file = urllib2.urlopen(url)
raw = file.read()

print ('downloaded file from url '+url+' content was '+str(len(raw))+' bytes')

#Multiple ways to extract the links
#either using beautiful soup.
from BeautifulSoup import BeautifulSoup
b = BeautifulSoup(raw)

#or using lxml. 
from lxml import etree
import StringIO
parser = etree.HTMLParser()
tree   = etree.parse(StringIO.StringIO(raw), parser)
links = tree.xpath('//a')
print ('found '+str(len(links))+' links in the file')