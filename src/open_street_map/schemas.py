from pydantic import BaseModel, validator


class TreeCountRequest(BaseModel):
    city: str
    year: int

    @validator("year")
    def sane_year(cls, value):
        if 2000 <= value <= 2030:
            return value

        raise ValueError("year must be between 2000 and 2030")


class TreeCountResponse(BaseModel):
    city: str
    tree_count: int


class OSMRecord(BaseModel):
    city: str
    year: int
    tree_count: int
