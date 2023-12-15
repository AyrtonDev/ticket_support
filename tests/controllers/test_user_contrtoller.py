from uuid import uuid4
from app.controllers.user_controller import user_controller
from unittest.mock import patch

def test_get_all_users_success(context):
    with context:
        response = user_controller.all()
        data = response.get_json()

        assert response.status_code == 200
        assert data['data'] is not None
        assert len(data['data']) > 0
        assert data['message'] == ''

# def test_get_myself_user_success(context, user_id):
#     with context:
#         with patch('flask.g', {'user_id': user_id}):
#             response = user_controller.myself()
#             data = response.get_json()
#             user = data['data']

#             assert response.status_code == 200
#             # assert data['data'] is not None
#             print(data)
#             assert data['message'] == ''
#             assert user['id'] == user_id

def test_one_user_empty(context):
    with context:
        response = user_controller.one('')
        data = response.get_json()

        assert response.status_code == 403
        assert data['data'] is None
        assert data['message'] == 'user id is required in url'

def test_one_user_invalid(context):
    with context:
        response = user_controller.one('dawdwadawdw')
        data = response.get_json()

        assert response.status_code == 400
        assert data['data'] is None
        assert data['message'] == 'user id is invalid'

def test_one_user_not_found(context):
    with context:
        response = user_controller.one(f'{uuid4()}')
        data = response.get_json()

        assert response.status_code == 404
        assert data['data'] is None
        assert data['message'] == 'user not found'

def test_get_one_user_success(context, user_id):
    with context:
        response = user_controller.one(user_id)
        data = response.get_json()
        user = data['data']

        assert response.status_code == 200
        assert data['data'] is not None
        assert data['message'] == ''
        assert user['id'] == user_id
