from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup as BS

def get_html(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e.code)
        return None
    except URLError as e:
        print(e.reason)
        return None
    else:
        return html

html = get_html("http://www.pythonscraping.com/pages/page3.html")
if html == None:
    print('Error')
else:
    soup = BS(html, "html.parser")
    gifts_children = soup.find(id="giftList").children
    gifts_descendants = soup.find(id="giftList").descendants
    n = 1
    for tag in gifts_children:
        if str(tag).strip() == "": 
            continue
        print(tag, end="\n")
        print(n)
        n += 1
            
            


