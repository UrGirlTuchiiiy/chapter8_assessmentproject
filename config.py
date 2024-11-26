import os


class Config(object):
    """Define app configurations"""
    SECRET_KEY = os.environ.get('SECET_KEY') or 'hard-to-guess'
   