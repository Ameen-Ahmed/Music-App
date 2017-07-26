from bs4 import BeautifulSoup
from urllib import request
import re


def youtube_search(song, artist):
    format_song = song.replace(' ', '+').strip()
    format_artist = artist.replace(' ', '+').strip()
    data = request.urlopen('https://www.youtube.com/results?search_query=' + format_song + '+by+' + format_artist)
    soup = BeautifulSoup(data, 'lxml')
    for link in soup.findAll('a', attrs={'href': re.compile('/watch', re.I)}):
        return 'https://www.youtube.com' + link['href']


def soundcloud_search(song, artist):
    reg = '(' + song.strip().replace(' ', '-') + ')'
    data = request.urlopen('https://soundcloud.com/search?q=' +
                           song.replace(' ', '%20').strip() +
                           '+' +
                           artist.replace(' ', '%20').strip())
    soup = BeautifulSoup(data, 'lxml')
    for link in soup.findAll('a', attrs={'href': re.compile(reg, re.I)}):
        return 'https://www.soundcloud.com' + link['href']


def audiomack_search(song, artist):
    reg = '/song/.*?('
    fullsong = song.strip().split()
    for word in fullsong:
        reg = reg + word + '-'
    reg = reg[:-1] + ')'
    data = request.urlopen('https://www.audiomack.com/search?q=' +
                           song.replace(' ', '+').strip() +
                           '+' +
                           artist.replace(' ', '+').strip())
    soup = BeautifulSoup(data, 'lxml')
    for link in soup.findAll('a', attrs={'href': re.compile(reg, re.I)}):
        return 'https://www.audiomack.com' + link['href']

def search(link):
    my_dict = {'Youtube': youtube_search,
               'SoundCloud': soundcloud_search,
               'Audiomack': audiomack_search}
    return my_dict[link.provider](link.song, link.artist)