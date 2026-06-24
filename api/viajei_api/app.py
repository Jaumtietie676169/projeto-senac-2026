from http import HTTPStatus

from api.viajei_api.schemas.user import User, UserDB, UserPublic
from fastapi import FastAPI

app = FastAPI()

database = []


@app.get("/")
def read_root():
    return {"message": "Bem vindo!"}


@app.get("/")
def bem_vindo():
    return {"message": "Bem vindo!"}


@app.get("/hello")
def ola_mundo():
    return """
        <head>
        </head>
        <body>
            <h1> </h1>
        </body>
"""


@app.post("/auth/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: User):
    user_with_id = UserDB(**user.model(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id
