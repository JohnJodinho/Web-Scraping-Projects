from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup as BS

try:
    html = urlopen('https://pythonscrapingthisurldoesnotexist.com')
except HTTPError as e1:
    print(e1)
except URLError as e2:
    print("URL does not exist")
else:
    print(BS(html.read(), 'html.parser').h1) 

