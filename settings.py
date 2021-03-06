# -*- coding: utf-8 -*-
# Django settings for basic pinax project.

import os.path
import posixpath
import pinax

PINAX_ROOT = os.path.abspath(os.path.dirname(pinax.__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# tells Pinax to use the default theme
PINAX_THEME = "default"

DEBUG = False
# True
TEMPLATE_DEBUG = DEBUG

# tells Pinax to serve media through the staticfiles app.
SERVE_MEDIA = DEBUG

INTERNAL_IPS = [
    "127.0.0.1",
    "173.3.95.213",
    "24.239.158.133",
]

ADMINS = [
    # ("Boris Raskin", "braskin@playdation.com"),
    # ("Your Name", "your_email@domain.com"),
]

PRODUCTION = True
MANAGERS = ADMINS
DEFAULT_CHARSET = 'utf-8'

DATABASES = {
    "default": {
#        "ENGINE": "django.db.backends.sqlite3", # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "ENGINE": "mysql", # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "NAME":   "playdation",               # Or path to database file if using sqlite3.
        "USER": "playdation",                             # Not used with sqlite3.
        "PASSWORD": "playdate123",                         # Not used with sqlite3.
        "HOST": "",                             # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "",                             # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "US/Eastern"

PIL_IMAGEFILE_MAXBLOCK=1000000

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "site_media", "static")

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = "/static/"

# Additional directories which hold static files
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "media"),
    os.path.join(PINAX_ROOT, "media", PINAX_THEME),
]

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

# Make this unique, and don't share it with anybody.
SECRET_KEY = "cf=fdx8l83kvdkz%2aj0m7qoy60*#fteherztmyy=35bj5=pib"




# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.load_template_source",
    "django.template.loaders.app_directories.load_template_source",
]

MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.middleware.transaction.TransactionMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "account.middleware.LocaleMiddleware",
    "pagination.middleware.PaginationMiddleware",
    "pinax.middleware.security.HideSensistiveFieldsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.csrf.CsrfResponseMiddleware",
    "account.middleware.SiteLogin",
]

ROOT_URLCONF = "playdation.urls"

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
    os.path.join(PINAX_ROOT, "templates", PINAX_THEME),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
#    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    
    "staticfiles.context_processors.static_url",
    
    "pinax.core.context_processors.pinax_settings",
    
    "account.context_processors.account",
    "account.context_processors.analytics_tracking",
    "account.context_processors.user_message_top",

    "notify.context_processors.inbox",
    "announcements.context_processors.site_wide_announcements",
    "notify.context_processors.combined_inbox_count",
]


INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.humanize",
    
    "pinax.templatetags",

    "oembed",    
    # external
    "notify",
    "staticfiles",
    "debug_toolbar",
    "mailer",
    "uni_form",
    "timezones",
    "announcements",
    "pagination",
    "authority",
    
    
    # project
    "signup_codes",
    "analytics",
    "about",
    "profiles",
    "account",
    "friends",
    "contacts_import",
    "emailconfirmation",
    "splash",
    "home",
    "playdates",
    "schools",
    "imagekit",
    "photos",
    "schedule",
    "search",
    "boto",
    "storages",
    "comments",
    "places",
    "error_pages",
    "uploadify",
    "metrics",
    "cachebot",
    "sentry",
    "sentry.client",
    "south",
]

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]


COMBINED_INBOX_COUNT_SOURCES = [
    "notify.context_processors.inbox",
]



MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

ABSOLUTE_URL_OVERRIDES = {
    "auth.user": lambda o: "/profiles/profile/%s/" % o.username,
}

AUTH_PROFILE_MODULE = "profiles.Profile"
NOTIFICATION_LANGUAGE_MODULE = "account.Account"

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_REQUIRED_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = True
ACCOUNT_EMAIL_AUTHENTICATION = True
ACCOUNT_UNIQUE_EMAIL = EMAIL_CONFIRMATION_UNIQUE_EMAIL = False

AUTHENTICATION_BACKENDS = [
    "account.auth_backends.AuthenticationBackend",
]

LOGIN_URL = "/account/login/" # @@@ any way this can be a url name?
LOGIN_REDIRECT_URLNAME = "home"

EMAIL_CONFIRMATION_DAYS = 2
EMAIL_DEBUG = DEBUG

# URCHIN_ID = "ua-..."

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

FB_API_KEY = '*?*?*?*?*?*?*??'
FB_SECRET_KEY = '*?*?*?*?*?'
BASE_URL = "http://www.playdation.net/"

YAHOO_APP_ID='?*?*?*?*'
YAHOO_CONSUMER_KEY='?*?*?*?*?'
YAHOO_CONSUMER_SECRET='?*?*?*?*?*?'

GOOGLE_OAUTH_CONSUMER_KEY='www.playdation.net'
GOOGLE_OAUTH_CONSUMER_SECRET='?*?*?*?*?*?*?*'


OAUTH_SETTINGS = {
    'GOOGLE':{
        'OAUTH_CONSUMER_KEY':'www.playdation.net',
        'OAUTH_CONSUMER_SECRET':'?*?*?*?*?*?'
    }                  
}

OAUTH_ACCESS_SETTINGS = {
    'yahoo':{
             'keys': {
                      'KEY': '*?*?*?*?*?*?*?*?',
                      'SECRET': '*?*?*?*?*?*?*?*?',
                      },
             'endpoints': {
                      'request_token':'https://api.login.yahoo.com/oauth/v2/get_request_token',
                      'access_token':'https://api.login.yahoo.com/oauth/v2/get_token',
                      'authorize':'https://api.login.yahoo.com/oauth/v2/request_auth',                                
                      'provider_scope':'unknown',
                           }
             }
}

BBAUTH_APP_ID = '*?*?*?*?*?*?*?*?*?'
BBAUTH_SHARED_SECRET = '*?*?*?*?*?*?**?*?*'

FB_LOGIN_CANCEL_URL = '/'
FB_LOGIN_NEXT_URL = "/account/acct_fb_auth"
FB_LOGIN_PERMS = 'publish_stream,offline_access'
FB_LOGIN_PERMS_PUBLISH = 'publish_stream'


RELATION_TYPES_DICT = {
    "parent":"P",
    "grandparent":"GP",
    "nanny":"N",
    "caregiver":"C",                                             
}


WWW_HOST = 'www.playdation.net'
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_USE_TLS = True
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'notification@playdation.com'
#EMAIL_HOST_PASSWORD = 'zima1979'
#EMAIL_SUBJECT_PREFIX = '[Playdation] '

SERVER_EMAIL = 'notification@playdation.com'

# DEFAULT_FROM_EMAIL = 'notification@playdation.com'
DEFAULT_FROM_EMAIL = 'Playdation <notification@playdation.com>'

OPENINVITER_USERNAME='berseken'
OPENINVITER_PRIVATE_KEY='**?*?*?*?*?'

# IF true emails the admins in case a user goes for an invalid service
OPENINVITER_MAIL_ADMINS = False


login_cancel_url = BASE_URL

DEFAULT_PROFILE_PHOTO_ID=1
DEFAULT_ALBUM_ID=1

FIRST_DAY_OF_WEEK = 0 # Monday

KISS_ID = '*?*?*?*?'

AWS_ACCESS_KEY_ID = '?*?*?*?*?*?*?'
AWS_SECRET_ACCESS_KEY = '?*?*?*?*?*?*?*?'
AWS_STORAGE_BUCKET_NAME = 'test2bucket'

EMAIL_BACKEND = 'django_ses.SESBackend'
MAILER_EMAIL_BACKEND = 'django_ses.SESBackend'

DEFAULT_SOURCE = 'Direct'
GOOGLE_ANAL_ACCOUNT = 'UA-22901472-1'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
from S3 import CallingFormat
AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN


AWS_HEADERS = {
    'Expires': 'Thu, 15 Apr 2020 20:00:00 GMT',
    'Cache-Control': 'max-age=86400',
}

CACHE_BACKEND = 'cachebot.backends.memcached://127.0.0.1:11211/?timeout=0'


# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from local_settings import *
except ImportError:
    pass


def getattr(key):
    return "nokey"
