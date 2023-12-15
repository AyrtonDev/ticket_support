import uuid
from app.controllers.auth_controller import auth_controller

valid_user_id = None

def test_body_empty_register(context):
    with context:
        error = auth_controller.register({})
        data = error.response.get_json()

        assert error.response.status_code == 400
        assert data['data'] is None
        assert 'the body is empty' == data['message']

def test_name_empty_register(context):
    with context:
        error = auth_controller.register({ 'email': 'teste'})
        data = error.get_json()

        assert error.status_code == 403
        assert data['data'] is None
        assert 'Name is required' == data['message']

def test_email_empty_register(context):
    with context:
        error = auth_controller.register({ 'name': 'teste'})
        data = error.get_json()

        assert error.status_code == 403
        assert data['data'] is None
        assert 'E-mail is required' == data['message']

def test_email_invalid_register(context):
    with context:
        error = auth_controller.register({ 'name': 'teste', 'email': 'teste'})
        data = error.get_json()

        assert error.status_code == 400
        assert data['data'] is None
        assert 'E-mail is invalid' == data['message']

def test_category_empty_register(context):
    with context:
        error = auth_controller.register({ 'name': 'teste', 'email': 'teste@teste.com'})
        data = error.get_json()

        assert error.status_code == 403
        assert data['data'] is None
        assert 'Category is required' == data['message']

def test_category_invalid_register(context):
    with context:
        error = auth_controller.register({ 'name': 'teste', 'email': 'teste@teste.com', 'category': 'dadwadawdasdawd'})
        data = error.get_json()

        assert error.status_code == 400
        assert data['data'] is None
        assert 'Category is invalid' == data['message']

def test_register_success(context, category_id):
    with context:
        response = auth_controller.register({ 'name': 'teste', 'email': 'teste@teste.com', 'category': category_id})
        data = response.get_json()

        assert response.status_code == 201
        assert data['data'] is not None
        global valid_user_id
        valid_user_id = data['data']

def test_user_id_empty_login(context):
    with context:
        response = auth_controller.login('')
        data = response.get_json()

        assert response.status_code == 403
        assert data['data'] is None
        assert data['message'] == 'user_id is required'

def test_user_id_invalid_login(context):
    with context:
        response = auth_controller.login({ 'user_id':'dadwdaddawdwadaw'})
        data = response.get_json()

        assert response.status_code == 400
        assert data['data'] is None
        assert data['message'] == 'user_id is invalid'

def test_user_not_found_login(context):
    with context:
        response = auth_controller.login({ 'user_id': f'{uuid.uuid4()}'})
        data = response.get_json()

        assert response.status_code == 404
        assert data['data'] is None
        assert data['message'] == 'user not found'

def test_user_login_success(context):
    with context:
        global valid_user_id
        response = auth_controller.login({ 'user_id':valid_user_id})
        data = response.get_json()

        assert response.status_code == 200
        assert data['data'] is not None
        assert data['message'] == ''
