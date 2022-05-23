# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel
from ..errors.types import AniListError

class PreviousName(BaseModel):
    name: str
    updatedAt: int


class Avatar(BaseModel):
    large: str


class Options(BaseModel):
    profileColor: str


class MediaListOptions(BaseModel):
    scoreFormat: str


class GenrePreviewItem(BaseModel):
    genre: str
    count: int


class Anime(BaseModel):
    count: int
    meanScore: float
    standardDeviation: int
    minutesWatched: int
    episodesWatched: int
    genrePreview: List[GenrePreviewItem]


class Manga(BaseModel):
    count: int
    meanScore: int
    standardDeviation: int
    chaptersRead: int
    volumesRead: int
    genrePreview: List


class Statistics(BaseModel):
    anime: Anime
    manga: Manga


class ActivityHistoryItem(BaseModel):
    date: int
    amount: int
    level: int


class Stats(BaseModel):
    activityHistory: List[ActivityHistoryItem]


class Title(BaseModel):
    userPreferred: str


class CoverImage(BaseModel):
    large: str


class StartDate(BaseModel):
    year: int


class Node(BaseModel):
    id: int
    type: str
    status: str
    format: str
    isAdult: bool
    bannerImage: str
    title: Title
    coverImage: CoverImage
    startDate: StartDate


class Edge(BaseModel):
    favouriteOrder: int
    node: Node


class Anime1(BaseModel):
    edges: List[Edge]


class Manga1(BaseModel):
    edges: List


class Name(BaseModel):
    userPreferred: str


class Image(BaseModel):
    large: str


class Node1(BaseModel):
    id: int
    name: Name
    image: Image


class Edge1(BaseModel):
    favouriteOrder: int
    node: Node1


class Characters(BaseModel):
    edges: List[Edge1]


class Staff(BaseModel):
    edges: List


class Studios(BaseModel):
    edges: List


class Favourites(BaseModel):
    anime: Anime1
    manga: Manga1
    characters: Characters
    staff: Staff
    studios: Studios


class User(BaseModel):
    id: int
    name: str
    previousNames: List[PreviousName]
    avatar: Avatar
    bannerImage: str
    about: str
    isFollowing: bool
    isFollower: bool
    donatorTier: int
    donatorBadge: str
    createdAt: int
    moderatorRoles: Any
    isBlocked: bool
    bans: List
    options: Options
    mediaListOptions: MediaListOptions
    statistics: Statistics
    stats: Stats
    favourites: Favourites


class Data(BaseModel):
    User: User


class AnilistUser(BaseModel):
    error: Optional[List[AniListError]] = None
    data: Optional[Data] = None
