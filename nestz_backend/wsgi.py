"""
WSGI config for nestz_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nestz_backend.settings')
project_folder = os.path.expanduser(
    '~/main/NestZ/nestz_backend/')
load_dotenv(os.path.join(project_folder, '.env'))

application = get_wsgi_application()
