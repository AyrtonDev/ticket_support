from app.models.ticket import PutTicketDto
from app.repositories.ticket_repository import TicketRepository
from app.utils.format import build_response, is_valid_uuid
from app.utils.errors import BadRequestion, FieldNotFound, NotAllowed, NotFound, InternalError
from flask import request, g


class TicketController():
    def __init__(self):
        self._ticket_repository = TicketRepository()

    def all(self):
        try:
            user_id = g.user_id
            is_analyst = g.is_analyst

            tickets = self._ticket_repository.all(user_id, is_analyst)

            return build_response(tickets, '')

        except InternalError as e:
            return e.response

    def one(self, ticket_id):
        try:
            user_id = g.user_id
            is_analyst = g.is_analyst

            if not ticket_id:
                raise FieldNotFound('ticket id is required in url')

            if not is_valid_uuid(ticket_id):
                raise BadRequestion('ticket id is invalid')

            ticket = self._ticket_repository.one(ticket_id, user_id, is_analyst)

            if ticket is None:
                raise NotFound('ticket not found')

            return build_response(ticket, '')

        except BadRequestion as e:
            return e.response
        except FieldNotFound as e:
            return e.response
        except NotFound as e:
            return e.response
        except InternalError as e:
            return e.response

    def create(self):
        try:
            is_analyst = g.is_analyst
            user_id = g.user_id

            input = request.get_json()

            if is_analyst:
                raise NotAllowed("you don't have permission for this action")

            if not input:
                raise BadRequestion("The 'title' and 'description' field are required")

            if 'title' not in input:
                raise BadRequestion("title is required")

            if len(input['title']) == 0:
                raise FieldNotFound("title field is empty")

            if 'description' not in input:
                raise BadRequestion("description is required")

            if len(input['description']) == 0:
                raise FieldNotFound("description field is empty")

            response = self._ticket_repository.create(user_id=user_id, **input)

            return build_response(response, '')

        except BadRequestion as e:
            return e.response
        except NotAllowed as e:
            return e.response
        except FieldNotFound as e:
            return e.response
        except NotFound as e:
            return e.response
        except InternalError as e:
            return e.response

    def next(self, ticket_id):
        try:
            is_analyst = g.is_analyst
            is_client = g.is_client
            user_id = g.user_id

            if not ticket_id:
                raise FieldNotFound('ticket id is required in url')

            if not is_valid_uuid(ticket_id):
                raise BadRequestion('ticket id is invalid')

            ticket = self._ticket_repository.one(ticket_id, user_id, is_analyst)

            if ticket is None:
                raise NotFound('ticket not found')

            data = PutTicketDto(ticket, user_id)

            if ticket['status_name'] == 'pending':
                if is_analyst:
                    self._ticket_repository.update(*data)

                    return build_response(
                        None,
                        'analyst changed the ticket for review',
                        200
                    )

                raise NotAllowed("you don't have permission for this action")

            if ticket['status_name'] == 'review':
                if ticket['client_id'] != user_id:
                    raise NotAllowed("you don't have permission for this action")

                if is_client:
                    self._ticket_repository.update(*data)

                    return build_response(
                        None,
                        'client changed the ticket for solved',
                        200
                    )

                raise NotAllowed("you don't have permission for this action")

            if ticket['status_name'] == 'solved':
                if is_analyst:
                    if ticket['analyst_id'] != user_id:
                        raise NotAllowed("you don't have permission for this action")

                if is_client:
                    if ticket['client_id'] != user_id:
                        raise NotAllowed("you don't have permission for this action")

                self._ticket_repository.update(*data)

                return build_response(
                    None,
                    f'the ticket {ticket_id} was closed',
                    200
                )

            raise BadRequestion("don't have any action")

        except BadRequestion as e:
            return e.response
        except NotAllowed as e:
            return e.response
        except FieldNotFound as e:
            return e.response
        except NotFound as e:
            return e.response
        except InternalError as e:
            return e.response

    def close(self, ticket_id):
        try:
            is_analyst = g.is_analyst
            user_id = g.user_id

            if is_analyst:
                raise NotAllowed("you don't have permission for this action")

            if not ticket_id:
                raise FieldNotFound('ticket id is required in url')

            if not is_valid_uuid(ticket_id):
                raise BadRequestion('ticket id is invalid')

            ticket = self._ticket_repository.one(ticket_id, user_id, is_analyst)

            if ticket is None:
                raise NotFound('ticket not found')

            data = PutTicketDto(ticket, user_id)

            if ticket['status_name'] == 'closed':
                raise BadRequestion("don't have any action")

            self._ticket_repository.close(*data)

            return build_response(None, 'the ticket was closed')

        except BadRequestion as e:
            return e.response
        except NotAllowed as e:
            return e.response
        except FieldNotFound as e:
            return e.response
        except NotFound as e:
            return e.response
        except InternalError as e:
            return e.response

ticket_controller = TicketController()
