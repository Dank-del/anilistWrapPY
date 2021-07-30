# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

from anilistWrapPY.errors.types import Error
from dataclasses import dataclass
from typing import Optional, Any, List

from anilistWrapPY.utils import from_union, from_str, from_none, from_int, from_list, to_class


@dataclass
class NextAiringEpisode:
    airing_at: Optional[int] = None
    time_until_airing: Optional[int] = None
    episode: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'NextAiringEpisode':
        assert isinstance(obj, dict)
        airing_at = from_union([from_int, from_none], obj.get("airingAt"))
        time_until_airing = from_union([from_int, from_none], obj.get("timeUntilAiring"))
        episode = from_union([from_int, from_none], obj.get("episode"))
        return NextAiringEpisode(airing_at, time_until_airing, episode)

    def to_dict(self) -> dict:
        result: dict = {}
        result["airingAt"] = from_union([from_int, from_none], self.airing_at)
        result["timeUntilAiring"] = from_union([from_int, from_none], self.time_until_airing)
        result["episode"] = from_union([from_int, from_none], self.episode)
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
    banner_image: Optional[str] = None
    episodes: Optional[int] = None
    title: Optional[Title] = None
    site_url: Optional[str] = None
    next_airing_episode: Optional[NextAiringEpisode] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Media':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        banner_image = from_union([from_none, from_str], obj.get("bannerImage"))
        episodes = from_union([from_int, from_none], obj.get("episodes"))
        title = from_union([Title.from_dict, from_none], obj.get("title"))
        site_url = from_union([from_str, from_none], obj.get("siteUrl"))
        next_airing_episode = from_union([NextAiringEpisode.from_dict, from_none], obj.get("nextAiringEpisode"))
        return Media(id, banner_image, episodes, title, site_url, next_airing_episode)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_int, from_none], self.id)
        result["bannerImage"] = from_union([from_none, from_str], self.banner_image)
        result["episodes"] = from_union([from_int, from_none], self.episodes)
        result["title"] = from_union([lambda x: to_class(Title, x), from_none], self.title)
        result["siteUrl"] = from_union([from_str, from_none], self.site_url)
        result["nextAiringEpisode"] = from_union([lambda x: to_class(NextAiringEpisode, x), from_none], self.next_airing_episode)
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
class AnilistAiring:
    data: Optional[Data] = None
    errors: Optional[List[Error]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AnilistAiring':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        return AnilistAiring(data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        return result
