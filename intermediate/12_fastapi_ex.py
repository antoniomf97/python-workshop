"""
Python Libraries - FastAPI

https://fastapi.tiangolo.com/
https://www.uvicorn.org/
https://docs.pydantic.dev/
"""

import uvicorn

from fastapi import FastAPI, HTTPException
from decouple import config, Csv

from pydantic import BaseModel


class Argument2(BaseModel):
    argument_3: int


class FastApiRequest(BaseModel):
    argument_1: str
    argument_2: Argument2


def app():
    app = FastAPI()

    @app.get("/")
    def get_request():
        return {"Argument": "This is the argument"}

    @app.post("/")
    def post_request(request: FastApiRequest):
        try:
            print(request.argument_1 + request.argument_2.argument_3)
        except Exception as e:
            return HTTPException(
                status_code=500, detail="Internal Error Server: " + str(e)
            )

        return {"Received": "Sucessfully processed"}

    return app


if __name__ == "__main__":
    host, port = config("ENDPOINT", cast=Csv())
    uvicorn.run(
        "fastapi_example:app", host=host, port=int(port), log_level="debug", reload=True
    )
