import jwt
from app import app
from flask import request, g
from functools import wraps
from jwt.exceptions import InvalidTokenError
from app.repositories.user_repository import UserRepository
from app.utils.errors import FieldNotFound, InternalError, NotAllowed
from app.utils.format import print_error


class Validate:
    def __init__(self):
        self._user_repository = UserRepository()

    def token(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            authorization = request.headers.get('Authorization')

            try:
                if authorization and authorization.startswith('Bearer '):
                    token = authorization[len('Bearer '):]

                    try:
                        payload = jwt.decode(token, app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
                        user_id = payload.get('user_id')

                        user = self._user_repository.one_by_id(user_id)

                        if user['category_name'] == 'client':
                            g.is_analyst = False
                            g.is_client = True
                        else:
                            g.is_analyst = True
                            g.is_client = False

                        g.user_id = user_id

                        return func(*args, **kwargs)
                    except InvalidTokenError:
                        raise NotAllowed('token is invalid')

                raise FieldNotFound('Authorization is empty')

            except NotAllowed as e:
                return e.response
            except FieldNotFound:
                return e.response
            except Exception as e:
                print_error(e)
                return InternalError(e).response

        return wrapper

validate = Validate()
