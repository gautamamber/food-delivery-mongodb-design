from mongoengine import connect
from django.conf import settings

connect(
    db=settings.MONGODB_SETTINGS['db'],
    host=settings.MONGODB_SETTINGS['host'],
    port=settings.MONGODB_SETTINGS['port']
)
