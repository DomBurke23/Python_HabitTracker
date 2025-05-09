import sqlite3
from flask import current_app

class UserRepository:
    def __init__(self, db_file):
        self.db_file = db_file

    def _get_db(self):
        conn = sqlite3.connect(self.db_file)
        conn.row_factory = sqlite3.Row
        return conn

    def _close_db(self, conn):
        if conn:
            conn.close()

    def fetch_users(self):
        conn = self._get_db()
        cursor = conn.cursor()
        users = cursor.execute("SELECT id, username FROM users").fetchall()
        self._close_db(conn)
        return users

    def fetch_user_by_username(self, username):
        conn = self._get_db()
        cursor = conn.cursor()
        user = cursor.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        self._close_db(conn)
        return user