# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

from __future__ import annotations

from typing import List

from pydantic import BaseModel


class Location(BaseModel):
    line: int
    column: int


class AniListError(BaseModel):
    message: str
    status: int
    locations: List[Location]