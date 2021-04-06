import urllib.request
from bs4 import BeautifulSoup as soup
from threading import Thread
from .SongClass import Song



add = "/charts/top"
url ="https://soundcloud.com"

# nuskaito html faila ir sudeda i soup
html = urllib.request.urlopen(url+add).read()
page_soup = soup(html, "html.parser")
ul_list = page_soup.find_all('a')
l= range(47,147,2)

song_list = []
# suranda linkus
for n in l:
     song_list.append(ul_list[n])
     
links =[]
# sudeda linkus i lista
for n in song_list:
     links.append(n.get('href'))
 
# aprasomi threads kurie sudeda dainas i Song klase
songs = []
def th(link):
     base = url+link
     page = urllib.request.urlopen(base).read()
     page_so = soup(page, "html.parser")
     song_title = page_so.img["alt"]
     genre = page_so.header.meta.meta["content"]
     likes = page_so.header.meta.meta.meta["content"].split(":")
     pic = page_so.img["src"]
     songs.append(Song(song_title, genre, likes[1], pic))

# paleidziami threads
threadlist = []
for u in links:
     t = Thread(target =th, args=(u,))
     t.start()
     threadlist.append(t)
     
for b in threadlist:
     b.join() # palaukia kol threads pabaigia darba

def return_object():
    return songs
