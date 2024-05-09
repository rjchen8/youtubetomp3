from dotenv import load_dotenv, find_dotenv
import requests
import os
from googleapiclient.discovery import build

load_dotenv(find_dotenv())
rapidapi_key = os.environ.get("RAPIDAPI_KEY")
youtubeapi_key = os.environ.get("YOUTUBEAPI_KEY")


def getDownloadLink(link):
    params = {
        "url": link,
        "format": "mp3"
    }

    headers = {
        "content-type": "application/json",
	    "X-RapidAPI-Key": rapidapi_key,
	    "X-RapidAPI-Host": "youtube-to-mp315.p.rapidapi.com"
    }
    
    response = requests.post("https://youtube-to-mp315.p.rapidapi.com/download", json={}, headers=headers, params=params)
    
    return {'download_url': response.json().downloadUrl, 'id': response.json().id}


def getVideoInfo(link):
    video_id = link.split('watch?v=')[1]
    
    youtube = build(
        'youtube',
        'v3',
        developerKey=youtubeapi_key,
    )

    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )

    response = request.execute()

    publish_date = response['items'][0]['snippet']['publishedAt']
    title = response['items'][0]['snippet']['title']
    tb_link = response['items'][0]['snippet']['thumbnails']['high']['url']

    return {'publish_date': publish_date, 'title': title, 'tb_link': tb_link}