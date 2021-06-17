import os 
from .base import *
from .installed import *

HOME_PAGE_MSG = "HELLO WORLD. THIS IS LOCAL."
print("Using local.py")

#Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
