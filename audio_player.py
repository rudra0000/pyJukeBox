import pytube
from pytube import YouTube
from pydub import AudioSegment
import os
def download_track(URL,query):
    try:
        yt=YouTube(URL)
        t=yt.streams.filter(only_audio=True).first()
        t.download(filename=f'{query}.mp3')
    except pytube.exceptions.LiveStreamError:
        print('Not available')
        return
    except pytube.exceptions.RegexMatchError:
        print("Invalid YouTube URL.")
        return

    path=os.path.join(os.getcwd(),f'{query}.mp3')
    audio_segment=AudioSegment.from_file(path)
