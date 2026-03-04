import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
from django.conf import settings
print('DIRS:', settings.TEMPLATES[0]['DIRS'])
