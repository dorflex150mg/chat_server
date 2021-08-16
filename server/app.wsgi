#! /usr/bin/python3


import logging
import sys

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/src')
from my_flask_app import app as application
application.secret_key = ('chat')

