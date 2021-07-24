# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

from dataclasses import dataclass
from typing import Optional, Any, List

from anilistWrapPY.utils import from_union, from_str, from_none, from_int, from_list, to_class


@dataclass
class ExternalLink:
    url: Optional[str] = None
    site: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ExternalLink':
        assert isinstance(obj, dict)
        url = from_union([from_str, from_none], obj.get("url"))
        site = from_union([from_str, from_none], obj.get("site"))
        return ExternalLink(url, site)

    def to_dict(self) -> dict:
        result: dict = {}
        result["url"] = from_union([from_str, from_none], self.url)
        result["site"] = from_union([from_str, from_none], self.site)
        return result


@dataclass
class StartDate:
    year: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StartDate':
        assert isinstance(obj, dict)
        year = from_union([from_int, from_none], obj.get("year"))
        return StartDate(year)

    def to_dict(self) -> dict:
        result: dict = {"year": from_union([from_int, from_none], self.year)}
        return result


@dataclass
class Node:
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Node':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        return Node(name)

    def to_dict(self) -> dict:
        result: dict = {"name": from_union([from_str, from_none], self.name)}
        return result


@dataclass
class Studios:
    nodes: Optional[List[Node]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Studios':
        assert isinstance(obj, dict)
        nodes = from_union([lambda x: from_list(Node.from_dict, x), from_none], obj.get("nodes"))
        return Studios(nodes)

    def to_dict(self) -> dict:
        result: dict = {
            "nodes": from_union([lambda x: from_list(lambda x: to_class(Node, x), x), from_none], self.nodes)}
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
        result: dict = {"romaji": from_union([from_str, from_none], self.romaji),
                        "english": from_union([from_none, from_str], self.english),
                        "native": from_union([from_str, from_none], self.native)}
        return result


@dataclass
class Trailer:
    id: Optional[str] = None
    site: Optional[str] = None
    thumbnail: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Trailer':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        site = from_union([from_str, from_none], obj.get("site"))
        thumbnail = from_union([from_str, from_none], obj.get("thumbnail"))
        return Trailer(id, site, thumbnail)

    def to_dict(self) -> dict:
        result: dict = {"id": from_union([from_str, from_none], self.id),
                        "site": from_union([from_str, from_none], self.site),
                        "thumbnail": from_union([from_str, from_none], self.thumbnail)}
        return result


@dataclass
class Media:
    id: Optional[int] = None
    title: Optional[Title] = None
    description: Optional[str] = None
    start_date: Optional[StartDate] = None
    episodes: Optional[int] = None
    season: Optional[str] = None
    type: Optional[str] = None
    format: Optional[str] = None
    status: Optional[str] = None
    duration: Optional[int] = None
    site_url: Optional[str] = None
    studios: Optional[Studios] = None
    trailer: Optional[Trailer] = None
    external_links: Optional[List[ExternalLink]] = None
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
        episodes = from_union([from_int, from_none], obj.get("episodes"))
        season = from_union([from_str, from_none], obj.get("season"))
        type = from_union([from_str, from_none], obj.get("type"))
        format = from_union([from_str, from_none], obj.get("format"))
        status = from_union([from_str, from_none], obj.get("status"))
        duration = from_union([from_int, from_none], obj.get("duration"))
        site_url = from_union([from_str, from_none], obj.get("siteUrl"))
        studios = from_union([Studios.from_dict, from_none], obj.get("studios"))
        trailer = from_union([Trailer.from_dict, from_none], obj.get("trailer"))
        external_links = from_union([lambda x: from_list(ExternalLink.from_dict, x), from_none], obj.get("externalLinks"))
        average_score = from_union([from_int, from_none], obj.get("averageScore"))
        genres = from_union([lambda x: from_list(from_str, x), from_none], obj.get("genres"))
        banner_image = from_union([from_none, from_str], obj.get("bannerImage"))
        return Media(id, title, description, start_date, episodes, season, type, format, status, duration, site_url, studios, trailer, external_links, average_score, genres, banner_image)

    def to_dict(self) -> dict:
        result: dict = {"id": from_union([from_int, from_none], self.id),
                        "title": from_union([lambda x: to_class(Title, x), from_none], self.title),
                        "description": from_union([from_str, from_none], self.description),
                        "startDate": from_union([lambda x: to_class(StartDate, x), from_none], self.start_date),
                        "episodes": from_union([from_int, from_none], self.episodes),
                        "season": from_union([from_str, from_none], self.season),
                        "type": from_union([from_str, from_none], self.type),
                        "format": from_union([from_str, from_none], self.format),
                        "status": from_union([from_str, from_none], self.status),
                        "duration": from_union([from_int, from_none], self.duration),
                        "siteUrl": from_union([from_str, from_none], self.site_url),
                        "studios": from_union([lambda x: to_class(Studios, x), from_none], self.studios),
                        "trailer": from_union([lambda x: to_class(Trailer, x), from_none], self.trailer),
                        "externalLinks": from_union(
                            [lambda x: from_list(lambda x: to_class(ExternalLink, x), x), from_none],
                            self.external_links), "averageScore": from_union([from_int, from_none], self.average_score),
                        "genres": from_union([lambda x: from_list(from_str, x), from_none], self.genres),
                        "bannerImage": from_union([from_none, from_str], self.banner_image)}
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
        result: dict = {
            "media": from_union([lambda x: from_list(lambda x: to_class(Media, x), x), from_none], self.media)}
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
class AniListAnime:
    data: Optional[Data] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AniListAnime':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        return AniListAnime(data)

    def to_dict(self) -> dict:
        result: dict = {"data": from_union([lambda x: to_class(Data, x), from_none], self.data)}
        return result


def ani_list_anime_from_dict(s: Any) -> AniListAnime:
    return AniListAnime.from_dict(s)


def ani_list_anime_to_dict(x: AniListAnime) -> Any:
    return to_class(AniListAnime, x)
