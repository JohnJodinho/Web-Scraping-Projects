from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup as BS

def get_title(url):

    try:
        html = urlopen(url)
    except (URLError):
        return None
    try:
        soup = BS(html.read(), 'html.parser')
        title = soup.body.h1
    except AttributeError:
        return None
    return title

title = get_title('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print("No title found")
else:
    print(title.text)