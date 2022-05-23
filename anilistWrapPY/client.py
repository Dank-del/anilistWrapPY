# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>


from anilistWrapPY.Airing.request import GetAiring
from anilistWrapPY.Airing.types import AnilistAiring
from anilistWrapPY.Anime.types import AniListAnime
from anilistWrapPY.Character.types import AnilistCharacter
from anilistWrapPY.Manga.request import GetManga
from anilistWrapPY.Anime.request import GetAnime
from anilistWrapPY.Character.request import GetCharacter
from anilistWrapPY.Manga.types import AnilistManga
from anilistWrapPY.Media.request import GetMedia
from anilistWrapPY.Media.types import AnilistMedia
from anilistWrapPY.User.request import GetUser
from anilistWrapPY.User.types import AnilistUser


class aniWrapPYClient:
    def __init__(self, *, baseUrl: str = "https://graphql.anilist.co") -> None:
        self.baseUrl = baseUrl

    def Anime(self, query: str) -> AniListAnime:
        return GetAnime(search=query, baseUrl=self.baseUrl)

    def Media(self, query: str) -> AnilistMedia:
        return GetMedia(search=query, baseUrl=self.baseUrl)

    def Character(self, query: str) -> AnilistCharacter:
        return GetCharacter(search=query, baseUrl=self.baseUrl)

    def Manga(self, query: str) -> AnilistManga:
        return GetManga(search=query, baseUrl=self.baseUrl)

    def Airing(self, query: str) -> AnilistAiring:
        return GetAiring(search=query, baseUrl=self.baseUrl)

    def User(self, query: str) -> AnilistUser:
        return GetUser(search=query, baseUrl=self.baseUrl)
