from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup as BS

try:
    html_content = urlopen("http://www.pythonscraping.com/pages/page3.html")
except HTTPError as e:
    print(e.reason)
except URLError as e:
    print(e.reason)
else:
    soup = BS(html_content, "html.parser")
    # Get tag that contains a particular text = "Now with super-colorful bell peppers!"
    html_tag = soup.body
    the_tags = soup.find_all(lambda html_tag: html_tag.text.find("Now with super-colorful bell peppers!") != -1)
    for tag in the_tags:
        for tag_content in tag.contents[::-1]:
            if isinstance(tag_content, type(soup.new_string(" "))) or isinstance(tag_content, str):
                content = tag_content if tag_content.strip() != "" else None
                print(content)