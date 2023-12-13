from app.repositories.category_repository import CategoryRepository
from app.utils import build_response

class CategoryController:
    def __init__(self):
        self._category_repository = CategoryRepository()

    def all(self):
        categories = self._category_repository.all()

        return build_response(
            message="",
            data= categories
        )

category_controller = CategoryController()
