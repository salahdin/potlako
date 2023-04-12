import os

from django.core.wsgi import get_wsgi_application

os.environ.update(DJANGO_SETTINGS_MODULE="potlako.configs.machine_60")

application = get_wsgi_application()
