f = open("xenoscrapingfile.txt","rb") #opens file with name of "test.txt"

s = [];
d = "www.xeno-canto.org"
for line in f:
    s.append(line)

full =[];
#print(len(s))
for i in range(1,len(s)):
    full.append(d+s[i])

print(full[0])
