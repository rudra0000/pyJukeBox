from urlScrapper import get_data
from audio_player import download_track
from send_email import create_email_and_send
from getPlaylists import get_user_tracks
def main():
    query=input()
    if query[0:7]=='spotify':
        user_id=input("Enter your spotify user id ")
        receiver=input("Enter your email: ")
        songs=get_user_tracks(user_id)
        for song in songs:
            video_url=get_data(song)
            download_track(video_url,song)
            create_email_and_send(song,receiver)
        return
    receiver=input("Enter your email: ")
    video_url=get_data(query)
    print(video_url)
    download_track(video_url,query)
    create_email_and_send(query,receiver)
if __name__=='__main__':
    main()
