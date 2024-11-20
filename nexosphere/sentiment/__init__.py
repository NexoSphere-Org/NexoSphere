from flask import Blueprint

bp = Blueprint('sentiment', __name__)

from nexosphere.sentiment import routes