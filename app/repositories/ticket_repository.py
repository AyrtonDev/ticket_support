from uuid import UUID
from typing import List
from app import cursor, conn
from app.utils.format import find_by_name
from app.utils.errors import InternalError, NotAllowed
from app.models.category_status import GetCategoryStatusDto
from app.repositories.queries.status import get_status_query
from app.models.ticket import GetTicketDto
from app.repositories.queries.ticket import post_ticket_query, get_tickets_analyst_query, get_tickets_client_query, get_ticket_query, put_ticket_next_query, put_ticket_finish_query, put_ticket_take_query

class TicketRepository:
    def __init__(self):
        cursor.execute(get_status_query)

        rows = cursor.fetchall()

        self._status = [GetCategoryStatusDto(row).to_dict() for row in rows]

    def all(self, user_id: str, category: bool) -> List[GetTicketDto]:
        try:
            QUERY = get_tickets_analyst_query if category else get_tickets_client_query

            cursor.execute(
                QUERY,
                (user_id, )
            )

            rows = cursor.fetchall()

            return [GetTicketDto(row).to_dict() for row in rows]

        except Exception as e:
            raise InternalError(e)

    def one(self, ticket_id: UUID, user_id: UUID, is_analyst: bool) -> GetTicketDto | None:
        try:
            cursor.execute(get_ticket_query, (ticket_id,))

            row = cursor.fetchone()

            if row is None:
                return None

            ticket = GetTicketDto(row)

            if is_analyst:
                if ticket.analyst_id is not None and ticket.analyst_id != user_id:
                    return None
            else:
                if ticket.client_id != user_id:
                    return None

            return GetTicketDto(row).to_dict()

        except Exception as e:
            raise InternalError(e)

    def create(self, **data) -> UUID:
        try:
            cursor.execute(
                post_ticket_query,
                {
                    **data,
                    'status': find_by_name('pending', self._status),
                }
            )

            conn.commit()

            return cursor.fetchone()[0]

        except Exception as e:
            raise InternalError(e)

    def update(self, *data) -> None:
        try:
            ticket, user_id = data

            if ticket['status_name'] == 'pending':
                cursor.execute(
                    put_ticket_take_query,
                    (
                        find_by_name('review', self._status),
                        user_id,
                        ticket['id'],
                    )
                )

            elif ticket['status_name'] == 'review':
                cursor.execute(
                    put_ticket_next_query,
                    (
                        find_by_name('solved', self._status),
                        ticket['id'],
                    )
                )

            elif ticket['status_name'] == 'solved':
                cursor.execute(
                    put_ticket_finish_query,
                    (
                        find_by_name('closed', self._status),
                        user_id,
                        ticket['id'],
                    )
                )

            conn.commit()

        except Exception as e:
            raise InternalError(e)

    def close(self, *data):
        try:
            ticket, user_id = data

            cursor.execute(
                    put_ticket_finish_query,
                    (
                        find_by_name('closed', self._status),
                        user_id,
                        ticket['id'],
                    )
                )

        except Exception as e:
            raise InternalError(e)
