import requests
from bs4 import BeautifulSoup
import json
API='AIzaSyC0O6p6BhEG4ym-mI0dWWSjnW4voL-F_Dc'
BASE_URL='https://www.googleapis.com/youtube/v3/search?q='
def get_data(query):
    query+=' song'
    URL=f'{BASE_URL}{query}&key={API}&part=snippet'
    resp=requests.get(URL)
    result=resp.json()
    video=result['items'][0]['id']['videoId']
    videoURL=f'https://www.youtube.com/watch?v={video}'
    return videoURL
 
# query=input()+' song'
# print(query)
# print(get_data(query))
