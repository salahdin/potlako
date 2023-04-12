import os

from django.core.wsgi import get_wsgi_application

os.environ.update(DJANGO_SETTINGS_MODULE="potlako.configs.machine_91")

application = get_wsgi_application()
