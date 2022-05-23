# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

from __future__ import annotations
from msilib.schema import Error
from anilistWrapPY.errors import AniListError

from typing import List, Optional

from pydantic import BaseModel


class Title(BaseModel):
    romaji: str
    english: Optional[str]
    native: str


class ExternalLink(BaseModel):
    url: str


class AiringSchedule(BaseModel):
    nodes: List


class MediaItem(BaseModel):
    id: int
    title: Title
    type: str
    format: str
    status: str
    description: Optional[str]
    episodes: Optional[int]
    bannerImage: Optional[str]
    externalLinks: List[ExternalLink]
    duration: Optional[int]
    chapters: Optional[int]
    volumes: Optional[int]
    genres: List[str]
    synonyms: List[str]
    averageScore: Optional[int]
    airingSchedule: AiringSchedule
    siteUrl: str


class Page(BaseModel):
    media: List[MediaItem]


class Data(BaseModel):
    Page: Page


class AnilistMedia(BaseModel):
    data: Optional[Data] = None
    error: Optional[AniListError] = Error
