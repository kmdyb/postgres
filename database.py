from psycopg2 import pool
import cred

# import psycopg2
# def connect():
#     return psycopg2.connect(user=cred.login, password=cred.passwd, database='learning', host='localhost')
# before connection pooling

connection_pool = pool.SimpleConnectionPool(1,
                                            5,
                                            user=cred.login,
                                            password=cred.passwd,
                                            database='learning',
                                            host='localhost')


class ConnectionFromPool:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = connection_pool.getconn()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        connection_pool.putconn(self.connection)
