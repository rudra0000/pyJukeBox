from urlScrapper import get_data
from audio_player import play_music
def main():
    query=input()
    video_url=get_data(query)
    play_music(video_url,query)
if __name__=='__main__':
    main()