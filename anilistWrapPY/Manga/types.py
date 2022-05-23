# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

from __future__ import annotations
from anilistWrapPY.errors import AniListError

from typing import List, Optional

from pydantic import BaseModel


class Title(BaseModel):
    romaji: str
    english: Optional[str]
    native: str


class StartDate(BaseModel):
    year: int


class MediaItem(BaseModel):
    id: int
    title: Title
    description: Optional[str]
    startDate: StartDate
    type: str
    format: str
    status: str
    siteUrl: str
    averageScore: int
    genres: List[str]
    bannerImage: Optional[str]


class Page(BaseModel):
    media: List[MediaItem]


class Data(BaseModel):
    Page: Page


class AnilistManga(BaseModel):
    data: Optional[Data] = None
    error: Optional[AniListError] = None