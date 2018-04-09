# import libraries
# coding: latin-1
import urllib2
from bs4 import BeautifulSoup
# specify the url
quote_page = "http://www.xeno-canto.org/species/Emberiza-rustica"
# query the website and return the html to the variable ‘page’
page = urllib2.urlopen(quote_page)


# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html5lib')
serch = [];
results = soup.find_all('nav', {'class':"results-pages"})
print(len(results))
print results

serch=results
print serch


matching = [s for s in serch if "<a" in s]
print matching
