from mock.routes import data_analyst, data_client, data_ticket_long, data_ticket_short
from app.utils.format import is_valid_uuid

def test_ping_pong(client):
    response = client.get('/ping')
    assert response.status_code == 200
    data = response.get_json()
    assert data['pong'] == True


def test_get_categories(client):
    response = client.get('/categories')
    assert response.status_code == 200
    data = response.get_json()
    assert type(data['data']) == type([])
    category1, category2, *rest = data['data']
    assert len(data['data']) > 0
    assert 'id' in category1
    assert 'name' in category1
    assert category1['name'] == 'analyst'
    assert category2['name'] == 'client'
    data_analyst['category'] = category1['id']
    data_client['category'] = category2['id']


def test_regiser_client(client):
    response = client.post('/register', json={**data_client})
    assert response.status_code == 201
    data = response.get_json()
    user_id = data['data']
    assert user_id in data['data']
    assert is_valid_uuid(user_id)
    data_client['id'] = user_id


def test_regiser_analyst(client):
    global id_category_analyst
    response = client.post('/register', json={**data_analyst})
    assert response.status_code == 201
    data = response.get_json()
    user_id = data['data']
    assert user_id in data['data']
    assert is_valid_uuid(user_id)
    data_analyst['id'] = user_id


def test_login_client(client):
    response = client.post('/login', json={ "user_id": data_client['id']})
    assert response.status_code == 200
    data = response.get_json()
    token = data['data']
    assert token in data['data']
    data_client['token'] = token


def test_login_analyst(client):
    response = client.post('/login', json={ "user_id": data_analyst['id'] })
    assert response.status_code == 200
    data = response.get_json()
    token = data['data']
    assert token in data['data']
    data_analyst['token'] = token


def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    data = response.get_json()
    assert type(data['data']) == type([])
    user, *rest = data['data']
    assert len(data['data']) > 0
    assert 'id' in user
    assert 'name' in user
    assert 'email' in user
    assert 'category_id' in user
    if user['category_name'] == 'client':
        assert user['ranking'] == None
        assert user['category_id'] == data_client['category']
    else:
        assert user['ranking'] == 'D'
        assert user['category_id'] == data_analyst['category']


def test_get_user(client):
    response = client.get(f'/user/{data_analyst["id"]}')
    assert response.status_code == 200
    user = response.get_json()['data']
    assert 'id' in user
    assert 'name' in user
    assert 'email' in user
    assert user['category_id'] == data_analyst['category']
    assert user['ranking'] == 'D'
    assert user['name'] == data_analyst['name']
    assert user['id'] == data_analyst['id']


def test_get_myself(client):
    headers = {'Authorization': f'Bearer {data_client["token"]}'}
    response = client.get(f'/user', headers=headers)
    assert response.status_code == 200
    user = response.get_json()['data']
    assert 'id' in user
    assert 'name' in user
    assert 'email' in user
    assert user['category_id'] == data_client['category']
    assert user['ranking'] is None
    assert user['name'] == data_client['name']
    assert user['id'] == data_client['id']


def test_post_ticket_long(client):
    headers = {'Authorization': f'Bearer {data_client["token"]}'}
    response = client.post('/ticket', json={**data_ticket_long}, headers=headers)
    assert response.status_code == 201
    ticket_id = response.get_json()['data']
    assert is_valid_uuid(ticket_id)
    data_ticket_long['id'] = ticket_id
    response_ticket = client.get(f'/ticket/{ticket_id}', headers=headers)
    ticket = response_ticket.get_json()['data']
    assert ticket['status_name'] == 'pending'
    assert ticket['client_id'] == data_client['id']


def test_post_ticket_short(client):
    headers = {'Authorization': f'Bearer {data_client["token"]}'}
    response = client.post('/ticket', json={**data_ticket_short}, headers=headers)
    assert response.status_code == 201
    ticket_id = response.get_json()['data']
    assert is_valid_uuid(ticket_id)
    data_ticket_short['id'] = ticket_id
    response_ticket = client.get(f'/ticket/{ticket_id}', headers=headers)
    ticket = response_ticket.get_json()['data']
    assert ticket['status_name'] == 'pending'
    assert ticket['client_id'] == data_client['id']


def test_put_client_closed_ticket_short(client):
    headers = {'Authorization': f'Bearer {data_client["token"]}'}
    response = client.put(f'/ticket/close/{data_ticket_short["id"]}', headers=headers)
    data = response.get_json()
    assert response.status_code == 200
    assert data['data'] is None
    assert data['message'] == f'the ticket {data_ticket_short["id"]} was closed'
    response_ticket = client.get(f'/ticket/{data_ticket_short["id"]}', headers=headers)
    ticket = response_ticket.get_json()['data']
    assert ticket['status_name'] == 'closed'
    assert ticket['closed_by'] == data_client["id"]


def test_put_analyst_taken_ticket_long(client):
    headers = {'Authorization': f'Bearer {data_analyst["token"]}'}
    response = client.put(f'/ticket/next-step/{data_ticket_long["id"]}', headers=headers)
    data = response.get_json()
    assert response.status_code == 200
    assert data['data'] is None
    assert data['message'] == 'analyst changed the ticket for review'
    response_ticket = client.get(f'/ticket/{data_ticket_long["id"]}', headers=headers)
    ticket = response_ticket.get_json()['data']
    assert ticket['status_name'] == 'review'


def test_put_client_solved_ticket_long(client):
    headers = {'Authorization': f'Bearer {data_client["token"]}'}
    response = client.put(f'/ticket/next-step/{data_ticket_long["id"]}', headers=headers)
    data = response.get_json()
    assert response.status_code == 200
    assert data['data'] is None
    assert data['message'] == 'client changed the ticket for solved'
    response_ticket = client.get(f'/ticket/{data_ticket_long["id"]}', headers=headers)
    ticket = response_ticket.get_json()['data']
    assert ticket['status_name'] == 'solved'

def test_put_analyst_closed_ticket_long(client):
    headers = {'Authorization': f'Bearer {data_analyst["token"]}'}
    response = client.put(f'/ticket/next-step/{data_ticket_long["id"]}', headers=headers)
    data = response.get_json()
    assert response.status_code == 200
    assert data['data'] is None
    assert data['message'] == f'the ticket {data_ticket_long["id"]} was closed'
    response_ticket = client.get(f'/ticket/{data_ticket_long["id"]}', headers=headers)
    ticket = response_ticket.get_json()['data']
    assert ticket['status_name'] == 'closed'
    assert ticket['closed_by'] == data_analyst["id"]


def test_get_tickets(client):
    headers = {'Authorization': f'Bearer {data_client["token"]}'}
    response = client.get('/tickets', headers=headers)
    tickets = response.get_json()['data']
    assert response.status_code == 200
    assert type(tickets) == type([])
    assert len(tickets) > 0


def test_get_ticket(client):
    headers = {'Authorization': f'Bearer {data_client["token"]}'}
    response = client.get(f'/ticket/{data_ticket_short["id"]}', headers=headers)
    ticket = response.get_json()['data']
    assert response.status_code == 200
    assert 'client_id' in ticket
    assert 'title' in ticket
    assert 'analyst_id' in ticket
    assert ticket['client_id'] == data_client['id']
    assert ticket['title'] == data_ticket_short['title']
    assert ticket['analyst_id'] is None


