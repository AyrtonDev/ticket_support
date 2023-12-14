from typing import Dict
from uuid import UUID

class Category(Dict):
    id: UUID
    name: str

query = 'SELECT * FROM categories'
