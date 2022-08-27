from datetime import date
from typing import List
from pydantic import BaseModel


class Genre(BaseModel):
    name: str


class Book(BaseModel):
    """Модель аудиокниги"""
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre]
    pages: int


