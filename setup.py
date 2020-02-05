"""
This script is the center of all activity in building, distributing, and 
installing modules using the Distutils. The main purpose of the setup script is
to describe your module distribution to the Distutils, so that the various 
commands that operate on your modules do the right thing. However, in this 
case, it is used simply to hold application metadata.
"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


CONFIG = {
    "name": "trailersweb",
    "description": ("Dynamically generates a movie trailer website using "
        "YouTube playlist data."),
    "version": "2.0.0.dev",
    "url": "https://github.com/noelnoche/udacity-fsnd-movie-trailer-website",
    "download_url": 
        ("https://github.com/noelnoche/udacity-fsnd-movie-trailer-website"),
    "author": "Noel Noche",
    "author_email": "contact@hellonoel.com",
    "packages": ["trailersweb"],
    "license": "MIT",
    "zip_safe": False
}

setup(**CONFIG)
