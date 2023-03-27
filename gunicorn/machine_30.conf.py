# gunicorn.conf.py

import os
SOURCE_ROOT = os.path.expanduser('~/source')

errorlog = os.path.join(SOURCE_ROOT, 'potlako/logs/machine_30-error.log')
accesslog = os.path.join(SOURCE_ROOT, 'potlako/logs/machine_30-access.log')
loglevel = 'debug'
pidfile = os.path.join(SOURCE_ROOT, 'potlako/logs/machine_30.pid')

workers = 2  # the number of recommended workers is '2 * number of CPUs + 1'

raw_env = ['DJANGO_SETTINGS_MODULE=potlako.configs.machine_30']

bind = "127.0.0.1:9013"
