from dataclasses import dataclass
from typing import Optional, List, Any, TypeVar, Callable, Type, cast
from enum import Enum


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


@dataclass
class AiringSchedule:
    nodes: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AiringSchedule':
        assert isinstance(obj, dict)
        nodes = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("nodes"))
        return AiringSchedule(nodes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["nodes"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.nodes)
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
        result: dict = {}
        result["url"] = from_union([from_str, from_none], self.url)
        return result


class Format(Enum):
    MANGA = "MANGA"
    ONE_SHOT = "ONE_SHOT"
    TV = "TV"


class Status(Enum):
    FINISHED = "FINISHED"


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


class TypeEnum(Enum):
    ANIME = "ANIME"
    MANGA = "MANGA"


@dataclass
class Media:
    id: Optional[int] = None
    title: Optional[Title] = None
    type: Optional[TypeEnum] = None
    format: Optional[Format] = None
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
        format = from_union([Format, from_none], obj.get("format"))
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
        result: dict = {}
        result["id"] = from_union([from_int, from_none], self.id)
        result["title"] = from_union([lambda x: to_class(Title, x), from_none], self.title)
        result["type"] = from_union([lambda x: to_enum(TypeEnum, x), from_none], self.type)
        result["format"] = from_union([lambda x: to_enum(Format, x), from_none], self.format)
        result["status"] = from_union([lambda x: to_enum(Status, x), from_none], self.status)
        result["description"] = from_union([from_none, from_str], self.description)
        result["episodes"] = from_union([from_int, from_none], self.episodes)
        result["bannerImage"] = from_union([from_none, from_str], self.banner_image)
        result["externalLinks"] = from_union([lambda x: from_list(lambda x: to_class(ExternalLink, x), x), from_none], self.external_links)
        result["duration"] = from_union([from_int, from_none], self.duration)
        result["chapters"] = from_union([from_int, from_none], self.chapters)
        result["volumes"] = from_union([from_int, from_none], self.volumes)
        result["genres"] = from_union([lambda x: from_list(from_str, x), from_none], self.genres)
        result["synonyms"] = from_union([lambda x: from_list(from_str, x), from_none], self.synonyms)
        result["averageScore"] = from_union([from_int, from_none], self.average_score)
        result["airingSchedule"] = from_union([lambda x: to_class(AiringSchedule, x), from_none], self.airing_schedule)
        result["siteUrl"] = from_union([from_str, from_none], self.site_url)
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
class AniListMedia:
    data: Optional[Data] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AniListMedia':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        return AniListMedia(data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        return result


def ani_list_media_from_dict(s: Any) -> AniListMedia:
    return AniListMedia.from_dict(s)


def ani_list_media_to_dict(x: AniListMedia) -> Any:
    return to_class(AniListMedia, x)
