import os
from urllib.parse import urlparse


DEBUG = False
ALLOWED_HOSTS = ['https://notifier896.herokuapp.com']
SECRET_KEY = os.environ.get('SECRET_KEY', 'arun')  


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500