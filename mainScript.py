import re
import subprocess
import MySQLdb
conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="ihoco",
                  db="birds")


proc = subprocess.Popen(['./getDownloadExtensions.sh', 'emberiza', 'rustica'], stdout=subprocess.PIPE)
allHyperSoundLinks = proc.stdout.read()


linkList = allHyperSoundLinks.split("\n")
linkList.pop()

b = []

for i in range(0,len(linkList)):
    filename = "/Users/Frej/birdAudioFiles/emberiza-rustica_%d.mp3" %(i)
    proc = subprocess.Popen(['curl', '-Lo', filename, linkList[i]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    b.append(re.findall("\d+", linkList[i]))


for i in range(0,len(linkList)-1):
    pass
    #print b[i][0]


    #try:
    #   x.execute("""INSERT INTO anooog1 VALUES (%s,%s)""",(188,90))
    #   conn.commit()
    #except:
    #   conn.rollback()

    #conn.close()
