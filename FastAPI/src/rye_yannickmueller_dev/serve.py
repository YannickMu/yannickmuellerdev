"""Module for all pages"""

# Autor: Yannick Müller
from typing import Annotated, Optional

import secrets
from capt import generate
from db import GetSalt, Login, Signup
from __init__ import api
from capt import generate
from fastapi import Request, Depends
from fastapi.responses import RedirectResponse

async def generate_salt():
	"""Generate a captcha"""
	return secrets.token_hex(4)

@api.get("/", response_class=RedirectResponse)
async def root():
	"""This function returns a redirect for the gui to the login page."""
	return RedirectResponse("/login", status_code=307)


# /login
@api.get("/api/login/gets",)
async def getsalt(uname: str):
	"""takes uname and geather salt"""
	gs = GetSalt()
	return await gs.gets(uname)

@api.get("/api/login/login",)
async def getlogin(username: str, passwd: str):
    gl = Login()
    res = await gl.get(username, passwd)
    if not res == []:
        return "true"
    return "No such user"
# /signup
@api.get('/api/signup/gets')
async def gens():
    salt = await generate_salt()
    await generate(salt)
    return salt


@api.get('/api/signup/signup')
async def signup(username: str, fname: str, lname: str, email: str, password: str, chpassword: str, salt: str, captcha: str, phone: str = ""):
    si = Signup()
    return await si.signup(username, fname, lname, email, phone, password, chpassword, salt, captcha)
