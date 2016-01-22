##################################
#This is main program for crawler#
##################################
import urllib
import HTMLParser
print "************* crawler version 0.0.0 *************"
url = "http://www-rohan.sdsu.edu/~gawron/index.html"
url_handle = urllib.urlopen(url);
html_page = url_handle.read();
#print html_page;

urlText = []

class parseText(HTMLParser.HTMLParser):
	def handle_data(self,data):
		if data != '\n':
			urlText.append(data);

# create object of parseText
lParser = parseText();
thisurl = "http://www-rohan.sdsu.edu/~gawron/index.html"
#Feed HTML file into parser
lParser.feed(urllib.urlopen(thisurl).read())
lParser.close();
for item in urlText:
	print item;

