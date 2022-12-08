from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/hello')
def hello():
    return{
        'message': 'Hello!!!!'
    }


@app.get('/{url_path:path}')
def all_others(url_path: str):
    return{'request to': url_path}

