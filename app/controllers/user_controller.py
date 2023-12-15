from app.repositories.user_repository import UserRepository
from app.utils.errors import BadRequestion, FieldNotFound, InternalError, NotFound
from app.utils.format import build_response, is_valid_uuid
from flask import g

class UserController:
    def __init__(self):
        self._user_repository = UserRepository()

    def all(self):
        try:
            users = self._user_repository.all()

            return build_response(users, '')
        except InternalError as e:
            return e.response

    def myself(self):
        try:
            user_id = g.get('user_id')

            user = self._user_repository.one_by_id(user_id)

            return build_response(user, '')
        except InternalError as e:
            return e.response

    def one(self, user_id):
        try:
            if not user_id:
                raise FieldNotFound('user id is required in url')

            if not is_valid_uuid(user_id):
                raise BadRequestion('user id is invalid')

            user = self._user_repository.one_by_id(user_id)

            if user is None:
                raise NotFound('user not found')

            return build_response(user, '')

        except BadRequestion as e:
            return e.response
        except FieldNotFound as e:
            return e.response
        except NotFound as e:
            return e.response
        except InternalError as e:
            return e.response

user_controller = UserController()
