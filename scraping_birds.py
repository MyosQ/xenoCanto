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

s = [];
for t in soup.findAll('table')[3].findAll('tr'):
    s.append(t)

#name = [];
length = [];
recordist = [];
date = [];
time = [];
country = [];
location = [];
elevation= [];
song_type = [];
remarks = [];
quality = [];
category_nr = [];


i=0
j=0

for row in s:
    if i !=0:

        length.append(row.contents[5].get_text())
        recordist.append(row.contents[7].get_text())
        date.append(row.contents[9].get_text())
        time.append(row.contents[11].get_text())
        country.append(row.contents[13].get_text())
        location.append(row.contents[15].get_text())
        elevation.append(row.contents[17].get_text())
        song_type.append(row.contents[19].get_text())
        remarks.append(row.contents[21].get_text())
        category_nr.append(row.contents[24].get_text())

        # Hoppar quality just nu för den är en class inte text!

        length[j] = length[j].strip()
        country[j] = country[j].strip()
        remarks[j] = remarks[j].strip()
        recordist[j] = recordist[j].strip()
        date[j] = date[j].strip()
        time[j] = time[j].strip()
        country[j] = country[j].strip()
        location[j] = location[j].strip()
        elevation[j] = elevation[j].strip()
        song_type[j] = song_type[j].strip()
        remarks[j] = remarks[j].strip()
        #quality[j] = quality[j].strip()
        #category_nr[j] = category_nr[j].strip()
        j=j+1

    i=1


print date

#length[0] = length[0].strip()
#country[0] = country[0].strip()
#remarks[0] = remarks[0].strip()
#recordist[0] = recordist[0].strip()
#date[0] = date[0].strip()
#time[0] = time[0].strip()
#country[0] = country[0].strip()
#location[0] = location[0].strip()
#elevation[0] = elevation[0].strip()
#song_type[0] = song_type[0].strip()
#remarks[0] = remarks[0].strip()
#quality[0] = quality[0].strip()
#category_nr[0] = category_nr[0].strip()
