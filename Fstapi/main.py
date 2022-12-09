from fastapi import FastAPI, Query, Path, Body
from schemas import Book, Author, BookOut
from typing import List

app = FastAPI()


@app.get("/")
def home():
    return {"key": "Hello"}


# @app.get("/{pk}")
# def get_item(pk: str, value: int = None):
#     return {"key": pk, 'value': value}
#
#
# @app.get("/user/{pk}/items/{item}")
# def get_user_item(pk: int, item: str):
#     return {"user": pk, 'item': item}


@app.post('/author')
def create_author(author: Author = Body(..., embed=True)):
    return {"author": author}


@app.post("/book")
def create_book(item: Book, author: Author, quantity: int = Body(...)):
    return {'item': item, 'author': author, 'quantity': quantity}


@app.get("/stuk")
def get_book1(w: str = Query(None)):
    return w


@app.get("/kook")
def get_book2(e: str = Query('test', regex='qwerty')):
    return e


@app.get("/cook")
def get_book3(r: str = Query(..., min_length=2, max_length=5, description='Scatch ')):
    return r


@app.get("/sook")
def get_book4(t: List[str] = Query(..., min_length=2, max_length=5, description='Scatch ')):
    return t


@app.get("/sook2")
def get_book5(y: List[str] = Query(['...', "..."], min_length=2, max_length=55,
                                   description='Scatch ')):  # с параметрами по умолчанию
    return y


@app.get("/sook3")
def get_book6(
        u: List[str] = Query(None, min_length=2, max_length=55, description='Scatch ')):  # с параметрами по умолчанию
    return u


@app.get("/sook4")
def get_book7(i: str = Query(..., deprecated=False)):  # с параметрами по умолчанию
    return i


@app.get("/book/{pk}")
def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10, le=500)):
    return {'pk': pk, 'pages': pages}


@app.post('/book2', response_model=Book,
          response_model_exclude_unset=True)  # исключает из ответа сервера поля со значениями по умолчанию
def create_author2(item: Book):
    return item


@app.post('/book3', response_model=Book,
          response_model_exclude_unset=False)  # возвращает из ответа сервера поля со значениями по умолчанию, True возвращает из ответа сервера поля со значениями по умолчанию
def create_author3(item: Book):
    return item


@app.post('/book4', response_model=Book,
          response_model_exclude={'pages', 'date'})  # возвращает из ответа сервера поля со значениями по умолчанию
def create_author4(item: Book):
    return item


@app.post('/book5', response_model=BookOut)  # возвращает из ответа сервера поля со значениями по умолчанию
def create_author5(item: Book):
    return BookOut(**item.dict(), id=3)
