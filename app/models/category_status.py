from uuid import UUID
from typing import Dict, Tuple

type_category = Tuple[UUID, str]

class GetCategoryStatusDto(Dict):
    def __init__(self, data: type_category):
        self.id = data[0]
        self.name = data[1]

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
