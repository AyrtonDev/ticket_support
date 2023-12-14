from uuid import UUID
from typing import List
from app import cursor, conn
from app.dtos.user_dto import get_user_dto, post_user_dto
from app.models.user import User, post_analyst_query, post_client_query, get_users_query, delete_user_query


class UserRepository:
    def __init__(self):
        cursor.execute("SELECT * FROM categories WHERE category_name = 'analyst'")

        self._analyst_id = cursor.fetchone()[0]

    def all(self) -> List[get_user_dto]:
        try:
            users_list = []
            cursor.execute(get_users_query)
            users: List[User] = cursor.fetchall()

            print(users)

            for user in users:
                d_user = {}

                if user[5] == 'analyst':
                    d_user.update({
                        'id': user[0],
                        'name': user[1],
                        'email': user[2],
                        'category_id': user[3],
                        'ranking': user[4],
                        'category_name': user[5]
                    })

                d_user.update({
                    'id': user[0],
                    'name': user[1],
                    'email': user[2],
                    'category_id': user[3],
                    'category_name': user[5]
                })

                users_list.append(d_user)

            return users_list

        except Exception as e:
            raise e

    def create(self, data: post_user_dto) -> UUID:
        try:
            if self._analyst_id == data['category']:
                cursor.execute(
                    post_analyst_query,
                    {
                        'name': data['name'],
                        'email': data['email'],
                        'category': data['category'],
                        'ranking': 'D'
                    }
                )
            else:
                cursor.execute(
                    post_client_query,
                    {
                        'name': data['name'],
                        'email': data['email'],
                        'category': data['category'],
                    }
                )

            new_user_id = cursor.fetchone()[0]

            conn.commit()

            return new_user_id
        except Exception as e:
            raise e

    def delete(self, user_id):
        try:
            cursor.execute(
                delete_user_query,
                (
                    user_id,
                )
            )

            conn.commit()

        except Exception as e:
            raise e
