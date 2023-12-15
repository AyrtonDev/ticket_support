from app.repositories.category_repository import CategoryRepository
from app.utils.errors import InternalError
from app.utils.format import build_response, print_error

class CategoryController:
    def __init__(self):
        self._category_repository = CategoryRepository()

    def all(self):
        try:
            categories = self._category_repository.all()

            return build_response(categories,'')
        except InternalError as e:
            return e.response

category_controller = CategoryController()
