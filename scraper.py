import request
from bs4 import BeautifulSoup
req = urllib.request.Request('http://www.voidspace.org.uk')
# with urllib.request.urlopen(req) as response:
#    the_page = response.read()
headers = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"}
soup=BeautifulSoup(req,headers=headers)
print(soup.prettify())