from urllib.request import urlopen
from urllib.error import HTTPError 
from urllib.error import URLError
import ssl
from time import sleep


url = "https://www.thenetnaija.net/videos"

# ssl errors handler
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for i in range(10):
    try:
        html  = urlopen(url, context=ctx).read().decode("utf-8")
        break
    except HTTPError and URLError:
        print("re_trying")
        sleep(3)
        continue
print(i)

soup = BS(html, "html.parser")

h3s = soup.select(".tb-info h3")

print(len(h3s))

