from typing import List, Dict
from app import cursor
from app.models.category import Category, query

class CategoryRepository:
    def all(self) -> List[Category | None]:
        category_list = []
        cursor.execute(query)
        categories = cursor.fetchall()

        for category in categories:
            category_list.append({
                'id': category[0],
                'name': category[1]
            })

        return category_list
