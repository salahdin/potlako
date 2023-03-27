# gunicorn.conf.py

import os
SOURCE_ROOT = os.path.expanduser('~/source')

errorlog = os.path.join(SOURCE_ROOT, 'potlako/logs/machine_50-error.log')
accesslog = os.path.join(SOURCE_ROOT, 'potlako/logs/machine_50-access.log')
loglevel = 'debug'
pidfile = os.path.join(SOURCE_ROOT, 'potlako/logs/machine_50.pid')

workers = 2  # the number of recommended workers is '2 * number of CPUs + 1'

raw_env = ['DJANGO_SETTINGS_MODULE=potlako.configs.machine_50']

bind = "127.0.0.1:9015"
