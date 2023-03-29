import json
import os
from accessify import private, protected
from googleapiclient.discovery import build
# API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)
class Video():
    """Инициализация реальными данными следующих атрибутов экземпляра класса `Video`:
    - id видео
    - название видео
    - ссылка на видео
    - количество просмотров
    - количество лайков"""

    def __init__(self, video_id):
        self.video_id = video_id #id видео
        self.url = f'https://www.youtube.com/watch?v={self.video_id}'  # ссылка на видео
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=self.video_id).execute()
        self.video_title = video_response['items'][0]['snippet']['title'] #название видео
        self.view_count = video_response['items'][0]['statistics']['viewCount'] #количество просмотров
        self.like_count = video_response['items'][0]['statistics']['likeCount'] #количество лайков
        self.comment_count = video_response['items'][0]['statistics']['commentCount'] #количество лайков

    def __str__(self):
        """Выводит данные в формате: <название_видел>"""
        return self.video_title

class PLVideo():
    """Класс для видео `PLVideo`, который инициализируется 'id видео' и 'id плейлиста'
    > Видео может находиться в множестве плейлистов, поэтому непосредственно из видео через API информацию о
    плейлисте не получить.
    - Реализуйте инициализацию реальными данными следующих атрибутов экземпляра класса `PLVideo`:
    - id видео
    - название видео
    - ссылка на видео
    - количество просмотров
    - количество лайков
    - id плейлиста """

    def __init__(self, video_id, playlist_id):
        self.playlist_id = playlist_id
        playlist_videos = youtube.playlistItems().list(playlistId=self.playlist_id,
                                                       part='contentDetails', maxResults=50,).execute()
        self.video_id = video_id  # id видео
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=self.video_id).execute()
        self.video_title = video_response['items'][0]['snippet']['title'] #название видео
        self.view_count = video_response['items'][0]['statistics']['viewCount'] #количество просмотров
        self.like_count = video_response['items'][0]['statistics']['likeCount'] #количество лайков
        self.comment_count = video_response['items'][0]['statistics']['commentCount'] #количество лайков

    def __str__(self):
        """Выводит данные в формате: <название_видел>"""
        return self.video_title

