from urlScrapper import get_data
from audio_player import play_music
from send_email import create_email_and_send
def main():
    query=input()
    receiver=input("Enter your email: ")
    video_url=get_data(query)
    play_music(video_url,query)
    create_email_and_send(query,receiver)
if __name__=='__main__':
    main()
