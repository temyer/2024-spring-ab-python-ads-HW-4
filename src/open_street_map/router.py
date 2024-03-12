import typing as tp

import requests
from fastapi import APIRouter, Depends, HTTPException, status

from src.open_street_map.exceptions import CityNotFoundException, OSMException
from src.open_street_map.schemas import TreeCountRequest, TreeCountResponse, OSMRecord
from src.open_street_map.osm import OSM
from src.open_street_map.db_logger import DBLogger

router = APIRouter(prefix="/v1/osm", tags=["open-street-map"])


@router.post("/tree-count")
async def tree_count(
    tree_count_request: TreeCountRequest,
    osm_service: tp.Annotated[OSM, Depends()],
    db_logger: tp.Annotated[DBLogger, Depends()],
) -> TreeCountResponse:
    try:
        total_trees = osm_service.get_tree_count(**tree_count_request.model_dump())

        osm_record = OSMRecord(
            **tree_count_request.model_dump(),
            tree_count=total_trees,
        )

        await db_logger.save_osm_record(osm_record)

        return TreeCountResponse(
            city=tree_count_request.city,
            tree_count=total_trees,
        )
    except (CityNotFoundException, OSMException) as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
    except requests.RequestException as e:
        raise HTTPException(
            status_code=status.HTTP_408_REQUEST_TIMEOUT,
            detail=str(e),
        )


@router.get("/most-freq-city")
async def most_freq_city(db_logger: tp.Annotated[DBLogger, Depends()]):
    result = await db_logger.get_most_freq_city()

    return {"city": result}
