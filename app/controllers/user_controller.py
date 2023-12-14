from app.repositories.user_repository import UserRepository
from app.utils import build_response, is_valid_uuid, print_error


class UserController:
    def __init__(self):
        self._user_repository = UserRepository()

    def all(self):
        try:
            users = self._user_repository.all()

            return build_response(users, '')
        except Exception as e:
            return print_error(e, True)

    def delete(self, user_id):
        try:
            if not is_valid_uuid(user_id):
                return build_response(None, 'User id is invalid', 400)

            self._user_repository.delete(user_id)

            return build_response(None, 'user deleted', 204)
        except Exception as e:
            return print_error(e, True)

user_controller = UserController()
