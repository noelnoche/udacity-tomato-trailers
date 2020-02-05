Movie Trailer Website
===


Description
---
This project makes use of Google's YouTube Data API and CustomSearch API to 
obtain the movie data based on a YouTube playlist created by the user, store 
results in a database and serve the results from a webpage served on the Flask 
web framework.


App Link
---



Requirements
---
This project makes use of Google Cloud's YouTube Data and Custom Search API. 
The virtual environment application Pyenv was used in the development of this 
application. Once set up, you can install the required packages from the 
requirements.txt file:

        `$ pip install -r  requirements.txt`


Getting the API key & enabling it
---
1. Log into your Google Cloud Platform console.
2. Click: "Navigation menu" -> "APIs & Services" -> "Library" -> "YouTube Data API v3"
3. Enable the API.
4. Return to "Library" screen and enable "Custom Search API."
5. Click: "Create credentials" -> "Help me choose"
6. Select: "YouTube Data API v(3)" -> Web browser (JavaScript)" -> "Public data"
7. Click: "What credentials do I need"
8. Restrict the key to "Custom Search API" and "YouTube Data API v(3)."
9. Click "Save."


Setup and get CSE key
---
1. Log into your [Google Custom Search Engine console](https://cse.google.com/cse/)
2. Click "New search engine"
3. Under "Sites to search" enter `https://www.imdb.com/title/*`
4. Select "Include just this specific page..."
5. Give the cse a name.
6. In the "Basics" tab enter:
    + Search engine keywords: `movie`
    + Image search: ON
    + Region and language: United States and English
    + Search entire web: OFF


Make playlist and get ID
---
1. Log into your YouTube account.
2. Find a movie trailer (or any video) you like.
3. Click: "Add to" -> "Create new playlist"
4. Give the playlist a name.
5. Privacy setting must be public.
6. Click: Profile icon -> "Your channel"
7. Click the playlist you just created.
8. The playlist id is in the url after the `list` flag.


Running the application (development)
---
1. Open the /scripts/dev_config.py in a text editor and provide the values.
2. Open Terminal in the application root directory.
3. `python scripts/db_setup.py` (Creates a new movies database in trailersweb directory)
4. `export FLASK_ENV=development`
5. `export FLASK_APP=run.py`
6. `flask run --no-reload`
7. Open browser: `localhost:5000/trailersweb`


Credits
---
Trailers are taken from [YouTube Movies](https://www.youtube.com/movies)


License
---
Code provided under an [MIT license](https://github.com/noelnoche/udacity-fsnd-movie-trailer-website/blob/gh-pages/LICENSE.md)


Reference
---
+ [Pyenv](https://github.com/pyenv/pyenv)
+ [Getting Started with YouTube Data API](https://developers.google.com/youtube/v3/getting-started)
+ [Creating a Google Custom Search Engine](https://developers.google.com/custom-search/json-api/v1/introduction)
+ [Flask](http://flask.palletsprojects.com/en/1.1.x/)
+ [sqlite3](https://docs.python.org/3/library/sqlite3.html)
