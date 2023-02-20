from soup_getters import get_html
from bs4 import BeautifulSoup as BS
from typing import Optional

html_content = get_html("http://www.pythonscraping.com/pages/page3.html")

if html_content == None:
    print("An Error occurred")
else:
    soup = BS(html_content, "html.parser")
    # Get all tags on the page with at least two attributes
    tag = soup.html 
    all_tags = soup.find_all(lambda tag : len(tag.attrs) >= 2)
    for t in all_tags:
        print(t.name)