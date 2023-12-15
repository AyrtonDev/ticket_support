from typing import NamedTuple, Tuple, Dict
from uuid import UUID
from datetime import datetime

from app.utils.format import formatar_date

type_ticket = Tuple[str, str, str, UUID, UUID, datetime, UUID | None, UUID | None, str]

class GetTicketDto(Dict):
    def __init__(self, data: type_ticket):
        self.id = data[0]
        self.title = data[1]
        self.description = data[2]
        self.client_id = data[3]
        self.status_id = data[4]
        self.created_at = formatar_date(data[5])
        self.closed_by = data[6]
        self.analyst_id = data[7]
        self.status_name = data[8]

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'client_id': self.client_id,
            'stats_id': self.status_id,
            'created_at': self.created_at,
            'closed_by': self.closed_by,
            'analyst_id': self.analyst_id,
            'status_name': self.status_name,
        }

class PutTicketDto(NamedTuple):
    user_id: UUID
    ticket: GetTicketDto
