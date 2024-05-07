"""Basefile for FastAPI"""

# Autor: Yannick Müller
from fastapi import FastAPI, Form
from typing import Annotated
from fastapi.templating import Jinja2Templates as j2
from fastapi.staticfiles import StaticFiles

api = FastAPI(title="yannickmueller", version="0.0.1")

templates = j2(directory="templates")

api.mount("/static", StaticFiles(directory="static"), name="static")
