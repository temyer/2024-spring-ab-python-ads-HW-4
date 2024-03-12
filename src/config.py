import typing as tp
import os
from functools import lru_cache

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Config(BaseSettings):
    DB_HOST: tp.Final[str] = os.environ.get("DB_HOST")
    DB_DB: tp.Final[str] = os.environ.get("DB_DB")
    DB_PORT: tp.Final[int] = os.environ.get("DB_PORT")
    DB_USER: tp.Final[str] = os.environ.get("DB_USER")
    DB_PASSWORD: tp.Final[str] = os.environ.get("DB_PASSWORD")


@lru_cache
def get_config():
    return Config()
