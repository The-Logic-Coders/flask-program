import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    
    SECRET_KEY = b'\xb8k\xa6\xf7C\xc1%\xf5\x87\x00\x01\xaf)SR\xa3'
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'app.db')