from uuid import UUID
from typing import List
from app import cursor, conn
from app.models.user import GetUserDto, PostUserDto
from app.repositories.queries.category import get_category_query
from app.repositories.queries.user import post_analyst_query, post_client_query, get_users_query, get_user_id_query
from app.utils.errors import InternalError


class UserRepository:
    def __init__(self):
        cursor.execute(get_category_query, ('analyst', ))

        self._analyst_category_id = cursor.fetchone()[0]

    def all(self) -> List[GetUserDto]:
        try:
            cursor.execute(get_users_query)
            rows = cursor.fetchall()

            return [GetUserDto(row).to_dict() for row in rows]

        except Exception as e:
            raise InternalError(e)

    def one_by_id(self, user_id: UUID) -> GetUserDto | None:
        try:
            cursor.execute(get_user_id_query, ( user_id,))

            row = cursor.fetchone()

            if row is None:
                return None

            return GetUserDto(row).to_dict()

        except Exception as e:
            raise InternalError(e)

    def create(self, data: PostUserDto) -> UUID:
        try:
            if self._analyst_category_id == data['category']:
                cursor.execute(
                    post_analyst_query,
                    {**data, 'ranking': 'D'}
                )
            else:
                cursor.execute(
                    post_client_query,
                    {**data}
                )

            conn.commit()

            return cursor.fetchone()[0]

        except Exception as e:
            raise InternalError(e)
