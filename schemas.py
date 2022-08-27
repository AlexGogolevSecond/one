from pydantic import BaseModel


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: None


