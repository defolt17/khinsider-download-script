from bs4 import BeautifulSoup as bs
from urllib.parse import unquote
from os import mkdir, chdir
import requests
import wget

url = '< Full page link >'
folder = '< Folder name >'
headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}

def fun(name, furl, headers=headers):
    url = 'https://downloads.khinsider.com' + furl
    r = requests.get(url, headers=headers)
    s = bs(r.text, 'html.parser')

    for i in s.find_all("audio"):
        wget.download(unquote(i.attrs['src']), name)

r = requests.get(url, headers=headers)
s = bs(r.text, 'html.parser')

links = []
a = {}
for i in s.find_all("td", {"class" : "clickable-row"}):
    links.append(i.find_all("a")[0])

l = []
for i in links:
    l.append(i.text)

l = l[::3]

for i in links:
    a[i.text] = i.attrs['href']

mkdir(folder)
chdir(folder)
for i in l:
    fun(i, a[i])
