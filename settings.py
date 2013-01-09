# Django settings for testing123 project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pydj',                      # Or path to database file if using sqlite3.
        'USER': 'pydj',                      # Not used with sqlite3.
        'PASSWORD': 'trollface',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3fb5ry-1+ukj07pbw%gbr1&amp;omtxtoqzhdg7s-8nqfgfp7e&amp;005'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pydj.urls'

# Python dotted path to the WSGI application used by Django's runserver.
#WSGI_APPLICATION = 'pydj.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'pydj.playlist',
    'django.contrib.markup',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

AUTH_PROFILE_MODULE = 'playlist.UserProfile'
LOGIN_REDIRECT_URL = '/playlist'
LOGIN_URL = '/login'
TEMPLATE_CONTEXT_PROCESSORS = (
     "django.contrib.auth.context_processors.auth",
     "django.core.context_processors.debug",
     "django.core.context_processors.i18n",
     "django.core.context_processors.media",
     "django.contrib.messages.context_processors.messages",
     'playlist.context.listenersContextProcessor',
     'playlist.context.newReportsContextProcessor',
     'playlist.context.newEditsContextProcessor',
     'playlist.context.positionContextProcessor',
     'playlist.context.commentProcessor',
     'playlist.context.nowPlayingContextProcessor',
     'playlist.context.SQLLogContextProcessor',
     'playlist.context.siteContext',
      )

IMAGES_DIR = '/home/phuzion/Code/pydj/playlist/images'
LOGIC_DIR = '/home/phuzion/Code/pydj/playlist/logic'
SHOW_QUERIES = 'FALSE'
ICES_CONF = '/home/phuzion/Code/pydj/playlist/logic/ices.conf'
STREAMINFO_URL = 'http://localhost/info.pls'
# ^^^^^^^^^^^^^^^^^^^^^^ This needs changed ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
NEXT_PASSWORD = 'asdc98asdcn1csdcai7qlkdlkdsa8ekq'
MAX_UPLOAD_SIZE = '15728640'
MAX_SONG_LENGTH = '480'
PLAYLIST_MAX = '5'
PLAYLIST_SOFT_TIME_LIMIT = '360'
REPLAY_INTERVAL = '1'
IS_LIVE = 'FALSE'
FILE_UPLOAD_MAX_MEMORY_SIZE = '0'
SET_TITLE = 'SYNHAK.FM'
SITE_TITLE = 'SYNHAK.FM'
LISTEN_URL = 'localhost.test/listen.pls'
DEAD_AIR_TRACK = '/home/phuzion/Code/pydj/playlist/logic/bees.mp3'
