from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "https://www.rottentomatoes.com/browse/movies_in_theaters/?page=1"

html = urlopen(url, context=ctx).read().decode("utf-8")

soup = BS(html, "html.parser")
selector = ".js-tile-link .p--small"
movies = soup.select(selector)
len_movies = []
for movie in movies:
    len_movies.append((movie.text).strip())
map_dates = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}
print(len(len_movies))
print(len(movies))

for item in map_dates.items():
    print(item )
"""
<a class="js-tile-link" href="/m/memories_of_my_father" data-id="b3156fcd-15ff-3845-abda-b3117ead8a04" data-qa="discovery-media-list-item">

  <tile-dynamic isvideo="false">
    <img alt="Memories of My Father" class="posterImage" loading="lazy" slot="image" src="https://resizing.flixster.com/xJOa206dTlvl84Hgbd-b4uRvkXQ=/180x258/v2/https://resizing.flixster.com/sT-6FOjHis3RN7oernUn1Kvd2wo=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzkzYzljMzczLWYzMzgtNGVhYi1iMDY1LTMwN2EzODhjNzJjMC5qcGc=">
    
    <div slot="caption" data-track="scores" data-qa="discovery-media-list-item-caption">
        <score-pairs audiencesentiment="" audiencescore="" criticssentiment="positive" criticsscore="83" criticscertified="">
        </score-pairs>
        <span class="p--small" data-qa="discovery-media-list-item-title">
            Memories of My Father
        </span>
        
          <span class="smaller" data-qa="discovery-media-list-item-start-date">
            Opens Nov 18, 2022 
          </span>
        
    </div>
  </tile-dynamic>
</a>
"""

#main-page-content > div > div.discovery-grids-container.sticky-header > div > div > a:nth-child(13) > tile-dynamic > div > span.p--small

