import psycopg2
from app.utils import print_error

def db_connection():
    dbname = 'ticket_db'
    user = 'root'
    password = 'root'
    host = 'localhost'
    port = '5432'

    try:
        connection = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port= port
        )
        print('DB connection successful')
        return connection.cursor(), connection

    except Exception as e:
        print_error(e, False)
