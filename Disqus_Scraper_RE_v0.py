from urllib import urlopen
import re
import os
import pprint
import datetime
#############################################################################

#Initialize URL variables
authors = []
sForum = 'breitbartproduction'
sThread = '4849504492'  #clintoncash        #trump_immig'4847389789'
sLimit = '100'          # limit is 25 to 100
sOrder = 'desc'         # asc (oldest), desc (newest) 
sAPI_KEY = '<enter your API key here>'
file_name = '/root/test/scrapingEnv/data_capture/userData' + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + '.txt'
#URL0 lists users and cursor position post/list
URL0 = "https://disqus.com/api/3.0/posts/list.json?forum=%s&thread=%s&limit=%s&order=%s&api_key=%s" % (sForum, sThread, sLimit, sOrder, sAPI_KEY)
#Open the webpage URL for scanning.
text = urlopen(URL0).read() 
#print(text)
#create a file to save the html text into.
if os.path.exists(file_name):
    print ("File exists")
    file = open(file_name,'w')
else:
    file = open(file_name, 'w')

#Compile the regular expressions needed to filter out the disqus information.
m = re.compile('(\"thread\":\"[0-9]{7,10}\")')      #Thread 10 digit identifier 
n = re.compile('(\"id\":\"[0-9]{7,9}\")')           #User ID 
o = re.compile('(\"author\":{)+')
p = re.compile('\"name\"\:\"[A-Za-z0-9]+')
q = re.compile('\"username\"\:\"[A-Za-z0-9]+[\.\_A-Za-z0-9]+')
r = re.compile('\"rep\"\:[0-9]+\.[0-9]+')
temp = o.split(text)
#print(len(temp))
i=0
del temp[0]
for i in range(len(temp)):
    if temp[i] != '"author":{' and i <= len(temp):
        #print(i)
        #print(authors)
        authors.append(temp[i])
#file.write("DISQUS reputation (rep):scale(1 to 50)")
file.write("<a href=https://help.disqus.com/customer/portal/articles/466247-user-reputation>(click me for) DISQUS Reputation Explained (rep):scale(1 to 50)</a>\r\n")
for author in authors:
    if len(author) >= 100:
        id = n.findall(author)
        name = p.findall(author)
        user = q.findall(author)
        rep = r.findall(author)
        #print( '%s %s %.15s\r') % (user, name, rep )
        file.write('%s %s %s %.15s\']\r\n' % (id, user, name, rep ))
file.close()
