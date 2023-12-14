# import requests
# import time
# import unittest
# from app.utils import get_client_and_analyst, is_valid_uuid

# from mock.routes import valid_data_analyst, valid_data_client

# from test import start_app, stop_app

# try:
#     app_process = start_app()

#     time.sleep(2)

#     def test_get_all_categories():
#         response_get = requests.get("http://127.0.0.1:3001/categories")
#         output_get = response_get.json()

#         list_categories = output_get['data']
#         analyst_category = list_categories[0]


#         assert response_get.status_code == 200
#         assert 'id' in analyst_category
#         assert 'name' in analyst_category
#         assert 'analyst' is analyst_category["name"]

#     class TestRoutesUsers(unittest.TestCase):
#         def __init__(self):
#             response_get = requests.get("http://127.0.0.1:3001/categories")
#             output_get = response_get.json()
#             list_categories = output_get['data']

#             self.base_url = "http://127.0.0.1:3001"

#             self.analyst_category = list_categories[0]
#             self.client_category = list_categories[1]
#             self.data_analyst = {
#                 **valid_data_analyst,
#                 'category': self.analyst_category['id']
#             }
#             self.data_client = {
#                 **valid_data_client,
#                 'category': self.client_category['id']
#             }
#             self.users_id = []

#         def test_register_new_analyst(self):
#             response_post = requests.post(self.base_url + "/register", self.data_analyst)
#             output_post = response_post.json()

#             self.users_id.append(output_post['data'])

#             self.assertTrue(response_post.status_code == 201)
#             self.assertTrue(is_valid_uuid(self.user_id[0]))

#         def test_register_new_client(self):
#             response_post = requests.post(self.base_url + "/register", self.data_client)
#             output_post = response_post.json()

#             self.users_id.append(output_post['data'])

#             self.assertTrue(response_post.status_code == 201)
#             self.assertTrue(is_valid_uuid(self.user_id[1]))

#         def test_get_analyst(self):
#             response_get = requests.get(self.base_url + "/users")
#             output_get = response_get.json

#             user_analyst = get_client_and_analyst(
#                 self.users_id[0],
#                 output_get['data']
#             )

#             self.assertEqual(user_analyst['name'], self.data_analyst['name'])
#             self.assertEqual(user_analyst['email'], self.data_analyst['email'])
#             self.assertIn('category_name', user_analyst)
#             self.assertEqual(user_analyst['category_name'], 'analyst')
#             self.assertIn('ranking', user_analyst)
#             self.assertNotEqual(user_analyst['ranking'], '')

#         def test_get_client(self):
#             response_get = requests.get(self.base_url + "/users")
#             output_get = response_get.json

#             user_client = get_client_and_analyst(
#                 self.users_id[1],
#                 output_get['data']
#             )

#             self.assertEqual(user_client['name'], self.data_client['name'])
#             self.assertEqual(user_client['email'], self.data_client['email'])
#             self.assertIn('category_name', user_client)
#             self.assertEqual(user_client['category_name'], 'client')
#             self.assertNotIn('ranking', user_client)


# finally:
#     stop_app(app_process)
