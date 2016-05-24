from urllib.request import urlopen 
from bs4 import BeautifulSoup
import re
import os
import pprint
import datetime
import json
################################################################################
#Initialize URL variables
feeds = []
sForum = 'breitbartproduction'
sThread = '4849504492'  #clintoncash        #trump_immig'4847389789'
sLimit = '100'          # limit is 25 to 100
sOrder = 'desc'         # asc (oldest), desc (newest) 
sAPI_KEY = '<COPY AND PASTE THE API_KEY FROM YOUR DISQUS ACCOUNT INTO THIS FIELD>'
file_name = '/root/test/scrapingEnv/data_capture/Threads_listHot' + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + '.txt'

#Open new file with date and time in the filename.
file = open(file_name,'w')
#Compile the regular expressions needed to filter out the disqus information.
has_next_page = re.compile('(\"hasNext\":true)+')
next_cursor = re.compile('([0-9]{16}:[0]:[0])+')
has_prev_page = re.compile('(\"hasPrev\":true)+')
prev_cursor = re.compile('([0-9]{16}:[0]:[1])+')

#URL0 lists users and cursor position post/list
#URL0 = "https://disqus.com/api/3.0/posts/list.json?forum=%s&thread=%s&limit=%s&order=%s&api_key=%s" % (sForum, sThread, sLimit, sOrder, sAPI_KEY)
#URL1 lists threads in a forum and cursor position threads/list. This should fail if "sThread is supplied.
URL1 = "https://disqus.com/api/3.0/threads/listHot.json?forum=%s&api_key=%s&limit=%s" % (sForum, sAPI_KEY, sLimit)

#Open the URL and download the html.
html = urlopen(URL1).read().decode('utf-8')
responseJSON = json.loads(html)
i = 0
file.write('Thread ID               Title of Article\r')
for i in range(49):
    file.write('%s %s\r\n' % (responseJSON.get("response")[i].get("id"), responseJSON.get("response")[i].get("clean_title")))
file.close()
