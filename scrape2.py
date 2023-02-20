from soup_getters import get_html
from bs4 import BeautifulSoup as BS
import re

html_content = get_html("http://www.pythonscraping.com/pages/page3.html")
if html_content is None:
    print("Error retrieving html content")
else:
    soup = BS(html_content, "html.parser")
    images = soup.find_all("img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")}) 
    for img in images:
        print(img['src'])
        print(img.parent.previous_sibling.get_text())
