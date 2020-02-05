"""
This module connects routes and handlers for the application.
"""
from flask import abort
from flask import Blueprint
from flask import current_app as app
from flask import g
from flask import make_response
from flask import render_template
from jinja2 import TemplateNotFound
from trailersweb.cache import cache
from trailersweb.db_engine import connect_db
from trailersweb.db_engine import query_movie_data
from trailersweb.db_engine import query_total_pages


bp_views = Blueprint("bp_views", __name__, template_folder="templates")


def open_db():
    """
    Invokes database connection and holds the connection in the 
    application context via the global (g) object.
    https://flask.palletsprojects.com/en/1.1.x/appcontext/
    """
    if 'db' not in g:
        g.db = connect_db()
        print("DB OPEN")
    return g.db

@app.teardown_appcontext
def teardown_db(e):
    """
    Closes connection and deallocates resources when the application
    context is popped.
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()
        print("DP CLOSED")


@bp_views.route("/")
@bp_views.route("/<int:page_num>")
@cache.cached()
def serve_page(page_num=1):
    """
    Handler for application pages.

    Args:
        page_num (int): Page number (if pagination active).
    """
    prev_page = None
    next_page = None

    conn = open_db()
    total_pages = query_total_pages(conn)

    if page_num > 1 and page_num <= total_pages:
        prev_page = page_num - 1
    if page_num < total_pages:
        next_page = page_num + 1
    if page_num > total_pages:
        abort(404)

    movie_tiles = query_movie_data(conn, page_num)

    try:
        resp = make_response(render_template("main.html", 
            movie_tiles=movie_tiles, page_num=page_num, 
            total_pages=total_pages, prev_page=prev_page, 
            next_page=next_page))
        resp.headers["Cache-Control"] = ("max-age=518400, must-revalidate, "
            "public")
        return resp
    except TemplateNotFound:
        abort(404)
