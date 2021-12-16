import os
from .settings import *

DEBUG = False

SECRET_KEY = 'wuhtvjn_8*#(99h^w4n5^r9%_b!ub8j#x%=1g&c$he$el@^7w^'
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}