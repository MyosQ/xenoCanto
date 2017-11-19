#!/usr/bin/python
import re
import subprocess

print "start"
#p = subprocess.check_output(['./getDownloadExtensions.sh', 'emberiza', 'rustica'])

proc = subprocess.Popen(['./getDownloadExtensions.sh', 'emberiza', 'rustica'], stdout=subprocess.PIPE)
allHyperSoundLinks = proc.stdout.read()


linkList = allHyperSoundLinks.split("\n")
linkList.pop()

a = linkList
b = []

for i in range(0,len(linkList)-1):
    filename = "emberiza-rustica_%d.mp3" %(i)
    proc = subprocess.Popen(['curl', '-Lo', filename, linkList[i]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    b.append(re.findall("\d+", a[i]))


for i in range(0,len(linkList)-1):
    print b[i][0]


#print p

print "end"
