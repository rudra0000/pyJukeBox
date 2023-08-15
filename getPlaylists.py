from dotenv import load_dotenv
import os
import base64
from requests import post
import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
load_dotenv()
CLIENT_ID=os.getenv('CLIENT_ID')
CLIENT_SECRET=os.getenv('CLIENT_SECRET')

def get_token():
    auth_string=f'{CLIENT_ID}:{CLIENT_SECRET}'
    auth_bytes=auth_string.encode('utf-8')
    auth_base64=str(base64.b64encode(auth_bytes),'utf-8')
    URL='https://accounts.spotify.com/api/token'
    headers={
        'Authorization':'Basic '+auth_base64,
        'Content-Type':'application/x-www-form-urlencoded'
    }
    data={'grant_type':'client_credentials'}
    result=post(URL,headers=headers,data=data)
    json_result=json.loads(result.content)
    token=json_result.get('access_token')
    return token
#prints songs of a playlist
def get_songs_of_playlists(token,playlist_id):
    URL=f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    header={'Authorization':f'Bearer {token}'}
    resp=requests.get(URL,headers=header)
    result=resp.json()
    songs_list=[]
    for elem in result['items']:
        songs_list.append(elem['track']['name'])
    return songs_list
   
def get_user_playlists(token,user_id):
    URL=f'https://api.spotify.com/v1/users/{user_id}/playlists'
    headers={'Authorization':f'Bearer {token}',
            'Content-Type':'application/json'}
    resp=requests.get(URL,headers=headers)
    data=resp.json()
    playlists_id=[]
    for elem in data['items']:
        playlists_id.append(elem['id'])
    return playlists_id

def get_user_tracks(user_id):
    token=get_token()
    songs=[]
    # user_id='31yhjd7ntfspdgdx5uxhcl4pnjny'
    playlists=get_user_playlists(token,user_id)
    for playlist in playlists:
        songs.extend(get_songs_of_playlists(token,playlist))
    return songs
