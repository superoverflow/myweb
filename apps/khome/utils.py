import os

import youtube_dl
from pydub import AudioSegment

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
    stereo = AudioSegment.from_file(in_mp3, format = "mp3")
    left, right = stereo.split_to_mono()
    inv_right = right.invert_phase()
    no_vocal = left.overlay(inv_right)
    no_vocal.export(out_mp3, format = "mp3")


if __name__=='__main__':
    id = 'L6joGUdc6y4'
    dir = 'tmp'

    if not os.path.exists(dir):
        os.mkdir(dir)

    download_youtube(dir, id)

    in_mp3 = os.path.join(dir, f'{id}.mp3')
    out_mp3 = os.path.join(dir, f'{id}.mp3')
    remove_vocal(in_mp3, out_mp3)