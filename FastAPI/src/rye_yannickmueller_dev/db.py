"""Module for login page"""

import hashlib
import secrets
import mariadb
from mariadb.constants.INDICATOR import NULL
from mariadb.constants.INFO import ERROR
from fastapi.responses import HTMLResponse, RedirectResponse
from capt import generate
from __init__ import templates as html


# Autor: Yannick Müller


class Signup:
    """
    In this class are the functions for the Signup process.
    """
    async def post(self, request, username, fname, lname, email, phone, passwd, chpasswd, salt, captcha):
        if not passwd == None and passwd == chpasswd and salt == captcha:
            if phone == None:
                phone = 'NULL'
            passwd = hashlib.sha512(b"{{passwd}}{{salt}}").hexdigest()
            try:
                conn = mariadb.connect(
                    host="172.15.15.3", port=3306, user="README", password="README"
                )
                cur = conn.cursor()
                cur.execute(
                    f"""INSERT INTO App.Login (username, fname, lname, email, phone, password, salt) 
                    VALUES ('{username}', '{fname}', '{lname}', '{email}', '{phone}','{passwd}', '{salt}')"""
                )
                conn.commit()
                conn.close()
                return RedirectResponse("/login", status_code=307)
            except Exception as e:
                return f"Error: {e}"
        else:
            error = 1
            salt = secrets.token_hex(2)
            await generate(salt)
            return html.TemplateResponse(
                request=request, name="signup.html", context={"error": error, "salt": salt}
            )


class Login:
    async def post(self, username, password):
        try:
            conn = mariadb.connect(
                host="172.15.15.3", port=3306, user="README", password="README"
            )
            cur = conn.cursor()
            cur.execute(
                f"USE App; SELECT username FROM Login WHERE password = {password} AND username = {username};<"
            )
            conn.commit()
            conn.close()
            return RedirectResponse("/login", status_code=307)
        except Exception as e:
            return f"Error: {e}"
