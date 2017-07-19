from bs4 import BeautifulSoup
from urllib import request
import re


def youtube_search(song, artist):
    format_song = song.replace(' ', '+').strip()
    format_artist = artist.replace(' ', '+').strip()
    data = request.urlopen('https://www.youtube.com/results?search_query=' + format_song + '+by+' + format_artist)
    soup = BeautifulSoup(data)
    for link in soup.findAll('a', attrs={'href': re.compile('/watch', re.I)}):
        return link['href']


def soundcloud_search(song, artist):
    format_song = song.replace(' ', '%20').strip()
    format_artist = artist.replace(' ', '%20').strip()
    x = song.replace(' ', '-')
    y = artist.replace(' ', '-')
    data = request.urlopen('https://soundcloud.com/search?q=' + format_song + '+' + format_artist)
    soup = BeautifulSoup(data)
    for link in soup.findAll('a', attrs={'href': re.compile('(' + x + '|' + y + ')', re.I)}):
        return 'https://www.soundcloud.com' + link['href']


def audiomack_search(song, artist):
    format_song = song.replace(' ', '+').strip()
    format_artist = artist.replace(' ', '+').strip()
    data = request.urlopen('https://www.audiomack.com/search?q=' + format_song + '+' + format_artist)
    soup = BeautifulSoup(data)
    for link in soup.findAll('a', attrs={'href': re.compile('/song/.*?' + format_song, re.I)}):
        return 'https://www.audiomack.com' + link['href']