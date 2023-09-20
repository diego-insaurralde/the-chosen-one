from flask import render_template, Blueprint, current_app
from src.api import MoviesApi


blp_index = Blueprint("index", __name__)

@blp_index.route("/")
def index():
    mv = MoviesApi(current_app)
    list_movies = mv.get_movies_less_high_votes()
    print(list_movies)
    return render_template("index.html")