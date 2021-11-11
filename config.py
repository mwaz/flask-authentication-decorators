import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'api.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'd9874b1c9d7d19b255c72a8096ecbd331f6885e9'

class TestingConfig(Config):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'test_api.db')
    TESTING = True
class StagingConfig(Config):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'staging_api.db')


app_config = {
    'testing': TestingConfig,
    'staging': StagingConfig,
    'default': Config
}
