"""Module for login page"""

import os
import hashlib
import secrets
import mariadb
from mariadb.constants.INDICATOR import NULL
from mariadb.constants.INFO import ERROR
from fastapi.responses import HTMLResponse, RedirectResponse


# Autor: Yannick Müller


class Signup:
    """
    In this class are the functions for the Signup process.
    """
    async def signup(self, username, fname, lname, email, phone, password, chpassword, salt, captcha):
        if salt == captcha:
            if phone == "":
                phone = 'NULL'
            try:
                conn = mariadb.connect(
                    host="172.15.15.3", port=3306, user="README", password="README"
                )
                cur = conn.cursor()
                cur.execute("USE App;")
                if phone == "NULL":
                    cur.execute(
                        f"""INSERT INTO Login (username, fname, lname, email, phone, password, salt)
                        VALUES ('{username}', '{fname}', '{lname}', '{email}', '{phone}','{password}', '{salt}')"""
                    )
                else:
                    cur.execute(
                        f"""INSERT INTO Login (username, fname, lname, email, phone, password, salt)
                        VALUES ('{username}', '{fname}', '{lname}', '{email}', '{phone}','{password}', '{salt}')"""
                    )
                conn.commit()
                conn.close()
                return 'true'
            except Exception as e:
                return f"Error: {e}"
        else:
            return "false"


class Login:
    async def get(self, username, password):
        try:
            conn = mariadb.connect(
                host="172.15.15.3", port=3306, user="README", password="README"
            )
            cur = conn.cursor()
            cur.execute("USE App;")
            cur.execute(
                f"SELECT username FROM Login WHERE password = '{password}' AND username = '{username}'"
            )
            out = cur.fetchall()
            conn.commit()
            conn.close()
            return out
        except Exception as e:
            return f"Error: {e}"
class GetSalt:
    async def gets(self, username):
        try:
            conn = mariadb.connect(
                host="172.15.15.3", port=3306, user="README", password="README"
            )
            cur = conn.cursor()
            cur.execute("USE App;")
            cur.execute(f"SELECT salt FROM Login WHERE username = '{username}'")
            salt = cur.fetchall()[0][0]
            conn.commit()
            conn.close()
        except Exception as e:
            return f"Error: {e}"
        return salt
