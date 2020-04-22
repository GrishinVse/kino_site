<<<<<<< HEAD
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SEKRET_KEY') or 'YOU-SHALL-NOT-PASS'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'appd.db')
=======
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SEKRET_KEY') or 'YOU-SHALL-NOT-PASS'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'appd.db')
>>>>>>> 85d6b8ea0501ed3d4ece54d28aa109f945ee3ccb
    SQLALCHEMY_TRACK_MODIFICATIONS = False