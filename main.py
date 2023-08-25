from urlScrapper import get_data
from audio_player import download_track
from send_email import create_email_and_send,sendSpotifyPlaylistSongs
from getPlaylists import get_user_tracks
from unidecode import unidecode
import json
def capitalize_words(input_string):
    words = input_string.split() 
    capitalized_words = [word.title() for word in words]
    return ' '.join(capitalized_words)
def main():
    query=input()
    try:
        with open('downloaded_songs.json','r') as f:
            downloadedSongs=json.load(f)
    except(FileNotFoundError,json.JSONDecodeError):
        downloadedSongs={}
    if query=='spotify':
        user_id=input("Enter your spotify user id ")
        receiver=input("Enter your email: ")
        songs=get_user_tracks(user_id)
        for song in songs:
            songName=unidecode(song)
            if downloadedSongs.get(songName):
                continue
            print(songName)
            video_url=get_data(songName)
            download_track(video_url,songName)
            downloadedSongs[songName]=True
        sendSpotifyPlaylistSongs(songs,receiver)
        with open('downloaded_songs.json','w') as f:
            json.dump(downloadedSongs,f)
        return
    receiver=input("Enter your email: ")
    query=unidecode(query)
    query=capitalize_words(query)
    if downloadedSongs.get(query):
        create_email_and_send(query,receiver)
        return
    video_url=get_data(query)
    print(video_url)
    download_track(video_url,query)
    downloadedSongs[query]=True
    with open('downloaded_songs.json','w') as f:
            json.dump(downloadedSongs,f)
    create_email_and_send(query,receiver)
if __name__=='__main__':
    main()
