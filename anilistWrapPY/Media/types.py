# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Any, List

from anilistWrapPY.utils import from_union, from_int, from_none, from_list, to_class, from_str, to_enum


@dataclass
class Node:
    airing_at: Optional[int] = None
    time_until_airing: Optional[int] = None
    episode: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Node':
        assert isinstance(obj, dict)
        airing_at = from_union([from_int, from_none], obj.get("airingAt"))
        time_until_airing = from_union([from_int, from_none], obj.get("timeUntilAiring"))
        episode = from_union([from_int, from_none], obj.get("episode"))
        return Node(airing_at, time_until_airing, episode)

    def to_dict(self) -> dict:
        result: dict = {"airingAt": from_union([from_int, from_none], self.airing_at),
                        "timeUntilAiring": from_union([from_int, from_none], self.time_until_airing),
                        "episode": from_union([from_int, from_none], self.episode)}
        return result


@dataclass
class AiringSchedule:
    nodes: Optional[List[Node]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AiringSchedule':
        assert isinstance(obj, dict)
        nodes = from_union([lambda x: from_list(Node.from_dict, x), from_none], obj.get("nodes"))
        return AiringSchedule(nodes)

    def to_dict(self) -> dict:
        result: dict = {
            "nodes": from_union([lambda x: from_list(lambda x: to_class(Node, x), x), from_none], self.nodes)}
        return result


@dataclass
class ExternalLink:
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ExternalLink':
        assert isinstance(obj, dict)
        url = from_union([from_str, from_none], obj.get("url"))
        return ExternalLink(url)

    def to_dict(self) -> dict:
        result: dict = {"url": from_union([from_str, from_none], self.url)}
        return result


class Status(Enum):
    FINISHED = "FINISHED"
    NOT_YET_RELEASED = "NOT_YET_RELEASED"
    RELEASING = "RELEASING"


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
class Media:
    id: Optional[int] = None
    title: Optional[Title] = None
    type: Optional[TypeEnum] = None
    format: Optional[str] = None
    status: Optional[Status] = None
    description: Optional[str] = None
    episodes: Optional[int] = None
    banner_image: Optional[str] = None
    external_links: Optional[List[ExternalLink]] = None
    duration: Optional[int] = None
    chapters: Optional[int] = None
    volumes: Optional[int] = None
    genres: Optional[List[str]] = None
    synonyms: Optional[List[str]] = None
    average_score: Optional[int] = None
    airing_schedule: Optional[AiringSchedule] = None
    site_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Media':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        title = from_union([Title.from_dict, from_none], obj.get("title"))
        type = from_union([TypeEnum, from_none], obj.get("type"))
        format = from_union([from_str, from_none], obj.get("format"))
        status = from_union([Status, from_none], obj.get("status"))
        description = from_union([from_none, from_str], obj.get("description"))
        episodes = from_union([from_int, from_none], obj.get("episodes"))
        banner_image = from_union([from_none, from_str], obj.get("bannerImage"))
        external_links = from_union([lambda x: from_list(ExternalLink.from_dict, x), from_none], obj.get("externalLinks"))
        duration = from_union([from_int, from_none], obj.get("duration"))
        chapters = from_union([from_int, from_none], obj.get("chapters"))
        volumes = from_union([from_int, from_none], obj.get("volumes"))
        genres = from_union([lambda x: from_list(from_str, x), from_none], obj.get("genres"))
        synonyms = from_union([lambda x: from_list(from_str, x), from_none], obj.get("synonyms"))
        average_score = from_union([from_int, from_none], obj.get("averageScore"))
        airing_schedule = from_union([AiringSchedule.from_dict, from_none], obj.get("airingSchedule"))
        site_url = from_union([from_str, from_none], obj.get("siteUrl"))
        return Media(id, title, type, format, status, description, episodes, banner_image, external_links, duration, chapters, volumes, genres, synonyms, average_score, airing_schedule, site_url)

    def to_dict(self) -> dict:
        result: dict = {"id": from_union([from_int, from_none], self.id),
                        "title": from_union([lambda x: to_class(Title, x), from_none], self.title),
                        "type": from_union([lambda x: to_enum(TypeEnum, x), from_none], self.type),
                        "format": from_union([from_str, from_none], self.format),
                        "status": from_union([lambda x: to_enum(Status, x), from_none], self.status),
                        "description": from_union([from_none, from_str], self.description),
                        "episodes": from_union([from_int, from_none], self.episodes),
                        "bannerImage": from_union([from_none, from_str], self.banner_image),
                        "externalLinks": from_union(
                            [lambda x: from_list(lambda x: to_class(ExternalLink, x), x), from_none],
                            self.external_links), "duration": from_union([from_int, from_none], self.duration),
                        "chapters": from_union([from_int, from_none], self.chapters),
                        "volumes": from_union([from_int, from_none], self.volumes),
                        "genres": from_union([lambda x: from_list(from_str, x), from_none], self.genres),
                        "synonyms": from_union([lambda x: from_list(from_str, x), from_none], self.synonyms),
                        "averageScore": from_union([from_int, from_none], self.average_score),
                        "airingSchedule": from_union([lambda x: to_class(AiringSchedule, x), from_none],
                                                     self.airing_schedule),
                        "siteUrl": from_union([from_str, from_none], self.site_url)}
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
class AnilistMedia:
    data: Optional[Data] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AnilistMedia':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        return AnilistMedia(data)

    def to_dict(self) -> dict:
        result: dict = {"data": from_union([lambda x: to_class(Data, x), from_none], self.data)}
        return result


def anilist_media_from_dict(s: Any) -> AnilistMedia:
    return AnilistMedia.from_dict(s)


def anilist_media_to_dict(x: AnilistMedia) -> Any:
    return to_class(AnilistMedia, x)
