from .base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# Base_dir은 최상위 rabbit을 뜻함.

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
DEBUG = False
SECRET_KEY = env('SECRET_KEY')


ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'admin',
        'USER': 'admin',
        'PASSWORD': 'admin1234',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}