import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

@pytest.fixture
def category_id():
    client = app.test_client()
    response = client.get('/categories')
    categories = response.get_json()['data']
    return categories[0]['id']

@pytest.fixture
def context():
    app.config['TESTING'] = True
    client = app.test_request_context()

    yield client

@pytest.fixture
def user_id(category_id):
    client = app.test_client()
    response = client.post('/register', json={
        'name': 'teste',
        'email': 'teste@teste.com',
        'category': category_id
    })

    return response.get_json()['data']
