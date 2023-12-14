import re
from flask import request
from app.repositories.user_repository import UserRepository
from app.utils import build_response, is_valid_uuid, print_error
from app.dtos.user_dto import post_user_dto

class AuthController:
    def __init__(self):
        self._user_repository = UserRepository()

    def create(self):
        try:
            input: post_user_dto | None = request.get_json()

            if not input:
                return build_response(None, "The 'name', 'email' and 'category' field are required", 400)

            if 'name' not in input.keys():
                return build_response(None, 'Name is required', 400)

            if 'email' not in input.keys():
                return build_response(None, 'E-mail is required', 400)

            if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", input["email"]):
                return build_response(None, 'E-mail is invalid', 400)

            if 'category' not in input.keys():
                return build_response(None, 'Category is required', 400)

            if not is_valid_uuid(input['category']):
                return build_response(None, 'Category is invalid', 400)

            response = self._user_repository.create(input)

            return build_response(response, '', 201)
        except Exception as e:
            return print_error(e, True)

auth_controller = AuthController()
