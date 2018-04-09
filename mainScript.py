import re
import subprocess
import MySQLdb
conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="password",
                  db="birds")

birdFirstName = "emberiza"
birdSecondName = "rustica"

proc = subprocess.Popen(['./getDownloadExtensions.sh', birdFirstName, birdSecondName], stdout=subprocess.PIPE)
allHyperSoundLinks = proc.stdout.read()


linkList = allHyperSoundLinks.split("\n")
linkList.pop()

b = []

for i in range(0,len(linkList)):
    filename = "/Users/Newera/birdAudioFiles/%s-%s_%d.mp3" %(birdFirstName, birdSecondName, i)
    proc = subprocess.Popen(['curl', '-Lo', filename, linkList[i]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    b.append(re.findall("\d+", linkList[i]))


for i in range(0,len(linkList)-1):
    print b[i]


    #try:
    #   x.execute("""INSERT INTO anooog1 VALUES (%s,%s)""",(188,90))
    #   conn.commit()
    #except:
    #   conn.rollback()

    #conn.close()
