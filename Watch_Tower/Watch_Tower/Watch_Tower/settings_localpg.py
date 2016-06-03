from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'herosandwich',
        'USER': 'herosandwich_user',
        'PASSWORD': 'thebestpassword',
        'HOST': '',
        'PORT': '',
    }
}
