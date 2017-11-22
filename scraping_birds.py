# import libraries
# coding: latin-1
import urllib2
import sys
from bs4 import BeautifulSoup
import MySQLdb
import re
import string


### Connect to database at localhost.
conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="password",
                  db="birds")
xConn = conn.cursor()


### Main
#input: birdFirstName, birdSecondName, URL
def main():
    # get name
    name = sys.argv[1]+"_"+sys.argv[2];

    # specify the url
    quote_page = sys.argv[3];

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
    remarks = [];   quality = [];   idNumber = [];

    j=0;
    iteratingAllRows = iter(allRows)
    next(iteratingAllRows)
    for row in iteratingAllRows:

        # Get columns of this row
        columns = row.find_all('td')

        # Extract the text in each column
        length.append(columns[2].get_text())
        recordist.append(columns[3].get_text())
        date.append(columns[4].get_text())
        time.append(columns[5].get_text())
        country.append(columns[6].get_text())
        location.append(columns[7].get_text())
        elevation.append(columns[8].get_text())
        song_type.append(columns[9].get_text())
        remarks.append(columns[10].get_text())
        idNumber.append(columns[12].get_text())

        # Quality is special
        # Gets all with class selected
        get_quality = (row.find_all(lambda tag: tag.name == 'li' and tag.get('class') == ['selected']))
        # Takes out the part of quality which is an integer
        x = str(get_quality[0])
        x = re.sub("\D", "", x)
        quality.append(x[len(x)-1])


        # strip newLines and tabs
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
        idNumber[j] = idNumber[j].strip()

        # Further remove blanklines and tabs
        idNumber[j] = (re.findall("\d+", idNumber[j]))
        remarks[j] = remarks[j].replace('\n', ' ').replace('\r', '')

        # Checks if these entries are not numeric, otherwise 595959 is used.
        time[j] = check_entries(time[j])
        length[j] = check_entries(length[j])
        elevation[j] = check_entries(elevation[j])
        quality[j] = check_entries(quality[j])
        idNumber[j] = check_entries(idNumber[j])

        print length[j]
        try:
            #mysqlQuery = "INSERT INTO emberiza_rustica (name, length, recordist, date, time, country, location, elevation, soundtype, remarks, quality, id) \
            #VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % (name, length[j], recordist[j], date[j], time[j], country[j], location[j], elevation[j], song_type[j], remarks[j], quality[j], idNumber[j][0]);
            #xConn.execute(mysqlQuery);
            xConn.execute("""INSERT INTO emberiza_rustica (name, length, recordist, date, time, country, location, elevation, soundtype, remarks, quality, id) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (name, length[j], recordist[j], date[j], time[j], country[j], location[j], elevation[j], song_type[j], remarks[j], quality[j], idNumber[j][0]))
            conn.commit()
        except TypeError as e:
            print(e)
            conn.rollback()

        j=j+1;


    conn.close()
    return

# Function to check if the input variable only contains numbers.
def check_entries(are_uint):

    x = str(are_uint)
    x = re.sub("\D", "", x)
    if(x == ""):
        are_uint="595959"
        return are_uint
    else:
        return are_uint


if __name__ == '__main__':
    main()
