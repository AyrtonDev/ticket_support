from typing import NamedTuple
from uuid import UUID

class User(NamedTuple):
    id: UUID
    name: str
    email: str
    category_id: UUID
    cateforu_name: str
    ranking: str | None

post_client_query = 'INSERT INTO users (username, email, category_id) VALUES(%(name)s, %(email)s, %(category)s) RETURNING user_id'

post_analyst_query = 'INSERT INTO users (username, email, category_id, ranking) VALUES(%(name)s, %(email)s, %(category)s, %(ranking)s) RETURNING user_id'

get_users_query = 'SELECT users.*, categories.category_name AS category_name FROM users LEFT JOIN categories ON categories.category_id = users.category_id'

delete_user_query = 'DELETE FROM users WHERE user_id = %s'
