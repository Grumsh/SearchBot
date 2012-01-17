#We want to developpe a scrapper app.
#It should start with a getting the content of a given url. 
# Nothing agains using a few helper libraries.
import urllib2

file = urllib2.urlopen('http://www.google.com')
raw = file.read()

from BeautifulSoup import BeautifulSoup
b = BeautifulSoup(raw)
print b.prettify()