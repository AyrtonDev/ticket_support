import uuid
from flask import make_response, jsonify

def is_valid_uuid(uuid_str:str):
    try:
        uuid_obj = uuid.UUID(uuid_str)
        return str(uuid_obj) == uuid_str
    except ValueError:
        return False

def build_response(data:dict | list | None, message:str, status=200):
    return make_response(
        jsonify(
            message=message,
            data=data
        ),
        status
    )

def print_error(error:Exception, with_response:bool):
    font_red = "\033[31m"
    back_white = "\033[47m"
    reset = "\033[0m"

    print(font_red + back_white, error, reset)
    if with_response:
        return build_response(
            message="Internal server error",
            data=None,
            status=500
        )

    return None

def get_client_and_analyst(id, users):
    data_user = None
    for user in users:
        if id == user['user_id']:
            data_user = user

    return data_user
