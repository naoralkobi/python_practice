import mysql.connector
from mysql.connector import pooling

# Create a connection pool
db_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    host='your_host',
    user='your_user',
    password='your_password',
    database='your_database'
)


def get_connection():
    return db_pool.get_connection()


def close_connection(connection):
    connection.close()
