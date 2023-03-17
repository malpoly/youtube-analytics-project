import json
import os
from accessify import private, protected
from googleapiclient.discovery import build
# API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id # id канала
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}' # ссылка на канал
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        for i in channel['items']:
            self.title = i['snippet']['title'] #назание канала
        for i in channel['items']:
            self.video_count = i['statistics']['videoCount'] #количество видео
        for i in channel['items']:
            self.description = i['snippet']['description'] #описание канала
        for i in channel['items']:
            self.view_count = i['statistics']['viewCount'] #количество просмотров
        for i in channel['items']:
            self.subscriber_count = i['statistics']['subscriberCount']  # количество подписчиков

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """класс-метод `get_service()`, возвращающий объект для работы с YouTube API"""
        print(build('youtube', 'v3', developerKey=api_key))

    def to_json(self, name_json):
        """метод `to_json()`, сохраняющий в файл значения атрибутов экземпляра `Channel`"""
        self.name_json = name_json
        self.channel_dict = {'id': self.__channel_id, "ссылка на канал": self.url, 'назание канала': self.title,
                             'количество видео': self.video_count, 'описание канала': self.description,
                             'количество просмотров': self.view_count, 'количество подписчиков': self.subscriber_count}
        json_dict = json.dumps(self.channel_dict, indent=4, ensure_ascii=False)
        with open(self.name_json, 'w', encoding="utf-8") as fp:
            print(json_dict, file=fp)
