from app import app, cursor
from app.controllers.category_controller import category_controller

from flask import request

from app.utils import build_response

# Category user route

@app.route('/categories', methods=['GET'])
def category_handle():
    return category_controller.all()
