import os

class Config(object):
  API_KEY = os.environ.get('API_KEY') or 'nice-try'