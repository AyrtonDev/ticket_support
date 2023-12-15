from app import app
from app.middlewares.validations import validate

from app.controllers.auth_controller import auth_controller
from app.controllers.category_controller import category_controller
from app.controllers.user_controller import user_controller
from app.controllers.ticket_controller import ticket_controller

# Category user route

@app.route('/categories')
def category_handle():
    return category_controller.all()

# Auth routes

@app.route('/register', methods=['POST'])
def register_user_handle():
    return auth_controller.register()

@app.route('/login', methods=['POST'])
def login_user_handle():
    return auth_controller.login()

# User routes

@app.route('/users')
def get_users_handle():
    return user_controller.all()

@app.route('/user')
@validate.token
def get_myself_handle():
    return user_controller.myself()

@app.route('/user/<user_id>')
def get_user_handle(user_id):
    return user_controller.one(user_id)

# Ticket routes

@app.route('/ticket', methods=['POST'])
@validate.token
def create_ticket_handle(*args, **kwargs):
    return ticket_controller.create()

@app.route('/tickets')
@validate.token
def get_tickets_handle():
    return ticket_controller.all()

@app.route('/ticket/<ticket_id>', methods=['GET'])
@validate.token
def get_ticket_handle(ticket_id):
    return ticket_controller.one(ticket_id)

@app.route('/ticket/next-step/<ticket_id>', methods=['PUT'])
@validate.token
def put_ticket_handle(ticket_id):
    return ticket_controller.next(ticket_id)

@app.route('/ticket/close/<ticket_id>', methods=['PUT'])
@validate.token
def put_close_ticket_handle(ticket_id):
    return ticket_controller.close(ticket_id)
