from django.core.management import setup_environ
import sys

sys.path.append('/var/www/playdation.net')
sys.path.append('/var/www/playdation.net/playdation')
sys.path.append('/var/www/playdation.net/playdation/apps')

from playdation import settings

setup_environ(settings)

from django.db import connection
from django import db

from mydebug import * 

from models import MessagePreference, MessagePreferenceDefaults, Update, InternalMessage, Email, FBPost, create_message_content, create_message, get_message_content, inbox_count_for, create_update, send_email
from profiles.models import Child
from django.contrib.auth.models import User
import time


u = InternalMessage.objects.filter(recipient=83)

c = len(u.all())

print c
