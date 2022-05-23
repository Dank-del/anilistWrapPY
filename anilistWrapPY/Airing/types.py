# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>


from __future__ import annotations
from anilistWrapPY.errors import AniListError
from typing import List, Optional

from pydantic import BaseModel


class Title(BaseModel):
    romaji: str
    english: str
    native: str


class NextAiringEpisode(BaseModel):
    airingAt: int
    timeUntilAiring: int
    episode: int


class MediaItem(BaseModel):
    id: int
    bannerImage: str
    episodes: int
    title: Title
    siteUrl: str
    nextAiringEpisode: NextAiringEpisode


class Page(BaseModel):
    media: List[MediaItem]


class Data(BaseModel):
    Page: Page


class AnilistAiring(BaseModel):
    data: Optional[Data] = None
    error: Optional[AniListError] = None
