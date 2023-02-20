from soup_getters import get_html
from bs4 import BeautifulSoup as BS

html_content = get_html("http://www.pythonscraping.com/pages/page3.html")
if html_content is None:
    print("Failed to get html_content")
else:
    soup = BS(html_content, "html.parser")
    for sibling in soup.find("table", {"id": "giftList"}).tr.next_siblings:
        if sibling.text.strip() == "":
            continue
        print(sibling.prettify())