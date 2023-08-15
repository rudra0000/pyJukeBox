import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()
API=os.getenv('API')
print(f'API is {API}')
BASE_URL='https://www.googleapis.com/youtube/v3/search?q='
def get_data(query):
    query+=' song'
    URL=f'{BASE_URL}{query}&key={API}&part=snippet'
    resp=requests.get(URL)
    result=resp.json()
    print(result)
    video=result['items'][0]['id']['videoId']
    videoURL=f'https://www.youtube.com/watch?v={video}'
    return videoURL
 
# query=input()+' song'
# print(query)
# print(get_data(query))
