from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse
from starlette import status
from api.items_view import router as items_router
from api.users.views import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hello")
def hello():
    return {
        'message': ''
    }


# @app.get("{path:path}")
# def all_others(path:str):
#     return{
#         'request to': path
#     }



@app.exception_handler(status.HTTP_404_NOT_FOUND)
async def custom_404_handler(request, exception):
    print(exception, type(exception))
    if isinstance(exception, HTTPException):
        return exception
    return JSONResponse(
        {
            'request url': request.url.path,
            'exception': str(exception),
        },
        status_code=status.HTTP_404_NOT_FOUND,
    )
