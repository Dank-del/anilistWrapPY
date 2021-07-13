# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

from dataclasses import dataclass
from typing import Any, Optional, List, TypeVar, Type, cast, Callable


T = TypeVar("T")


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


@dataclass
class DateOfBirth:
    year: None
    month: None
    day: None

    @staticmethod
    def from_dict(obj: Any) -> 'DateOfBirth':
        assert isinstance(obj, dict)
        year = from_none(obj.get("year"))
        month = from_none(obj.get("month"))
        day = from_none(obj.get("day"))
        return DateOfBirth(year, month, day)

    def to_dict(self) -> dict:
        result: dict = {}
        result["year"] = from_none(self.year)
        result["month"] = from_none(self.month)
        result["day"] = from_none(self.day)
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
        result: dict = {}
        result["large"] = from_union([from_str, from_none], self.large)
        return result


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
        result: dict = {}
        result["romaji"] = from_union([from_str, from_none], self.romaji)
        result["english"] = from_union([from_none, from_str], self.english)
        result["native"] = from_union([from_str, from_none], self.native)
        return result


@dataclass
class Node:
    title: Optional[Title] = None
    type: Optional[str] = None
    format: Optional[str] = None
    site_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Node':
        assert isinstance(obj, dict)
        title = from_union([Title.from_dict, from_none], obj.get("title"))
        type = from_union([from_str, from_none], obj.get("type"))
        format = from_union([from_str, from_none], obj.get("format"))
        site_url = from_union([from_str, from_none], obj.get("siteUrl"))
        return Node(title, type, format, site_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_union([lambda x: to_class(Title, x), from_none], self.title)
        result["type"] = from_union([from_str, from_none], self.type)
        result["format"] = from_union([from_str, from_none], self.format)
        result["siteUrl"] = from_union([from_str, from_none], self.site_url)
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
        result: dict = {}
        result["nodes"] = from_union([lambda x: from_list(lambda x: to_class(Node, x), x), from_none], self.nodes)
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
        result: dict = {}
        result["full"] = from_union([from_str, from_none], self.full)
        result["native"] = from_union([from_str, from_none], self.native)
        result["alternative"] = from_union([lambda x: from_list(from_str, x), from_none], self.alternative)
        return result


@dataclass
class Character:
    age: Optional[int] = None
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
        age = from_union([from_none, lambda x: int(from_str(x))], obj.get("age"))
        name = from_union([Name.from_dict, from_none], obj.get("name"))
        description = from_union([from_str, from_none], obj.get("description"))
        image = from_union([Image.from_dict, from_none], obj.get("image"))
        media = from_union([Media.from_dict, from_none], obj.get("media"))
        site_url = from_union([from_str, from_none], obj.get("siteUrl"))
        date_of_birth = from_union([DateOfBirth.from_dict, from_none], obj.get("dateOfBirth"))
        favourites = from_union([from_int, from_none], obj.get("favourites"))
        return Character(age, name, description, image, media, site_url, date_of_birth, favourites)

    def to_dict(self) -> dict:
        result: dict = {}
        result["age"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.age)
        result["name"] = from_union([lambda x: to_class(Name, x), from_none], self.name)
        result["description"] = from_union([from_str, from_none], self.description)
        result["image"] = from_union([lambda x: to_class(Image, x), from_none], self.image)
        result["media"] = from_union([lambda x: to_class(Media, x), from_none], self.media)
        result["siteUrl"] = from_union([from_str, from_none], self.site_url)
        result["dateOfBirth"] = from_union([lambda x: to_class(DateOfBirth, x), from_none], self.date_of_birth)
        result["favourites"] = from_union([from_int, from_none], self.favourites)
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
        result: dict = {}
        result["characters"] = from_union([lambda x: from_list(lambda x: to_class(Character, x), x), from_none], self.characters)
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
        result: dict = {}
        result["Page"] = from_union([lambda x: to_class(Page, x), from_none], self.page)
        return result


@dataclass
class AniListCharacter:
    data: Optional[Data] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AniListCharacter':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        return AniListCharacter(data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        return result


def ani_list_character_from_dict(s: Any) -> AniListCharacter:
    return AniListCharacter.from_dict(s)


def ani_list_character_to_dict(x: AniListCharacter) -> Any:
    return to_class(AniListCharacter, x)