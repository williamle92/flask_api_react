from flask import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api')

from . import routes, tokens
from app.blueprints.product.models import Products