""" mock """
from pathlib import Path
import os

from utils.inflect import inflect_engine
from utils.human_ids import humanize
from utils.object_storage import store_public_object

mimes_by_folder = {
    "spreadsheets": "application/CSV",
    "thumbs": "image/jpeg",
    "zips": "application/zip"
}


def set_from_mock(folder, obj, asset_id):
    dir_path = Path(os.path.dirname(os.path.realpath(__file__)))
    collection_name = inflect_engine.plural(obj.__class__.__name__.lower())
    asset_path = dir_path / '..' / 'mock'\
                 / folder / collection_name\
                 / str(asset_id)
    with open(asset_path, mode='rb') as file:
        if folder == "audios":
            obj.save_audio(file.read(), 0)
        elif folder == "thumbs":
            obj.save_thumb(file.read(), 0)
        else:
            store_public_object(folder,
                                collection_name + '/' + humanize(obj.id),
                                file.read(),
                                mimes_by_folder[folder])
    obj.check_and_save_itself()
