"""
This module connects routes and handlers for the application.
"""
from flask import current_app as app
import sqlite3


def connect_db():
    """
    Opens a connection to SQLite database.
    """
    conn = None
    db_path = app.config["DATABASE"]

    try:
        conn = sqlite3.connect(db_path, uri=True)
        print("SQLite3 -- {}".format(sqlite3.version))
    except sqlite3.Error as e:
        msg = "@connect_db -- {}".format(e)
        print(msg)
    finally:
        return conn


def query_movie_data(conn=None, page_num=1):
    """
    Queries data from the table "movies based on page number."

    Args:
        conn (class): sqlite3.Connection.
        page_num (int): Page number for pagination.
    """
    try:
        query = (page_num,)
        c = conn.cursor()
        c.execute("SELECT data FROM movies WHERE page_num=?", query)
        rows = c.fetchall()
        return rows[0][0]

    except sqlite3.Error as e:
        msg = "@read_movie_table -- {}".format(e)
        print(msg)


def query_total_pages(conn=None):
    """
    Queries the number of pagination pages from the table "movies."

    Args:
        conn (class): sqlite3.Connection.
    """
    try:
        c = conn.cursor()
        c.execute("SELECT MAX(page_num) FROM movies")
        rows = c.fetchall()
        return rows[0][0]

    except sqlite3.Error as e:
        msg = "@query_total_pages -- {}".format(e)
        print(msg)  
