import requests
import time

from tests import start_app, stop_app

def test_get_all_categories():
    app_process = start_app()

    time.sleep(1)

    try:
        response_get = requests.get("http://127.0.0.1:3001/categories")
        output_get = response_get.json()

        list_categories = output_get['data']
        item_category = list_categories[0]

        assert response_get.status_code == 200
        assert item_category["id"] == 'fcbd7109-4378-4010-a504-57f81f2e86e1'
        assert item_category["name"] == 'analyst'

    finally:
        stop_app(app_process)
