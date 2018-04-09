# import libraries
# coding: latin-1
import urllib2
import sys
from bs4 import BeautifulSoup
import MySQLdb
import re
import string

# Connect to database at localhost.
db = MySQLdb.connect(host= "localhost", user="root", passwd="password", db="birds")

# prepare a cursor object using cursor() method
cursor = db.cursor()




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
#    length = [];    recordist = []; date = [];  time = [];
#    country = [];   location = [];  elevation= [];  song_type = [];
#    remarks = [];   quality = [];   idNumber = [];

    j=0;
    iteratingAllRows = iter(allRows)
    next(iteratingAllRows)
    for row in iteratingAllRows:

        # Get columns of this row
        columns = row.find_all('td')

        # Extract the text in each column
        length = (columns[2].get_text())
        recordist=(columns[3].get_text())
        date=(columns[4].get_text())
        time=(columns[5].get_text())
        country=(columns[6].get_text())
        location=(columns[7].get_text())
        elevation=(columns[8].get_text())
        song_type=(columns[9].get_text())
        remarks=(columns[10].get_text())
        idNumber=(columns[12].get_text())

        # Quality is special
        # Gets all with class selected
        get_quality = (row.find_all(lambda tag: tag.name == 'li' and tag.get('class') == ['selected']))
        # Takes out the part of quality which is an integer
        x = str(get_quality)
        x = re.sub("\D", "", x)
        if(x==""):
            quality = 0
        else:
            quality = x[len(x)-1]


        # strip newLines and tabs
        length = length.strip()
        country = country.strip()
        remarks = remarks.strip()
        recordist = recordist.strip()
        date = date.strip()
        time = time.strip()
        country = country.strip()
        location = location.encode('utf-8').strip()
        elevation = elevation.strip()
        song_type = song_type.strip()
        remarks = remarks.strip()
        idNumber = idNumber.strip()

        # Further remove blanklines and tabs
        idNumber = (re.findall("\d+", idNumber))
        remarks = remarks.replace('\n', ' ').replace('\r', '')

        # Checks if these entries are not numeric, otherwise 595959 is used.
        time = check_entries(time)
        length = check_entries(length)
        elevation = check_entries(elevation)
        quality = check_entries(quality)
        idNumber = check_entries(idNumber)
        date = check_entries(date)

        #print remarks
        print location
        print length
        print name
        #print length[j]
        #print name

        #try:
            #mysqlQuery = "INSERT INTO emberiza_rustica (name, length, recordist, date, time, country, location, elevation, soundtype, remarks, quality, id) \
            #VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', %d, '%s', '%s', %d, %d)" % (name, length[j], recordist[j], date[j], time[j], country[j], location[j], int(elevation[j]), song_type[j], remarks[j], int(quality[j]), int(idNumber[j][0]));
            #cursor.execute(mysqlQuery);
        commandBeginning = "INSERT INTO %s " % name;
        SQLquery = commandBeginning+"(name, length, recordist, date, time, country, location, elevation, soundtype, remarks, quality, id) \
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)";
        data = (name, length, recordist, date, time, country, location, elevation, song_type, remarks, quality, idNumber[0]);
        cursor.execute(SQLquery, data);
            #print SQLquery
            #break
            #cursor.execute(commandBeginning + """(name, length, recordist, date, time, country, location, elevation, soundtype, remarks, quality, id) \
            #VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            #(name, name, length[j], recordist[j], date[j], time[j], country[j], location[j], elevation[j], song_type[j], remarks[j], quality[j], idNumber[j][0]))
        #    db.commit()
        #except TypeError as e:
        #    print(e)
        #    db.rollback()



        j=j+1;


    db.close()
    return

# Function to check if the input variable only contains numbers.
def check_entries(are_uint):

    x = str(are_uint)
    x = re.sub("\D", "", x)
    if(x == ""):
        # Debug value
        are_uint="595959"
        return are_uint
    elif(x == "00000000"):
        # Used to debug
        are_uint="1746-12-24"
        return are_uint
    else:
        return are_uint


if __name__ == '__main__':
    main()
