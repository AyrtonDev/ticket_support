from app.controllers.category_controller import category_controller

def test_return_categories_success(context):
    with context:
        response = category_controller.all()
        data = response.get_json()

        assert response.status_code == 200
        assert data['data'] is not None
        assert data['message'] == ''
