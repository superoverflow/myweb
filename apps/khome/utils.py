import os
import logging
import re
from collections import namedtuple

import youtube_dl
from pydub import AudioSegment
from urllib.parse import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup

Result = namedtuple("Result", "id title")

def download_youtube(dir, video_id):
    """ store the {id}.mp4 and {id}.mp3"""
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': os.path.join(dir ,'%(id)s.%(ext)s'),
        'keepvideo': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f'http://www.youtube.com/watch?v={video_id}'])

def remove_vocal(in_mp3, out_mp3):
    """ remove vocal from in_mp3 and produce out_mp3 """
    logging.debug(f'removing vocal for {in_mp3}')
    stereo = AudioSegment.from_file(in_mp3, format = 'mp3')
    left, right = stereo.split_to_mono()
    inv_right = right.invert_phase()
    no_vocal = left.overlay(inv_right)
    no_vocal.export(out_mp3, format = 'mp3')
    logging.debug(f'generated {out_mp3}')

def search_youtube(text_to_search):
    query = quote(text_to_search)
    # search only music type
    url = f"https://www.youtube.com/results?sp=EgIQAUIECAASAA%253D%253D&search_query={query}"
    response = urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    extracts = [ (_extract_id_from_href(vid['href']), vid['title'])
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'})]
    return [ Result(id, title) for (id, title) in extracts if id  ]

def _extract_id_from_href(href):
    pattern = r"/watch\?v=(.*)"
    m = re.match(pattern, href)
    if m:
        return m.group(1)
    else:
        return None


if __name__=='__main__':
    FORMAT = '%(asctime)-15s [%(levelname)s] %(filename)s %(lineno)d: %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)

    id = 'L6joGUdc6y4'
    dir = 'tmp'

    if not os.path.exists(dir):
        os.mkdir(dir)

    download_youtube(dir, id)

    in_mp3 = os.path.join(dir, f'{id}.mp3')
    out_mp3 = os.path.join(dir, f'{id}-music.mp3')
    remove_vocal(in_mp3, out_mp3)

    for r in search_youtube("hello"):
        print(r)