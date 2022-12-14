from datetime import date
from typing import List
from pydantic import BaseModel


class Genre(BaseModel):
    name: str


class Author(BaseModel):
    first_name: str
    last_name: str
    age: int


class Book(BaseModel):
    """Модель аудиокниги"""
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre]
    pages: int


