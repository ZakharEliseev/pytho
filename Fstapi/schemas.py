from typing import List
from pydantic import BaseModel, validator, Field
from datetime import date


class Genre(BaseModel):
    name: str


class Author(BaseModel):
    first_name: str = Field(..., max_length=25)
    last_name: str
    age: int = Field(..., gt=15, lt=90, description='Author age must be more than 15 years old and less than 90')
    year: int

    @validator('year')
    def check_year(cls, v):
        if v < 2002:
            raise ValueError('Year must be at least 2002')
        return v


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre] = []
    pages: int = 10


class  BookOut(Book):
    id: int