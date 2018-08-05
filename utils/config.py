""" config """
import os
from logging import DEBUG as LOG_LEVEL_DEBUG, INFO as LOG_LEVEL_INFO
from pathlib import Path

FLASK_ROOT_PATH = Path(os.path.dirname(os.path.realpath(__file__))) / '..'
BROWSER_URL = os.environ.get('BROWSER_URL', 'http://localhost:3000')
ENV = os.environ.get('ENV', 'development')
IS_DEV = ENV == 'development'
IS_STAGING = ENV == 'staging'
LOG_LEVEL = LOG_LEVEL_DEBUG if IS_DEV else LOG_LEVEL_INFO

if IS_DEV:
    API_URL = 'localhost'
elif IS_STAGING:
    API_URL = 'http://api-staging.music-pattern.org'
else:
    API_URL = 'http://api.music-pattern.org'

BLOB_SIZE = 80
BLOB_UNREAD_NUMBER = int(BLOB_SIZE/5)
BLOB_READ_NUMBER = int(BLOB_SIZE/5)
