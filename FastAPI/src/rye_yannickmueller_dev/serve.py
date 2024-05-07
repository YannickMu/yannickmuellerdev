"""Module for all pages"""

# Autor: Yannick Müller
from typing import Annotated, Optional

import secrets
from db import Login, Signup
from __init__ import api
from __init__ import templates as html
from capt import generate
from fastapi import Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse

async def generate_salt():
	"""Generate a captcha"""
	return secrets.token_hex(2)

@api.get("/", response_class=RedirectResponse)
async def root():
	"""This function returns a redirect for the gui to the login page."""
	return RedirectResponse("/login", status_code=307)


# /login
@api.post("/login")
async def login():
	"""function for login process"""
	print("login")


@api.get("/login", response_class=HTMLResponse)
async def getlogin(request: Request):
	"""returns the login page"""
	error = None
	return html.TemplateResponse(
		request=request, name="login.html", context={"error": error}
	)


# /signup
@api.post("/signup")
async def signup(request: Request, fname: Annotated[str, Form()], lname: Annotated[str, Form()], \
email: Annotated[str, Form()], passwd: Annotated[str, Form()], username: Annotated[str, Form()], \
chpasswd: Annotated[str, Form()], captcha: Annotated[str, Form()], \
context: dict = Depends(generate), phone: Optional[str] = Form(None)):
	"""function for Signup process"""
	s = Signup()
	salt = context.data
	return await s.post(request, username, fname, lname, email, phone, passwd, chpasswd, salt, captcha)


@api.get("/signup")
async def getsignup(request: Request):
	"""returns the signup page"""
	error = None
	salt = secrets.token_hex(2)
	await generate(salt)
	return html.TemplateResponse(
		request=request, name="signup.html", context={"error": error, "salt": salt}
	)
