import pytube
from pytube import YouTube
import vlc
from pydub import AudioSegment
import time
import os
def play_music(URL,query):
    try:
        yt=YouTube(URL)
        t=yt.streams.filter(only_audio=True).first()
        t.download(filename=f'{query}.mp3')
    except pytube.exceptions.LiveStreamError:
        print('Not available')
        return
    path=os.path.join(os.getcwd(),f'{query}.mp3')
    audio_segment=AudioSegment.from_file(path)
    # audio_duration=len(audio_segment)/1000
    # player=vlc.MediaPlayer(f'{query}.mp3')
    # player.play()
    # sec=audio_duration
    # print(audio_duration)
    # time.sleep(audio_duration)

    
