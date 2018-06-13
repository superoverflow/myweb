import youtube_dl


def download_youtube(dir, video_id):
    """ store the {id}.mp4 and {id}.mp3"""
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': dir + '/%(id)s.%(ext)s',
        'keepvideo': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f'http://www.youtube.com/watch?v={video_id}'])


if __name__=='__main__':
    id = 'L6joGUdc6y4'
    download_youtube(id)