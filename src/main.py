from contextlib import asynccontextmanager


from fastapi import FastAPI

from src.db import get_async_pool
from src.open_street_map.router import router as osm_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async_pool = get_async_pool()

    await async_pool.open()
    yield
    await async_pool.close()


def get_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    app.include_router(osm_router)

    return app


app = get_app()
