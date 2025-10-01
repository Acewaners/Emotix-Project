import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",          # sesuaikan kalau kamu pakai password di Laragon
        database="emotix_db"
    )