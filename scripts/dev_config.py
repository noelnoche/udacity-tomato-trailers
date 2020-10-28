"""
This file contains configuration variables for db_setup.py. passwords. 
DO NOT upload this file onto the production server. Use this for local 
development only.

API calls require a Google Cloud Platform API key, YouTube playlist ID
and a Google Custom Search Engine ID (cx):

    Attributes:
        API_KEY = "Your Google Cloud API key"
        PLAYLIST_ID = "Your YouTube playlist ID"
        CSE_ID="Your Google Custom Search Engine ID"
        LIMIT="Number of items shown at a time"
"""

secret = dict(
    API_KEY = "xxx",
    PLAYLIST_ID = "xxx",
    CSE_ID = "xxx"
)

envar = dict(
    LIMIT = 5
)
