from bs4 import BeautifulSoup
from urllib import request
import re

def youtube_search(song, artist):
    format_song = song.replace(' ', '+')
    format_song = format_song.strip()
    format_artist = artist.replace(' ', '+')
    format_artist = format_artist.strip()
    data = request.urlopen('https://www.youtube.com/results?search_query=' + format_song + '+by+' + format_artist)
    soup = BeautifulSoup(data)
    for link in soup.findAll('a', attrs={'href': re.compile('^/watch')}):
        return link['href']



def soundcloud_search(song, artist):
    pass


def spotify_search(song, artist):
    pass


def audiomack_search(song, artist):
    format_song = song.replace(' ', '+')
    format_song = format_song.strip()
    format_artist = artist.replace(' ', '+')
    format_artist = format_artist.strip()
    data = request.urlopen('https://www.audiomack.com/search?q=' + format_song + '+' + format_artist)
    soup = BeautifulSoup(data)
    for link in soup.findAll('a', attrs={'href': re.compile('^/song/'+format_artist)}):
        return 'https://www.audiomack.com' + link['href']
