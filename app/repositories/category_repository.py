from typing import List
from app import cursor
from app.models.category_status import GetCategoryStatusDto
from app.repositories.queries.category import get_categories_query
from app.utils.errors import InternalError

class CategoryRepository:
    try:
        def all(self) -> List[GetCategoryStatusDto]:
            cursor.execute(get_categories_query)
            rows = cursor.fetchall()

            return [GetCategoryStatusDto(row).to_dict() for row in rows]
    except Exception as e:
        raise InternalError(e)
