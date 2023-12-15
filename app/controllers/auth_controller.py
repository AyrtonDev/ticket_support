import re
import jwt
from flask import request
from app import app
from app.repositories.user_repository import UserRepository
from app.utils.errors import BadRequestion, FieldNotFound, InternalError, NotFound
from app.utils.format import build_response, is_valid_uuid, print_error
from app.models.user import PostUserDto

class AuthController:
    def __init__(self):
        self._user_repository = UserRepository()

    def register(self):
        try:
            input = request.get_json()

            if not input:
                return BadRequestion("the body is empty")

            if 'name' not in input.keys():
                raise FieldNotFound('Name is required')

            if 'email' not in input.keys():
                raise FieldNotFound('E-mail is required')

            if not re.match(
                r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
                input["email"]
            ):
                raise BadRequestion('E-mail is invalid')

            if 'category' not in input.keys():
                raise FieldNotFound('Category is required')

            if not is_valid_uuid(input['category']):
                raise BadRequestion('Category is invalid')

            response = self._user_repository.create(input)

            return build_response(response, '', 201)

        except BadRequestion as e:
            return e.response
        except FieldNotFound as e:
            return e.response
        except InternalError as e:
            return e.response

    def login(self):
        input = request.get_json()

        try:
            if not input:
                raise FieldNotFound('user_id is required')

            user_id = input['user_id']

            if not is_valid_uuid(user_id):
                raise BadRequestion('Category is invalid')

            user = self._user_repository.one_by_id(user_id)

            if user is None:
                raise NotFound('user not found')

            token = jwt.encode({"user_id": user_id}, app.config['JWT_SECRET_KEY'], algorithm="HS256")

            return build_response(token, '')

        except BadRequestion as e:
            return e.response
        except FieldNotFound as e:
            return e.response
        except NotFound as e:
            return e.response
        except InternalError as e:
            return e.response


auth_controller = AuthController()
