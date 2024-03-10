import sys
import requests
import youtube_dl
from bs4 import BeautifulSoup

def ToSearch(str):
    if (str == "pornhub.com"):
        return "div","preloadLine"
    else:
        return "div","post_el_small"

def webSite(str):
    if (str.find("pornhub.com") != -1):
        return "pornhub.com"
    if (str.find("sxyprn.com") != -1):
        return "sxyprn.com"

if (len(sys.argv) < 2):
    print("Add a link")
    exit(1)
URL = sys.argv[1]
try:
    page = requests.get(URL)
except IOError:
    print("No Internet!")
    exit(1)

soup = BeautifulSoup(page.content, "html.parser")
webname = webSite(URL)
tosearch =ToSearch(webSite);
result = soup.find_all(tosearch)
format = '480p' if (webname == "pornhub.com") else '0'
element_href = "view" if (webname == "pornhub.com") else "post"
links = []
for each_link in result:
    ln = each_link.find("a")
    if (ln):
            a = ln.get('href')
            if (a and a.find(element_href) != -1):
                links.append("https://"+webname + a)
for link in links:
        print(link)
ydl_opts = {
    'format' : format,
    'download_archive' : 'downloaded_videos.txt'
}
print("Downloading will Start")
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for link in links:
        ydl.download([link])
