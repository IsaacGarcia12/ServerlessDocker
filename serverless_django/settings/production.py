import os 
from .base import *
from .installed import *

HOME_PAGE_MSG = "HELLO WORLD. THIS IS PRODUCTION."
print("Using local.py")

ALLOWED_HOSTS = ['*']
DEBUG = False
SECRET_KEY = os.environ.get("SECRET_KEY",'django-insecure-l$7%apv4-=2x4*_ess_79%j35tt+fg^=-lzta(pz((x6&i3v7(')
#Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
import os 
from .base import *
from .installed import *

print("Using production.py")

#Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'prod.sqlite3',
    }
}
