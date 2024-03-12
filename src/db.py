from functools import lru_cache

from psycopg_pool import AsyncConnectionPool

from src.config import get_config


def get_db_uri():
    c = get_config()

    return f"host={c.DB_HOST} port={c.DB_PORT} user={c.DB_USER} password={c.DB_PASSWORD} dbname={c.DB_DB} connect_timeout=10"


@lru_cache
def get_async_pool():
    return AsyncConnectionPool(conninfo=get_db_uri(), open=False)
