from pytube import YouTube
import vlc
from pydub import AudioSegment
import time
import os
import pygame
def play_music(URL,query):
    yt=YouTube(URL)
    t=yt.streams.filter(only_audio=True).first()
    t.download(filename=f'{query}.wav')
    path=os.path.join(os.getcwd(),'dil.wav')
    audio_segment=AudioSegment.from_file(path)
    audio_duration=len(audio_segment)/1000
    player=vlc.MediaPlayer(f'{query}.wav')
    player.play()
    sec=audio_duration
    pygame.init()
    clock=pygame.time.Clock()
    FPS=1
    while sec>=0:
        print(sec)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.pause()
                    print('Paused')
                elif event.key == pygame.K_s:
                    player.play()
                    print('Played')
        if player.is_playing():
            sec-=1
        clock.tick(FPS)
