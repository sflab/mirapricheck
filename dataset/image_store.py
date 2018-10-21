from common import Event
import urllib.request
from abc import ABCMeta, abstractmethod


class ImageStore:
    def load(self, loadable_image):


class ImageHolder:
    def __init__(self, loadable_image):
        loadable_image.loaded_event += self.__set

    def get(self):

    def __set(self, id, image_data):
        self.__image_data = image_datas

class LoadableImage:
    __metaclass__ = ABCMeta

    def __init__(self, id):
        self.__id = id
        self.loaded_event = Event()

    def id(self):
        return self.__id

    def load(self):
        data = self._load_internal()
        self.loaded_event(self.id(), data)

    @abstractmethod
    def _load_internal(self):
        pass


class WebImage(LoadableImage):

    def __init__(self, url):
        self.__url = url

    def _load_internal(self):
        try:
            with urllib.request.urlopen(self.__url) as response:
                if 200 <= response.status <= 299:
                    return response.read()
                else:
                    return None
        except:
            return None
