from app.utils.format import build_response, print_error

class BaseErrorCustom(Exception):
    def __init__(self, status, message):
        self.response = build_response(None, message, status)
        super().__init__()

class BadRequestion(BaseErrorCustom):
    def __init__(self, message):
        super().__init__(400, message)

class NotAllowed(BaseErrorCustom):
    def __init__(self, message):
        super().__init__(401, message)

class FieldNotFound(BaseErrorCustom):
    def __init__(self, message):
        super().__init__(403, message)

class NotFound(BaseErrorCustom):
    def __init__(self, message):
        super().__init__(404, message)

class InternalError(BaseErrorCustom):
    def __init__(self, e: Exception):
        super().__init__(500, 'Internal Error')
        print_error(e)
