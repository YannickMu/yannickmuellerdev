"""Basefile for FastAPI"""

# Autor: Yannick Müller
from fastapi import FastAPI
from typing import Annotated
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI(title="yannickmueller", version="0.0.1")

origins = [
    "https://ya007.ch",
    "http://localhost:4200",
    "https://yannickmueller.dev",
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api.mount("/static", StaticFiles(directory="static"), name="static")
