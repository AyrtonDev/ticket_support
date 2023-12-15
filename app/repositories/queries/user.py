post_client_query = 'INSERT INTO users (user_name, email, category_id) VALUES(%(name)s, %(email)s, %(category)s) RETURNING user_id'

post_analyst_query = 'INSERT INTO users (user_name, email, category_id, ranking) VALUES(%(name)s, %(email)s, %(category)s, %(ranking)s) RETURNING user_id'

get_users_query = 'SELECT users.*, categories.category_name AS category_name FROM users LEFT JOIN categories ON categories.category_id = users.category_id'

get_user_id_query = 'SELECT users.*, categories.category_name AS category_name FROM users LEFT JOIN categories ON categories.category_id = users.category_id WHERE user_id = %s'
