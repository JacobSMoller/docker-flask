from flask import Blueprint
from . import route

bp = Blueprint('test', __name__, url_prefix='/test')


@route(bp, '/', methods=['GET'])
def hello_world():
    return 'Hello, World!'
