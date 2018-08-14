""" has audio mixin """
import requests
from sqlalchemy import Column,\
                       Integer

from models.utils import Wrapper
from utils.human_ids import humanize
from utils.inflect import inflect_engine
from utils.object_storage import delete_public_object,\
                                 get_public_object_date,\
                                 store_public_object

class HasAudioMixin(object):
    audioCount = Column(Integer(), nullable=False, default=0)

    def delete_audio(self, index):
        delete_public_object("audios", self.audio_storage_id(index))

    def audio_date(self, index):
        return get_public_object_date("audios", self.audio_storage_id(index))

    def audio_storage_id(self, index):
        if self.id is None:
            raise ValueError("Trying to get audio_storage_id for an unsaved object")
        return inflect_engine.plural(self.__class__.__name__.lower()) + "/"\
                                     + humanize(self.id)\
                                     + (('_' + str(index)) if index > 0 else '')

    def save_audio(self, audio, index):
        content_type = "application/octet-stream"
        if isinstance(audio, str):
            if not audio[0:4] == 'http':
                raise ValueError('Invalid audio URL for object '
                                 + str(self)
                                 + ' : ' + audio)
            audio_response = requests.get(audio)
            content_type = audio_response.headers['Content-type']
            print('content_type', content_type)
            if audio_response.status_code == 200:
                audio = audio_response.content
            else:
                raise ValueError('Error downloading audio for object '
                                 + str(self)
                                 + ' status_code: ' + str(audio_response.status_code))
        store_public_object("audios",
                            self.audio_storage_id(index),
                            audio,
                            content_type)
        self.audioCount = max(index + 1, self.audioCount or 0)
        print(self, self.audioCount)
        Wrapper.check_and_save(self)
