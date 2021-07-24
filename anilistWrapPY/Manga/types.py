# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

from dataclasses import dataclass
from typing import Optional, Any, List

from anilistWrapPY.utils import from_union, from_str, from_none, from_int, from_list, to_class


@dataclass
class StartDate:
    year: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StartDate':
        assert isinstance(obj, dict)
        year = from_union([from_int, from_none], obj.get("year"))
        return StartDate(year)

    def to_dict(self) -> dict:
        result: dict = {}
        result["year"] = from_union([from_int, from_none], self.year)
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
class Media:
    id: Optional[int] = None
    title: Optional[Title] = None
    description: Optional[str] = None
    start_date: Optional[StartDate] = None
    type: Optional[str] = None
    format: Optional[str] = None
    status: Optional[str] = None
    site_url: Optional[str] = None
    average_score: Optional[int] = None
    genres: Optional[List[str]] = None
    banner_image: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Media':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        title = from_union([Title.from_dict, from_none], obj.get("title"))
        description = from_union([from_str, from_none], obj.get("description"))
        start_date = from_union([StartDate.from_dict, from_none], obj.get("startDate"))
        type = from_union([from_str, from_none], obj.get("type"))
        format = from_union([from_str, from_none], obj.get("format"))
        status = from_union([from_str, from_none], obj.get("status"))
        site_url = from_union([from_str, from_none], obj.get("siteUrl"))
        average_score = from_union([from_int, from_none], obj.get("averageScore"))
        genres = from_union([lambda x: from_list(from_str, x), from_none], obj.get("genres"))
        banner_image = from_union([from_none, from_str], obj.get("bannerImage"))
        return Media(id, title, description, start_date, type, format, status, site_url, average_score, genres, banner_image)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_int, from_none], self.id)
        result["title"] = from_union([lambda x: to_class(Title, x), from_none], self.title)
        result["description"] = from_union([from_str, from_none], self.description)
        result["startDate"] = from_union([lambda x: to_class(StartDate, x), from_none], self.start_date)
        result["type"] = from_union([from_str, from_none], self.type)
        result["format"] = from_union([from_str, from_none], self.format)
        result["status"] = from_union([from_str, from_none], self.status)
        result["siteUrl"] = from_union([from_str, from_none], self.site_url)
        result["averageScore"] = from_union([from_int, from_none], self.average_score)
        result["genres"] = from_union([lambda x: from_list(from_str, x), from_none], self.genres)
        result["bannerImage"] = from_union([from_none, from_str], self.banner_image)
        return result


@dataclass
class Page:
    media: Optional[List[Media]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Page':
        assert isinstance(obj, dict)
        media = from_union([lambda x: from_list(Media.from_dict, x), from_none], obj.get("media"))
        return Page(media)

    def to_dict(self) -> dict:
        result: dict = {}
        result["media"] = from_union([lambda x: from_list(lambda x: to_class(Media, x), x), from_none], self.media)
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
class AnilistManga:
    data: Optional[Data] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AnilistManga':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        return AnilistManga(data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        return result


def anilist_manga_from_dict(s: Any) -> AnilistManga:
    return AnilistManga.from_dict(s)


def anilist_manga_to_dict(x: AnilistManga) -> Any:
    return to_class(AnilistManga, x)
