"""
This file contains most of the app configuration variables.
"""
import os

class Config(object):
    DEBUG = False
    TESTING = False
    ROOT_DIR = os.getcwd()

    # Since the database for this application does not store user 
    # input, we make it read-only (more secure)
    # SQLite has encryption options available but requires a licence 
    # and not needed for an application this small
    DATABASE = "file:{}/movies.db?mode=ro".format(ROOT_DIR)

class ProductionConfig(Config):
    SECRET_KEY = os.urandom(24)
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = "dev"

class TestingConfig(Config):
    TESTING = True
