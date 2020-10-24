import functools

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for, 
    make_response, 
    jsonify
)
from backend_app.db import get_db

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/create", methods=["OPTIONS", "POST"])
def create():
    print(request.method)
    if request.environ["HTTP_ORIGIN"] is not None:
        print("HTTP_ORIGIN in request.environ is {}".format(request.environ["HTTP_ORIGIN"]))
    if request.method == "OPTIONS":
        print("request method is OPTIONS")
        return build_preflight_response()
    if request.method == "POST":
        book_id = request.get_json()["bookID"]
        book_title = request.get_json()["bookTitle"]
        book_author = request.get_json()["bookAuthor"]
        
        error = None
        if error is None:
            db = get_db()
            db.execute(
                "INSERT INTO Book (BookId, BookTitle, BookAuthor) VALUES (?, ?, ?)",
                (book_id, book_title, book_author),
            )
            db.commit()
            return build_actual_response(make_response(jsonify(success=True)))
        flask(error)

def build_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response

def build_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response