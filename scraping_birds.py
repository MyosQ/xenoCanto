# import libraries
# coding: latin-1
import urllib2
from bs4 import BeautifulSoup




def main():
    # specify the url
    quote_page = "http://www.xeno-canto.org/species/Emberiza-rustica"

    # query the website and return the html to the variable ‘page’
    page = urllib2.urlopen(quote_page)


    # parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(page, 'html5lib')

    # Fill vector allRows with table-rows from table[3] (the table of interest)
    allRows = [];
    for tr in soup.findAll('table')[3].findAll('tr'):
        allRows.append(tr)

    # Entries of each row. Name is not needed (obviously)
    length = [];    recordist = []; date = [];  time = [];
    country = [];   location = [];  elevation= [];  song_type = [];
    remarks = [];   quality = [];   category_nr = [];

    i=0; j=0;
    for row in allRows:
        if i !=0:

            columns = row.find_all('td')
            length.append(columns[2].get_text())
            recordist.append(columns[3].get_text())
            date.append(columns[4].get_text())
            time.append(columns[5].get_text())
            country.append(columns[6].get_text())
            location.append(columns[7].get_text())
            elevation.append(columns[8].get_text())
            song_type.append(columns[9].get_text())
            remarks.append(columns[10].get_text())
            # qualty
            category_nr.append(columns[12].get_text())

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
            # quality ..
            category_nr[j] = category_nr[j].strip()
            j=j+1;

        i=1;

if __name__ == '__main__':
    main()
