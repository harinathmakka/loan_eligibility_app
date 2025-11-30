import os
import mysql.connector

def get_db_connection():
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USER = os.getenv("DB_USER", "loan_user")
    DB_PASS = os.getenv("DB_PASS", "prasad123")
    DB_NAME = os.getenv("DB_NAME", "loan_app")
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        auth_plugin='mysql_native_password'
    )
