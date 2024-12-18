from fastapi import FastAPI
from fastapi.routing import Mount
from piccolo_admin.endpoints import create_admin
from pydantic_settings import BaseSettings

from rabbitdb.tables import (
    Hutch,
    HutchRabbit,
    RabbitFriend,
    Vaccinations,
    Vaccine,
    rabbit,
)

api = FastAPI(
    routes=[
        Mount(
            path="/admin",
            app=create_admin(
                tables=[
                    Hutch,
                    rabbit,
                    Vaccinations,
                    Vaccine,
                    HutchRabbit,
                    RabbitFriend,
                ],
                site_name="RabbitDB Admin",
            ),
        ),
    ]
)


class Config(BaseSettings):
    database_url: str = "postgresql://user:password@localhost/rabbitdb"


config = Config()


def server(host: str = "127.0.0.1", port: int = 6502):
    import uvicorn

    uvicorn.run("rabbitdb:api", host=host, port=port)
