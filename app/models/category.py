from typing import Dict
import uuid


class Category(Dict):
    id: uuid
    name: str

query = 'SELECT * FROM categories'
