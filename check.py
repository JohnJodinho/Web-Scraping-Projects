from bs4 import BeautifulSoup

html_doc = """
<html>
  <body>
    <div id="text">Hello, World!</div>
  </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

tag = soup.find("", attrs={"id": "text"})


print(tag)