from uuid import UUID
from typing import Dict, List, TypeVar
from flask import make_response, jsonify
from datetime import datetime


T = TypeVar('T')

def build_response(data: T, message:str, status=200):
    return make_response(
        jsonify(
            message=message,
            data=data
        ),
        status
    )

def is_valid_uuid(uuid_str:str) -> bool:
    try:
        uuid_obj = UUID(uuid_str)
        return str(uuid_obj) == uuid_str
    except ValueError:
        return False

def print_error(error):
    font_red = "\033[31m"
    back_white = "\033[47m"
    reset = "\033[0m"

    print(font_red + back_white, 'ERROR:', error, reset)

def get_client_and_analyst(id: UUID, users: List[Dict]) -> Dict:
    data_user = None
    for user in users:
        if id == user['user_id']:
            data_user = user

    return data_user

def find_by_name(name: str, list_data: Dict) -> UUID:
    for data in list_data:
        if data['name'] == name:
            return data['id']

def formatar_date(date: datetime) -> str:
    return date.strftime('%Y-%m-%dT%H:%M:%S')
