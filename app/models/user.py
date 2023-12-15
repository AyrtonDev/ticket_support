from uuid import UUID
from typing import Dict, Tuple

type_user = Tuple[UUID, str, str, UUID, str | None, str]

class GetUserDto(Dict):
    def __init__(self, data: type_user):
        self.id = data[0]
        self.name = data[1]
        self.email = data[2]
        self.category_id = data[3]
        self.ranking = data[4]
        self.category_name = data[5]

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'category_id': self.category_id,
            'ranking': self.ranking,
            'category_name': self.category_name
        }

class PostUserDto(Dict):
    name: str
    email: str
    category: UUID
