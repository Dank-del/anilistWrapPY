# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

from anilistWrapPY.errors import Error
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Any, List

from anilistWrapPY.utils import from_union, from_int, from_none, from_list, to_class, from_str, to_enum


@dataclass
class DateOfBirth:
    year: None
    month: Optional[int] = None
    day: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DateOfBirth':
        assert isinstance(obj, dict)
        year = from_none(obj.get("year"))
        month = from_union([from_int, from_none], obj.get("month"))
        day = from_union([from_int, from_none], obj.get("day"))
        return DateOfBirth(year, month, day)

    def to_dict(self) -> dict:
        result: dict = {"year": from_none(self.year), "month": from_union([from_int, from_none], self.month),
                        "day": from_union([from_int, from_none], self.day)}
        return result


@dataclass
class Image:
    large: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Image':
        assert isinstance(obj, dict)
        large = from_union([from_str, from_none], obj.get("large"))
        return Image(large)

    def to_dict(self) -> dict:
        result: dict = {"large": from_union([from_str, from_none], self.large)}
        return result


class Format(Enum):
    MANGA = "MANGA"
    NOVEL = "NOVEL"
    OVA = "OVA"
    TV = "TV"


@dataclass
class Title:
    romaji: Optional[str] = None
    english: Optional[str] = None
    native: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Title':
        assert isinstance(obj, dict)
        romaji = from_union([from_str, from_none], obj.get("romaji"))
        english = from_union([from_none, from_str], obj.get("english"))
        native = from_union([from_str, from_none], obj.get("native"))
        return Title(romaji, english, native)

    def to_dict(self) -> dict:
        result: dict = {"romaji": from_union([from_str, from_none], self.romaji),
                        "english": from_union([from_none, from_str], self.english),
                        "native": from_union([from_str, from_none], self.native)}
        return result


class TypeEnum(Enum):
    ANIME = "ANIME"
    MANGA = "MANGA"


@dataclass
class Node:
    title: Optional[Title] = None
    type: Optional[TypeEnum] = None
    format: Optional[Format] = None
    site_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Node':
        assert isinstance(obj, dict)
        title = from_union([Title.from_dict, from_none], obj.get("title"))
        type = from_union([TypeEnum, from_none], obj.get("type"))
        format = from_union([Format, from_none], obj.get("format"))
        site_url = from_union([from_str, from_none], obj.get("siteUrl"))
        return Node(title, type, format, site_url)

    def to_dict(self) -> dict:
        result: dict = {"title": from_union([lambda x: to_class(Title, x), from_none], self.title),
                        "type": from_union([lambda x: to_enum(TypeEnum, x), from_none], self.type),
                        "format": from_union([lambda x: to_enum(Format, x), from_none], self.format),
                        "siteUrl": from_union([from_str, from_none], self.site_url)}
        return result


@dataclass
class Media:
    nodes: Optional[List[Node]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Media':
        assert isinstance(obj, dict)
        nodes = from_union([lambda x: from_list(Node.from_dict, x), from_none], obj.get("nodes"))
        return Media(nodes)

    def to_dict(self) -> dict:
        result: dict = {
            "nodes": from_union([lambda x: from_list(lambda x: to_class(Node, x), x), from_none], self.nodes)}
        return result


@dataclass
class Name:
    full: Optional[str] = None
    native: Optional[str] = None
    alternative: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Name':
        assert isinstance(obj, dict)
        full = from_union([from_str, from_none], obj.get("full"))
        native = from_union([from_str, from_none], obj.get("native"))
        alternative = from_union([lambda x: from_list(from_str, x), from_none], obj.get("alternative"))
        return Name(full, native, alternative)

    def to_dict(self) -> dict:
        result: dict = {"full": from_union([from_str, from_none], self.full),
                        "native": from_union([from_str, from_none], self.native),
                        "alternative": from_union([lambda x: from_list(from_str, x), from_none], self.alternative)}
        return result


@dataclass
class Character:
    age: None
    name: Optional[Name] = None
    description: Optional[str] = None
    image: Optional[Image] = None
    media: Optional[Media] = None
    site_url: Optional[str] = None
    date_of_birth: Optional[DateOfBirth] = None
    favourites: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Character':
        assert isinstance(obj, dict)
        age = from_none(obj.get("age"))
        name = from_union([Name.from_dict, from_none], obj.get("name"))
        description = from_union([from_none, from_str], obj.get("description"))
        image = from_union([Image.from_dict, from_none], obj.get("image"))
        media = from_union([Media.from_dict, from_none], obj.get("media"))
        site_url = from_union([from_str, from_none], obj.get("siteUrl"))
        date_of_birth = from_union([DateOfBirth.from_dict, from_none], obj.get("dateOfBirth"))
        favourites = from_union([from_int, from_none], obj.get("favourites"))
        return Character(age, name, description, image, media, site_url, date_of_birth, favourites)

    def to_dict(self) -> dict:
        result: dict = {"age": from_none(self.age),
                        "name": from_union([lambda x: to_class(Name, x), from_none], self.name),
                        "description": from_union([from_none, from_str], self.description),
                        "image": from_union([lambda x: to_class(Image, x), from_none], self.image),
                        "media": from_union([lambda x: to_class(Media, x), from_none], self.media),
                        "siteUrl": from_union([from_str, from_none], self.site_url),
                        "dateOfBirth": from_union([lambda x: to_class(DateOfBirth, x), from_none], self.date_of_birth),
                        "favourites": from_union([from_int, from_none], self.favourites)}
        return result


@dataclass
class Page:
    characters: Optional[List[Character]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Page':
        assert isinstance(obj, dict)
        characters = from_union([lambda x: from_list(Character.from_dict, x), from_none], obj.get("characters"))
        return Page(characters)

    def to_dict(self) -> dict:
        result: dict = {"characters": from_union([lambda x: from_list(lambda x: to_class(Character, x), x), from_none],
                                                 self.characters)}
        return result


@dataclass
class Data:
    page: Optional[Page] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        page = from_union([Page.from_dict, from_none], obj.get("Page"))
        return Data(page)

    def to_dict(self) -> dict:
        result: dict = {"Page": from_union([lambda x: to_class(Page, x), from_none], self.page)}
        return result


@dataclass
class AnilistCharacter:
    data: Optional[Data] = None
    errors: Optional[List[Error]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AnilistCharacter':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        return AnilistCharacter(data)

    def to_dict(self) -> dict:
        result: dict = {"data": from_union([lambda x: to_class(Data, x), from_none], self.data)}
        return result
