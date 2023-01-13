"""
Python Libraries - FastAPI

https://fastapi.tiangolo.com/
https://www.uvicorn.org/
"""

import uvicorn

from fastapi import FastAPI
from decouple import config, Csv


def app():
    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"Argument": "This is the argument"}

    return app


if __name__ == "__main__":
    # .env file example:
    # MONOLITH=127.0.0.1,8080
    host, port = config("ENDPOINT", cast=Csv())
    uvicorn.run(
        "fastapi_example:app", host=host, port=int(port), log_level="debug", reload=True
    )