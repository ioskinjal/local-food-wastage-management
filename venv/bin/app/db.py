import sqlite3

DB_NAME = "food_wastage.db"

def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)