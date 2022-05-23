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
    year: Optional[int]


class Node(BaseModel):
    name: str


class Studios(BaseModel):
    nodes: List[Node]


class TrailerItem(BaseModel):
    id: str
    site: str
    thumbnail: str


class ExternalLink(BaseModel):
    url: str
    site: str


class MediaItem(BaseModel):
    id: int
    title: Title
    description: str
    startDate: StartDate
    episodes: Optional[int]
    season: Optional[str]
    type: str
    format: str
    status: str
    duration: Optional[int]
    siteUrl: str
    studios: Studios
    trailer: Optional[TrailerItem]
    externalLinks: List[ExternalLink]
    averageScore: Optional[int]
    genres: List[str]
    bannerImage: Optional[str]


class Page(BaseModel):
    media: List[MediaItem]


class Data(BaseModel):
    Page: Page


class AniListAnime(BaseModel):
    data: Optional[Data] = None
    error: Optional[AniListError] = None