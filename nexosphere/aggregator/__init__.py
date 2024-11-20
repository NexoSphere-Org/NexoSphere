from flask import Blueprint

bp = Blueprint('aggregator', __name__)

from nexosphere.aggregator import routes