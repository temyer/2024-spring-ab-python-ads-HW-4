from src.db import get_async_pool
from src.open_street_map.schemas import OSMRecord


class DBLogger:
    def __init__(self) -> None:
        self._pool = get_async_pool()

    async def save_osm_record(self, osm_record: OSMRecord):
        async with self._pool.connection() as conn:
            await conn.execute(
                "insert into osm_record(city, year, tree_count) values (%s, %s, %s)",
                (osm_record.city, osm_record.year, osm_record.tree_count),
            )

    async def get_most_freq_city(self) -> str | None:
        async with self._pool.connection() as conn, conn.cursor() as cur:
            await cur.execute("select most_freq_city()")

            result = await cur.fetchone()

            if not result:
                return None

            return result[0]
