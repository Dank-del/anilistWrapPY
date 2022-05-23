# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

from __future__ import annotations
from anilistWrapPY.errors import AniListError
from typing import List, Optional

from pydantic import BaseModel


class Name(BaseModel):
    full: str
    native: str
    alternative: List[str]


class Image(BaseModel):
    large: str
    medium: str


class Title(BaseModel):
    romaji: str
    english: Optional[str]
    native: Optional[str]


class Node(BaseModel):
    title: Title
    type: str
    format: str
    siteUrl: str


class Media(BaseModel):
    nodes: List[Node]


class DateOfBirth(BaseModel):
    year: Optional[int]
    month: Optional[int]
    day: Optional[int]


class Character(BaseModel):
    name: Name
    description: str
    image: Image
    media: Media
    siteUrl: str
    id: int
    dateOfBirth: DateOfBirth
    age: Optional[str]
    favourites: int


class Page(BaseModel):
    characters: List[Character]


class Data(BaseModel):
    Page: Page


class AnilistCharacter(BaseModel):
    data: Optional[Data] = None
    error: Optional[AniListError] = None