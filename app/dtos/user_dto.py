from typing import Dict
from uuid import UUID

class post_user_dto(Dict):
    name: str
    email: str
    category: str

class get_user_dto(Dict):
    id: UUID
    name: str
    email: str
    category_id: UUID
    ranking: str
    category_name: str
