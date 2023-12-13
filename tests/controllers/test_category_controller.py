from app.controllers.category_controller import category_controller
import time

from tests import start_app, stop_app

async def test_return_list_categories():
    app_process = start_app()

    time.sleep(1)

    try:
        response = await category_controller.all()

        list_categories = response['data']
        item_category = list_categories[0]

        assert item_category["id"] == 'fcbd7109-4378-4010-a504-57f81f2e86e1'
        assert item_category["name"] == 'analyst'

    finally:
        stop_app(app_process)
