import urllib2
import urllib
from bs4 import BeautifulSoup
import cookielib

# Store the cookies and create an opener that will hold them
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

# Add our headers
opener.addheaders = [('User-agent', 'RedditTesting')]

# Install our opener (note that this changes the global opener to the one
# we just made, but you can also just call opener.open() if you want)
urllib2.install_opener(opener)

login = raw_input("What is your username?")
password = raw_input("What is your password?")


gpaURL = 'https://wrem.sis.yorku.ca/Apps/WebObjects/ydml.woa/wa/DirectAction/document?name=GradeReportv1'
loginCredentials = {
	'mli': login ,
	'password': password
}

data = urllib.urlencode(loginCredentials)

loginRequest = urllib2.Request(gpaURL, data)

resp = urllib2.urlopen(loginRequest);
contents = resp.read()

print(contents)


#page = urllib2.urlopen(gpaURL)
#soup = BeautifulSoup(resp);

#print(soup.prettify())