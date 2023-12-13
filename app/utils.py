from flask import make_response, jsonify

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
