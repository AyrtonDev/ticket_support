from app import app
from app.controllers.auth_controller import auth_controller
from app.controllers.category_controller import category_controller
from app.controllers.user_controller import user_controller

# Category user route

@app.route('/categories', methods=['GET'])
def category_handle():
    return category_controller.all()

# Auth routes

@app.route('/register', methods=['POST'])
def register_user_handle():
    return auth_controller.create()

# User routes

@app.route('/users', methods=['GET'])
def get_users_handle():
    return user_controller.all()

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user_handle(user_id):
    return user_controller.delete(user_id)
