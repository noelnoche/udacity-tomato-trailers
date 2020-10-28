#!/usr/bin/env python
"""
This is the file that is invoked to start up a development server. 
It gets a copy of the app from your package and runs it. This won’t be 
used in production.

"""
from trailersweb import app


if __name__ == "__main__":
    app.run()
