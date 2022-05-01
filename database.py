from psycopg2 import pool
import cred

# import psycopg2
# def connect():
#     return psycopg2.connect(user=cred.login, password=cred.passwd, database='learning', host='localhost')
# before connection pooling


class Database:
    connection_pool = None

    @staticmethod
    def initialise():
        Database.connection_pool = pool.SimpleConnectionPool(1,
                                                             5,
                                                             user=cred.login,
                                                             password=cred.passwd,
                                                             database='learning',
                                                             host='localhost')

    @classmethod
    def get_connection(cls):
        return cls.connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        Database.connection_pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):
        Database.connection_pool.closeall()


class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)
